from flet import * 

BASE_WIDTH = 380
BASE_HEIGHT = 720
MAIN_BACKGROUND = '#0B1957'
MAIN_BACKGROUND_OPACITY = '#330B1957'
SECONDARY_BACKGROUND = '#9ECCFA'
SECONDARY_BACKGROUND_OPACITY = '#3b9eccfa'
LIGHT_SECONDARY = '#D1E8FF'
TEXT_COLOR = '#F8F3EA'
WHITE_OPACITY = '#33F8F3EA'
TITLE_SIZE = 25
TEXT_SIZE = 13
BORDER_RAD = 35

class RecentMessages(UserControl):
    def __init__(self, page, myPyrebase, doctor_url, chat_room_id, unread_count):
        super().__init__()
        self.page = page 
        self.myPyrebase = myPyrebase
        self.doctor_url = doctor_url
        self.chat_room_id = chat_room_id 
        self.unread_coumt = unread_count
        

    def navigate_to_room(self, e):
        self.myPyrebase.mark_messages_as_read(self.chat_room_id)
        self.page.go(f"/chatroom?chat_room_id={self.chat_room_id}")
    

    def build(self):
        return Stack(
                    height=75, 
                    width=75,
                    controls=[ 
                        Container(
                            height=75, 
                            width=75, 
                            bgcolor=TEXT_COLOR,
                            alignment = alignment.center,
                            border_radius=50, 
                            content= Container( 
                                on_click = self.navigate_to_room, content = Image(f'{self.doctor_url}', height=60, width=60, border_radius=50)),
                        ),
                        Container(
                            alignment= alignment.top_right, 
                            content = CircleAvatar(bgcolor= MAIN_BACKGROUND_OPACITY, radius= 15, height=20, width=20, content= Text(f'{self.unread_coumt}', font_family='Poppins Regular', size=12, color=TEXT_COLOR))
                        ),
                    ]
                )