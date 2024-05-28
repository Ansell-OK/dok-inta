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


class DoctorConversation(UserControl):
    def __init__(self, page, myPyrebase, chat_room_id, message ='Hello', user_type='patient'):
        super().__init__()
        self.page = page 
        self.message = message
        self.myPyrebase = myPyrebase
        self.chat_room_id = chat_room_id
        self.user_type = user_type
        self.conversation = Row(
                            alignment= MainAxisAlignment.END, 
                            controls=[ Container(
                                border_radius=15,
                                bgcolor=MAIN_BACKGROUND_OPACITY,
                                alignment=alignment.center_right,
                                padding=padding.only(top=5, left =5, right = 5, bottom=5),
                                content = Text(f'{message}',  size=TEXT_SIZE, color=TEXT_COLOR,
                                            font_family='Poppins Regular', weight=FontWeight.W_300))]
                        )
    
    def build(self):
        if self.user_type != 'patient':
            if len(self.message) >= 35:
                return Row(
            
                            alignment= MainAxisAlignment.START, 
                            controls= [Container(
                                    width= 250,
                                    border_radius=15,
                                    bgcolor=MAIN_BACKGROUND_OPACITY,
                                    alignment=alignment.center_right,
                                    padding=padding.only(top=5, left =5, right = 5, bottom=5),
                                    content = Text(f'{self.message}',  size=TEXT_SIZE, color=TEXT_COLOR,
                                                font_family='Poppins Regular', weight=FontWeight.W_300))]
                        )
            elif len(self.message) <= 35:
                return Row(
                            alignment= MainAxisAlignment.START, 
                            controls= [Container(
                                border_radius=15,
                                bgcolor=MAIN_BACKGROUND_OPACITY,
                                alignment=alignment.center_right,
                                padding=padding.only(top=5, left =5, right = 5, bottom=5),
                                content = Text(f'{self.message}',  size=TEXT_SIZE, color=TEXT_COLOR,
                                            font_family='Poppins Regular', weight=FontWeight.W_300))]
                        )
        elif self.user_type == 'patient':
            if len(self.message) >= 35:
                return Row(
                alignment= MainAxisAlignment.END, 
                controls= [Container(
                    width= 250,
                    border_radius=15,
                    bgcolor=MAIN_BACKGROUND_OPACITY,
                    alignment=alignment.center_right,
                    padding=padding.only(top=5, left =5, right = 5, bottom=5),
                    content = Text(f'{self.message}',  size=TEXT_SIZE, color=TEXT_COLOR,
                                font_family='Poppins Regular', weight=FontWeight.W_300))]
            )
            else:
                return self.conversation


if __name__ == '__main__':
    def main(page: Page):

        conversation = DoctorConversation(page)

        page.add(
            conversation
        )

    app(target=main)