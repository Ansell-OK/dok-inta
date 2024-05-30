from flet import * 
from utils import * 
from user_controls.doctor_user import DoctorConversation

def ChatroomPage(page: Page, myPyrebase, chat_room_id):


    def handle_convo_stream(message):
        try:
            build_conversation()
            page.update()
        except:
            pass
    
    def on_page_load():
        clean_notes()
        if myPyrebase.check_token() == "Success":
            myPyrebase.stream_data_conversation(chat_room_id, handle_convo_stream)
            build_conversation() 
            page.update()
        else:
            pass

    message_input = TextField('', text_align= TextAlign.LEFT, border_color= colors.TRANSPARENT, width= 240,  height=50, text_size=TEXT_SIZE, bgcolor= colors.TRANSPARENT, color= MAIN_BACKGROUND)
    messages = []

    def send_message(e):
        message = message_input.value
        if message:
            myPyrebase.send_message(chat_room_id, message, "patient")
            message_input.value = ""
            page.update()

    
    def build_conversation():
        messages.clear()
        data = myPyrebase.chatroom_messages(chat_room_id)
        if data:
            for key, value in data.items():
                user_message = value.get('message', '')
                sender_type = value.get('sender_type', '')
                conversation = DoctorConversation(page, myPyrebase, chat_room_id, user_message, sender_type)
                messages.append(conversation)
            message_input.value = ""
            page.update()
    
    def clean_notes():
        messages.clear()
        messages.append(Text(" "))
        page.update()


    chatroom_content = Column(
        controls=[
            Row(
              alignment= MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    IconButton(bgcolor= colors.TRANSPARENT, icon = icons.CHEVRON_LEFT_OUTLINED, icon_color= TEXT_COLOR, icon_size=TEXT_SIZE, on_click= lambda _: page.go('/home')), 
                    IconButton(bgcolor= colors.TRANSPARENT, icon = icons.MENU_SHARP, icon_color= TEXT_COLOR, icon_size=TEXT_SIZE)
                ]
            ),
            Column(
                messages,
                scroll=True, 
                height= 655,
            ), 
            Row(
                alignment = MainAxisAlignment.CENTER,
                controls=[
                    Container(
                        height= 50, 
                        border_radius=BORDER_RAD, 
                        bgcolor= TEXT_COLOR,
                        padding = padding.only(left=5, right=5),
                        content=Row(
                            controls=[
                                message_input
                            ]
                        )
                    ),
                    IconButton(icon= icons.SEND, bgcolor= MAIN_BACKGROUND,icon_color= TEXT_COLOR, icon_size= 20, on_click=send_message)
                ]
            )
        ]
    )

    chatroom_page = Container(
        height= BASE_HEIGHT,
        border_radius= BORDER_RAD, 
        bgcolor= SECONDARY_BACKGROUND,
        padding= padding.only( top=10, bottom=10, right=10, left=10),
        content = chatroom_content

    )


    return{
        'view': chatroom_page, 
        'load': on_page_load
    }