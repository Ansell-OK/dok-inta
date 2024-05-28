from flet import * 
from utils import *
from user_controls.doctor_cards import DoctorCard
from user_controls.recent_messages import RecentMessages
def HomePage(page: Page, myPyrebase=None):

    file_picker = FilePicker()
    page.overlay.append(file_picker)
    page.update()

    def check_none():
        image_url = myPyrebase.get_image_url()
        if image_url is None:
            return 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/download%20(1).jpeg?alt=media&token=7ec5832a-79fb-4381-b8f3-2d18d88708cb'
        else:
            return image_url
    
    image_url = check_none()

    online_doctors = myPyrebase.fetch_online_doctors()

   

    page.adaptive = 0
    page.fonts = {
        'Poppins Regular': '/fonts/poppins/Poppins-Regular.ttf',
        'Poppins Bold': '/fonts/poppins/Poppins-Bold.ttf'
    }

    ProfileName = Text('Welcome back', font_family='Poppins Bold', size=17, color=TEXT_COLOR)

    def on_dialog_result(e: FilePickerResultEvent):
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                print(f'File: {f.name}')
                print(f'File: {f.path}')

                myPyrebase.add_profile(f.name, f.path)

                


    file_picker = FilePicker(on_result= on_dialog_result)
    page.overlay.append(file_picker)
    page.update()
    
    def handle_logout(*e):
        ProfileName.value = ""
        myPyrebase.kill_all_streams()
        myPyrebase.sign_out()
        page.go("/register")

    

    def on_page_load():
        ProfileName.value = "Welcome back"
        if myPyrebase.check_token() == "Success":
            handle = myPyrebase.get_username()
            build_recent()
            build_doctorcards()
            if handle:
                ProfileName.value = "Welcome Back, " +  handle
            page.update()

    

    def showMenu(e, screen):
        screen.height = BASE_HEIGHT
        screen.width = 250

        page.update()
    
    def hideMenu(e, screen):
        screen.height = 0
        screen.width = 0 

        page.update()
    
    doctor_cards = []
    recent_messages = []

    def build_recent():
        recent_messages.clear()
        chat_rooms = myPyrebase.get_chat_rooms_for_doctor()
        if chat_rooms:
            for chat_room in chat_rooms:
                chat_room_id = chat_room['id']
                doctor_id = chat_room["data"]["doctor_id"]
                doctor_info = myPyrebase.get_doctor_info(doctor_id)
                unread_count = myPyrebase.notify_unread_messages(chat_room_id)
                doctor_url = doctor_info.get('image_url')
                recent_message = RecentMessages(page, myPyrebase, doctor_url, chat_room_id, unread_count)
                recent_messages.append(recent_message)
    
    def build_doctorcards():
        doctor_cards.clear()
        online_doctors = myPyrebase.fetch_online_doctors()
        for doctor in online_doctors:
            doctor_id = doctor['doctor_id']
            image_url = doctor['image_url']
            name = doctor['name']
            speciality = doctor['speciality']
            online_status = doctor['is_online']
            doctor_card = DoctorCard(page,myPyrebase, doctor_id, name, speciality, image_url, online_status)
            doctor_cards.append(doctor_card)

    

    main_page_content = Column(
        scroll=True,
        height= BASE_HEIGHT,
        controls=[
            Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    Container(
                        on_click = lambda e:showMenu(e, second_page),
                        content=Image(src=f'{image_url}', width=35, height=35, border_radius=35)
                    ), 
                    ProfileName,
                    IconButton(bgcolor=colors.TRANSPARENT, icon_size=25, icon_color=TEXT_COLOR, icon=icons.NOTIFICATIONS)
                ]
            ),
            Container(height=10),
            Text('New Messages', color=TEXT_COLOR, font_family='Poppins Bold', size=17),
            Row(
                recent_messages,
                scroll=True, 
            ), 
            Container(height=15),
            Text('Get a Consultation', color=TEXT_COLOR, font_family='Poppins Bold', size=17), 
            Row(
                doctor_cards,
                spacing =5, 
                scroll=True, 
            ),
            Container(height=15),
            Text('Talk to Dokinta', color=TEXT_COLOR, font_family='Poppins Bold', size=17), 
            Container(
                padding= padding.only(top=15, left=15, right =15 , bottom=15), 
                bgcolor= MAIN_BACKGROUND_OPACITY,
                on_click= lambda _: page.go('/diagnosis'),
                border_radius= BORDER_RAD, 
                content=  Column(
                    horizontal_alignment= CrossAxisAlignment.CENTER,
                    controls = [
                        Container(
                                content= Column(
                                    controls=[
                                        Text('AI-Powered Diagnosis', color=TEXT_COLOR, size=19, font_family='Poppins Bold'),
                                        Text('Fast, accurate AI diagnoses for malaria and typhoid. Transforming healthcare effortlessly!', color=TEXT_COLOR, size=9, font_family='Poppins Regular'), 
                                    ]
                                )
                        ),
                        Row(
                            alignment = MainAxisAlignment.SPACE_BETWEEN, 
                            controls=[
                                Text(''),
                                Image(src ='https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/assets%2FChat%20bot-rafiki.png?alt=media&token=8f373db3-232b-464a-98e2-fb02ecbb69bb', height=200, width=200)
                            ]
                        ),
                    ]
                )
            ),
            Container(
                padding= padding.only(top=15, left=15, right =15 , bottom=15), 
                
                bgcolor= MAIN_BACKGROUND_OPACITY, 
                border_radius= BORDER_RAD, 
                content=  Column(
                    horizontal_alignment= CrossAxisAlignment.CENTER,
                    controls = [
                        Container(
                                content= Column(
                                    alignment = MainAxisAlignment.START,
                                    controls=[
                                        Text('AI-Powered Prescription', color=TEXT_COLOR, size=19, font_family='Poppins Bold'),
                                        Text('Fast, accurate AI prescription for malaria and typhoid. Transforming healthcare effortlessly!', color=TEXT_COLOR, size=9, font_family='Poppins Regular'), 
                                    ]
                                )
                        ),
                        Row(
                            alignment = MainAxisAlignment.SPACE_BETWEEN, 
                            controls=[
                                Text(''),
                                Image(src ='https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/assets%2FRemedy-rafiki.png?alt=media&token=d173976d-ff4d-4aec-a1fe-17ce77daecb6', height=200, width=200)
                            ]
                        ),
                    ]
                )
            )
            

        ]
    )

    main_page = Container(
        height= BASE_HEIGHT,
        bgcolor=SECONDARY_BACKGROUND, 
        border_radius=BORDER_RAD, 
        padding= padding.only(top=10, left=10, right=10, bottom=10),
        content= main_page_content


    )

    second_page_content = Column(
        horizontal_alignment= CrossAxisAlignment.CENTER, 
        controls = [
            Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    IconButton(bgcolor=colors.TRANSPARENT, icon_color=TEXT_COLOR, icon =icons.CLOSE, icon_size=TEXT_SIZE, on_click= lambda e:hideMenu(e, second_page)), 
                    Text('')
                ]   
            ),
            Stack(
               height= 150, 
               width=150,
               controls=[
                    Image(src=f'{image_url}', border_radius=75, height=150, width=150),
                    Container(
                                alignment = alignment.bottom_right,
                                content = CircleAvatar(bgcolor= SECONDARY_BACKGROUND, radius= 50, height=30, width=30, content= IconButton(icon=icons.CAMERA_ALT, icon_color=TEXT_COLOR, icon_size= 13, on_click= lambda _: file_picker.pick_files()))
                            ),
               ]
           ),
           Container(height=10), 
           Container(
               content= Row(
                   spacing = 5,
                   alignment = MainAxisAlignment.CENTER,
                   controls=[
                       Icon(icons.SETTINGS, color= TEXT_COLOR, size=25),
                       Text('Account', font_family='Poppins Regular', size=TEXT_SIZE, color=TEXT_COLOR)
                   ]
               )
           ),
           Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    Text('Recent Messages', font_family='Poppins Regular', size=TEXT_SIZE, color=TEXT_COLOR),
                    IconButton(bgcolor=colors.TRANSPARENT, icon_color=TEXT_COLOR, icon =icons.MESSAGE_OUTLINED, icon_size=TEXT_SIZE)
                ]   
            ),
             Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    Text('History', font_family='Poppins Regular', size=TEXT_SIZE, color=TEXT_COLOR),
                    IconButton(bgcolor=colors.TRANSPARENT, icon_color=TEXT_COLOR, icon =icons.MEDICAL_SERVICES, icon_size=TEXT_SIZE)
                ]   
            ),
            Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    Text('Security', font_family='Poppins Regular', size=TEXT_SIZE, color=TEXT_COLOR),
                    IconButton(bgcolor=colors.TRANSPARENT, icon_color=TEXT_COLOR, icon =icons.SHIELD, icon_size=TEXT_SIZE)
                ]   
            ),
            Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    Text('Help', font_family='Poppins Regular', size=TEXT_SIZE, color=TEXT_COLOR),
                    IconButton(bgcolor=colors.TRANSPARENT, icon_color=TEXT_COLOR, icon =icons.QUESTION_MARK, icon_size=TEXT_SIZE)
                ]   
            ),
             Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    Text('About', font_family='Poppins Regular', size=TEXT_SIZE, color=TEXT_COLOR),
                    IconButton(bgcolor=colors.TRANSPARENT, icon_color=TEXT_COLOR, icon =icons.INFO, icon_size=TEXT_SIZE)
                ]   
            ),
            Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    Text('Logout', font_family='Poppins Regular', size=TEXT_SIZE, color=TEXT_COLOR),
                    IconButton(bgcolor=colors.TRANSPARENT, icon_color=TEXT_COLOR, icon =icons.LOGOUT_OUTLINED, icon_size=TEXT_SIZE, on_click=handle_logout)
                ]   
            ),




        ]
    )
    second_page = Container(
        width= 0, 
        height=0,
        alignment= alignment.center, 
        bgcolor=MAIN_BACKGROUND, 
        
        padding= padding.only(top=10, left=10, right=10, bottom=10),
        content= second_page_content

    )

    home_page_content = Stack(
        [
            main_page, 
            second_page
        ]
    )

    home_page = Container(
        content= home_page_content
    )
    

    return {
        'view': home_page, 
        'load': on_page_load
    }