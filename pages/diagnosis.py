from flet import * 
from utils import * 
from user_controls.conversation import Conversation
import requests

def DiagnosisPage(page: Page, myPyrebase):

    ProfileName = Text('Hello', size=TEXT_SIZE, color= TEXT_COLOR, font_family= 'Poppins Regular', weight= FontWeight.W_300)

    url = "https://rnn-model-fasapi.onrender.com/predict"

    
    def handle_convo_stream(message):
        try:
            build_conversation()
            page.upload()
        except:
            pass

   
    
    def on_page_load():
        clean_notes()
        ProfileName.value = "Hello"
        if myPyrebase.check_token() == "Success":
            myPyrebase.stream_data_conversation_main(handle_convo_stream)
            handle = myPyrebase.get_username()
            if handle:
                ProfileName.value = "Hello " + handle + ' how may i be of assistance today?'
            page.update()

    def check_none():
        image_url = myPyrebase.get_image_url()
        if image_url is None:
            return 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/Male%20patient%20icon.jpeg?alt=media&token=89ba85f5-a990-473e-b763-44437237cb48'
        else:
            return image_url
    
    image_url = check_none() 

    def handle_add(e):
        data = {"text": message_input.value}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            prediction = response.json().get('Disease')
            myPyrebase.add_conversation(message_input.value, prediction)

        message_input.value = ""
        page.update()
    
    message_input = TextField('', text_align= TextAlign.LEFT, border_color= colors.TRANSPARENT, width= 240,  height=50, text_size=TEXT_SIZE, bgcolor= colors.TRANSPARENT, color= MAIN_BACKGROUND)

    conversations = []

    
    dokinta_image_url = 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/assets%2Fdokinta.png?alt=media&token=3e8ed1bc-2499-467c-99b1-6b9278e747ab'
    
    
    def build_conversation():
        conversations.clear()
        data = myPyrebase.get_conversation()
        if data:
            conversation_data = data.get('conversations', {}) 
            for key, value in conversation_data.items():
                user_message = value.get('user_message', '')
                prediction = value.get('prediction', '')
                conversation = Conversation(page, user_message, prediction, key, myPyrebase, dokinta_image_url, image_url)
                conversations.append(conversation)
            message_input.value = ""
            page.update()
        
    
    def clean_notes():
        conversations.clear()
        conversations.append(Text(" "))
        page.update()




    
    

    chat_page_content = Column(
        controls=[
            Row(
              alignment= MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    IconButton(bgcolor= colors.TRANSPARENT, icon = icons.CHEVRON_LEFT_OUTLINED, icon_color= TEXT_COLOR, icon_size=TEXT_SIZE, on_click= lambda _: page.go('/home')), 
                    IconButton(bgcolor= colors.TRANSPARENT, icon = icons.MENU_SHARP, icon_color= TEXT_COLOR, icon_size=TEXT_SIZE)
                ]
            ),
            Row(
                alignment= MainAxisAlignment.START, 
                controls=[
                    CircleAvatar(foreground_image_src=f'{dokinta_image_url}', width=45, height=45),
                    Column(
                        controls=[
                            Container(
                                width = 250,
                                border_radius=15,
                                bgcolor=MAIN_BACKGROUND_OPACITY,
                                alignment=alignment.center_right,
                                padding=padding.only(top=5, left =5, right = 5, bottom=5),
                                content = Text(f'Hello , i am dokinta! how may i assist you today?',  size=TEXT_SIZE, color=TEXT_COLOR,
                                            font_family='Poppins Regular', weight=FontWeight.W_300)
                            )
                        ]
                    )
                ]
            ),
            Column(
                conversations,
                scroll=True, 
                height= 610,
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
                    IconButton(icon= icons.SEND, bgcolor= MAIN_BACKGROUND,icon_color= TEXT_COLOR, icon_size= 20, on_click=handle_add)
                ]
            )

        ]
    )

    chat_page = Container(
        height= BASE_HEIGHT,
        border_radius= BORDER_RAD, 
        bgcolor= SECONDARY_BACKGROUND,
        padding= padding.only( top=10, bottom=10, right=10, left=10),
        content= chat_page_content 

    )

   

    diagnosis_page_content = Stack(
        controls=[
            chat_page
        ]
    )



    diagnosis_page = Container(
            content= diagnosis_page_content
    )

    return {
        'view': diagnosis_page,
        'load': on_page_load
    }