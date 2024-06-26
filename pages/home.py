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

    image = Image(src='', width=35, height=35, border_radius=35)
    big_image = Image(src='', border_radius=75, height=150, width=150)
    
    def handle_logout(*e):
        ProfileName.value = ""
        myPyrebase.kill_streams()
        myPyrebase.sign_out()
        page.go("/register")

    

    def on_page_load():
        ProfileName.value = "Welcome back"
        image.src = ''
        big_image.src = ''
        if myPyrebase.check_token() == "Success":
            handle = myPyrebase.get_username()
            build_recent()
            build_doctorcards()
            image_url = check_none()
            if handle:
                ProfileName.value = "Welcome Back, " +  handle
                image.src = image_url
                big_image.src  = image_url
            page.update()

    

    def showMenu(e, screen):
        screen.height = page.height
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
                if unread_count > 0:
                    doctor_url = doctor_info.get('image_url')
                    recent_message = RecentMessages(page, myPyrebase, doctor_url, chat_room_id, unread_count)
                    recent_messages.append(recent_message)
                else: 
                    pass
        else: 
            pass
    
    def build_doctorcards():
        doctor_cards.clear()
        online_doctors = myPyrebase.fetch_online_doctors()
        if online_doctors:
            for doctor in online_doctors:
                doctor_id = doctor['doctor_id']
                image_url = doctor['image_url']
                name = doctor['name']
                speciality = doctor['speciality']
                online_status = doctor['is_online']
                doctor_card = DoctorCard(page,myPyrebase, doctor_id, name, speciality, image_url, online_status)
                doctor_cards.append(doctor_card)
        else:
            pass

    

    main_page_content = Column(
        scroll=ScrollMode.HIDDEN,
        height= page.height,
        controls=[
            Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    Container(
                        on_click = lambda e:showMenu(e, second_page),
                        content=image
                    ), 
                    ProfileName,
                    Text('')
                ]
            ),
            Container(height=10),
            Row(
                recent_messages,
                scroll=ScrollMode.HIDDEN, 
            ), 
            Container(height=15),
            Text('Get a Consultation', color=TEXT_COLOR, font_family='Poppins Bold', size=17), 
            Row(
                doctor_cards,
                spacing =5, 
                scroll=ScrollMode.HIDDEN, 
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
           
        ]
    )

    main_page = Container(
        height= page.height,
        bgcolor=SECONDARY_BACKGROUND, 
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
                       IconButton(icons.SETTINGS, icon_color= TEXT_COLOR, icon_size=25, bgcolor= colors.TRANSPARENT, on_click= lambda _: page.go('/user_details')),
                       Text('Account', font_family='Poppins Regular', size=TEXT_SIZE, color=TEXT_COLOR)
                   ]
               )
           ),
             Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    Text('History', font_family='Poppins Regular', size=TEXT_SIZE, color=TEXT_COLOR),
                    IconButton(bgcolor=colors.TRANSPARENT, icon_color=TEXT_COLOR, icon =icons.MEDICAL_SERVICES, icon_size=TEXT_SIZE, on_click= lambda _: page.go('/medical_info'))
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