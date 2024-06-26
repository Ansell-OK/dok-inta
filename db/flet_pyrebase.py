import pyrebase
from db.config import config as keys
from flet.security import encrypt, decrypt

secret_key = 'dokintaadmin'

class PyrebaseWrapper:
    """
    Wraps Pyrebase with flet authentication flow and abstracts crud for my app.
    """

    def __init__(self, page):
        self.page = page
        self.firebase = pyrebase.initialize_app(keys)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.storage = self.firebase.storage()
        self.idToken = None
        self.uuid = None
        self.check_token()

        self.streams = []

    def save_tokens(self, token, uuid, page, refresh_token=None):
        encrypted_token = encrypt(token, secret_key)
        page.client_storage.set("firebase_token", encrypted_token)
        page.client_storage.set("firebase_id", uuid)
        self.idToken = token
        self.uuid = uuid
        if refresh_token:
            page.client_storage.set("firebase_refresh_token", refresh_token)
    
    def erase_token(self):
        self.page.client_storage.remove("firebase_token")
        self.page.client_storage.remove("firebase_id")
        self.page.client_storage.remove("firebase_refresh_token")

    def register_user(self, name, username, email, password, image_url= 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/download%20(1).jpeg?alt=media&token=7ec5832a-79fb-4381-b8f3-2d18d88708cb', DOB = '', gender = '', phone_number = ''):
        self.auth.create_user_with_email_and_password(email, password)
        self.sign_in(email, password)
        data = {"name": name, "username": username, 'email': email, "image_url": image_url,  'is_online': False, 'DOB': DOB,'gender': gender, 'phone_number': phone_number}
        self.db.child("users").child(self.uuid).update(data = data, token=self.idToken)

    def sign_in(self, email, password):
        user = self.auth.sign_in_with_email_and_password(email, password)
        self.db.child("users").child(user['localId']).update({"is_online": True})
        if user:
            token = user["idToken"]
            uuid = user["localId"]
            refresh_token = user["refreshToken"]
            self.save_tokens(token, uuid, self.page, refresh_token)

    def sign_out(self):
        self.db.child('users').child(self.uuid).update({'is_online': False})
        self.erase_token()

    def check_token(self):
        ### Prevents the user from having to sign in all the time
        encrypted_token = self.page.client_storage.get("firebase_token")
        uuid = self.page.client_storage.get("firebase_id")
        if encrypted_token:
            decrypted_token = decrypt(encrypted_token, secret_key)
            self.idToken = decrypted_token
            self.uuid = uuid
            try:
                self.auth.get_account_info(self.idToken)
                return "Success"
            except:
                return self.refresh_token()
        return None

    def refresh_token(self):
        refresh_token = self.page.client_storage.get("firebase_refresh_token")
        if refresh_token:
            try:
                refreshed_user = self.auth.refresh(refresh_token)
                self.save_tokens(refreshed_user["idToken"], refreshed_user["userId"], self.page, refreshed_user["refreshToken"])
                return "Token refreshed successfully"
            except Exception as e:
                print(f"Failed to refresh token: {e}")
                return "Failed to refresh token"
        return "No refresh token available"

    def get_username(self):
        return self.db.child("users").child(self.uuid).child("username").get(token=self.idToken).val()

    def add_conversation(self, user_message, prediction):
        if self.uuid == None:
            self.uuid = self.auth.get_account_info(self.idToken)["users"][0]["localId"]
        data = {"user_message": user_message, "prediction": prediction}
        self.db.child("users").child(self.uuid).child("conversations").push(data, self.idToken)
    
    def get_conversation(self):
        return self.db.child("users").child(self.uuid).get(token=self.idToken).val()
    
    def stream_data_conversation_main(self, stream_handler):
        stream = self.db.child("users").child(self.uuid).child("conversations").stream(stream_handler=stream_handler, token=self.idToken)
        self.streams.append(stream)
    
    def add_profile(self, image_name, image_path):
        if self.uuid == None:
            self.uuid = self.auth.get_account_info(self.idToken)['users'][0]["localId"]
        self.storage.child(image_name).put(image_path)
        image_url = self.storage.child(image_name).get_url(None)
        self.db.child('users').child(self.uuid).child('image_url').set(image_url, self.idToken)
    
    def add_info(self, name, email, DOB, gender, phone_number):
        if self.uuid == None:
            self.uuid = self.auth.get_account_info(self.idToken)['users'][0]['localId']
        data = {'name': name, 'email': email, 'DOB': DOB, 'gender': gender, 'phone_number': phone_number}
        self.db.child("users").child(self.uuid).update(data = data, token=self.idToken)
    
    def add_medical_info(self, weight, blood_group, genotype, previous_ailments):
        if self.uuid == None:
            self.uuid = self.auth.get_account_info(self.idToken)['users'][0]['localId']
        data = {'weight': weight, 'blood_group': blood_group, 'genotype': genotype, 'previous_ailments': previous_ailments}
        self.db.child("users").child(self.uuid).child("medical_info").set(data, self.idToken)
    
    def get_medical_info(self):
        return self.db.child("users").child(self.uuid).get(token=self.idToken).val()
    
    def get_user_info(self):
        return self.db.child("users").child(self.uuid).get(token=self.idToken).val()
    
    def get_image_url(self):
        try:
            if self.idToken is None:
                raise Exception("idToken is None")
            if self.uuid is None:
                raise Exception("uuid is None")
            
            image_url = self.db.child("users").child(self.uuid).child('image_url').get(token=self.idToken).val()
            if image_url is None:
                image_url = 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/download%20(1).jpeg?alt=media&token=7ec5832a-79fb-4381-b8f3-2d18d88708cb'
                return image_url
            return image_url
        except Exception as e:
            print(f"Error getting image_url: {e}")
            return None

    def fetch_online_doctors(self):
        try:
            doctors = self.db.child("doctors").get()
            all_doctors = []
            if doctors.each():
                for doctor in doctors.each():
                    doctor_data = doctor.val()
                    doctor_id = doctor.key()
                    all_doctors.append({
                        "doctor_id": doctor_id,
                        "name": doctor_data.get("name"),
                        "speciality": doctor_data.get("speaciality"),
                        "image_url": doctor_data.get("image_url"),
                        "is_online": doctor_data.get("is_online")
                    })
            return all_doctors
        except Exception as e:
            print(f"Error fetching doctors: {e}")
            return []
        
    def create_chat_room(self, doctor_id):
        chat_rooms = self.db.child("chat_rooms").get(self.idToken)
        if chat_rooms.each():
            for chat_room in chat_rooms.each():
                data = chat_room.val()
                if data["doctor_id"] == doctor_id and data["patient_id"] == self.uuid:
                    return chat_room.key()
        chat_room_data = {"doctor_id": doctor_id, "patient_id": self.uuid}
        chat_room = self.db.child("chat_rooms").push(chat_room_data, self.idToken)
        return chat_room['name']

    def send_message(self, chat_room_id, message, sender_type):
        message_data = {"sender_type": sender_type, "message": message, "read": False}
        self.db.child("chat_rooms").child(chat_room_id).child("messages").push(message_data, self.idToken)
    
    def stream_data_conversation(self, chat_room_id, stream_handler):
        stream = self.db.child("chat_rooms").child(chat_room_id).child("messages").stream(stream_handler=stream_handler, token=self.idToken)
        self.streams.append(stream)

    def chatroom_messages(self, chat_room_id):
        return self.db.child('chat_rooms').child(chat_room_id).child("messages").get(self.idToken).val()

    def get_chat_rooms_for_doctor(self):
        chat_rooms = self.db.child("chat_rooms").get(self.idToken)
        if chat_rooms.each():
            patient_chat_rooms = []
            for chat_room in chat_rooms.each():
                data = chat_room.val()
                if data["patient_id"] == self.uuid:
                    patient_chat_rooms.append({"id": chat_room.key(), "data": data})
            return patient_chat_rooms
        return []
    
    def get_doctor_info(self, doctor_id):
        patient = self.db.child("doctors").child(doctor_id).get(self.idToken)
        if patient.val():
            return patient.val()
        return None
    
    def fetch_unread_messages(self, chat_room_id):
        messages = self.db.child("chat_rooms").child(chat_room_id).child("messages").get(token=self.idToken).val()
        if messages == None:
            return []
        else:
            unread_messages = {k: v for k, v in messages.items() if not v.get('read')}
            return unread_messages

    def notify_unread_messages(self, chat_room_id):
        unread_messages = self.fetch_unread_messages(chat_room_id)
        return len(unread_messages)

    def mark_messages_as_read(self, chat_room_id):
        messages = self.db.child("chat_rooms").child(chat_room_id).child("messages").get(token=self.idToken).val()
        if messages == None:
            pass
        else:
            for key, msg in messages.items():
                if not msg['read']:
                    self.db.child("chat_rooms").child(chat_room_id).child("messages").child(key).update({"read": True}, self.idToken)

    def get_doctor_info(self, doctor_id):
        doctor = self.db.child("doctors").child(doctor_id).get(self.idToken)
        if doctor.val():
            print(doctor.val())
            return doctor.val()
    
    def kill_streams(self):
        for stream in self.streams:
            try:
                stream.close()
            except Exception as e:
                print(f"Failed to close stream: {e}")
        self.streams.clear()

    def cleanup(self):
        self.kill_streams()
