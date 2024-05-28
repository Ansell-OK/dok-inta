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

class Conversation(UserControl):
    def __init__(self, page, user_input ='Hello Golie, i am dokinta! how may i assist you today?', disease_prediction ='Common Cold', uuid='None', myPyrebase='None', dokinta_image_url='None', image_url='None',  max_30_width=250, ):
        super().__init__()
        self.page = page 
        self.disease_prediction = disease_prediction
        self.user_input = user_input
        self.myPyrebase = myPyrebase
        self.uuid = uuid
        self.max_30_width = max_30_width
        self.dokinta_image_url = dokinta_image_url
        self.image_url = image_url
        self.conversation = Column(
            controls= [
                Row(
                    alignment= MainAxisAlignment.END, 
                    controls=[
                        Column(
                            controls=[
                                Container(
                                    border_radius=15,
                                    bgcolor=MAIN_BACKGROUND_OPACITY,
                                    alignment=alignment.center_right,
                                    padding=padding.only(top=5, left =5, right = 5, bottom=5),
                                    content = Text(f'{user_input}',  size=TEXT_SIZE, color=TEXT_COLOR,
                                                font_family='Poppins Regular', weight=FontWeight.W_300)
                                )
                            ]
                        ),
                        CircleAvatar(foreground_image_src=f'{image_url}', width=45, height=45)
                    ]
                ),
                Row(
                    alignment= MainAxisAlignment.START, 
                    controls=[
                        CircleAvatar(foreground_image_src=f'{dokinta_image_url}', width=45, height=45),
                        Column(
                            controls=[
                                Container(
                                    border_radius=15,
                                    bgcolor=MAIN_BACKGROUND_OPACITY,
                                    alignment=alignment.center_right,
                                    padding=padding.only(top=5, left =5, right = 5, bottom=5),
                                    content = Text(f'Getting Diagnosis',  size=TEXT_SIZE, color=TEXT_COLOR,
                                                font_family='Poppins Regular', weight=FontWeight.W_300)
                                )
                            ]
                        )
                    ]
                ),
                Row(
                    alignment= MainAxisAlignment.START, 
                    controls=[
                        CircleAvatar(foreground_image_src=f'{dokinta_image_url}', width=45, height=45),
                        Column(
                            controls=[
                                Container(
                                    width = max_30_width,
                                    border_radius=15,
                                    bgcolor=MAIN_BACKGROUND_OPACITY,
                                    alignment=alignment.center_right,
                                    padding=padding.only(top=5, left =5, right = 5, bottom=5),
                                    content = Text(f'Seems you are down with a case of {disease_prediction}',  size=TEXT_SIZE, color=TEXT_COLOR,
                                                font_family='Poppins Regular', weight=FontWeight.W_300)
                                )
                            ]
                        )
                    ]
                ),
                Row(
                    alignment= MainAxisAlignment.CENTER, 
                    controls=[
                        FloatingActionButton(
                            width=150, 
                            content=Row(
                                alignment= MainAxisAlignment.CENTER, 
                                controls=[
                                    Icon(icons.ARROW_FORWARD, color= TEXT_COLOR, size=TEXT_SIZE), 
                                    Text('Talk to a Doctor', font_family='Poppins Regular', color= TEXT_COLOR, size= TEXT_SIZE)
                                ]
                            )
                        ),
                        FloatingActionButton(
                            width=150, 
                            content=Row(
                                alignment= MainAxisAlignment.CENTER, 
                                controls=[
                                    Icon(icons.ARROW_FORWARD, color= TEXT_COLOR, size=TEXT_SIZE), 
                                    Text('Get a prescription', font_family='Poppins Regular', color= TEXT_COLOR, size= TEXT_SIZE)
                                ]
                            )
                        )
                    ]
                ),

            ]
        )

    def build(self):
        if len(self.user_input) >= 35:
            return Column(
            controls= [
                Row(
                    alignment= MainAxisAlignment.END, 
                    controls=[
                        Column(
                            controls=[
                                Container(
                                    width = self.max_30_width,
                                    border_radius=15,
                                    bgcolor=MAIN_BACKGROUND_OPACITY,
                                    alignment=alignment.center_right,
                                    padding=padding.only(top=5, left =5, right = 5, bottom=5),
                                    content = Text(f'{self.user_input}',  size=TEXT_SIZE, color=TEXT_COLOR,
                                                font_family='Poppins Regular', weight=FontWeight.W_300)
                                )
                            ]
                        ),
                        CircleAvatar(foreground_image_src=f'{self.image_url}', width=45, height=45)
                    ]
                ),
                Row(
                    alignment= MainAxisAlignment.START, 
                    controls=[
                        CircleAvatar(foreground_image_src=f'{self.dokinta_image_url}', width=45, height=45),
                        Column(
                            controls=[
                                Container(
                                    border_radius=15,
                                    bgcolor=MAIN_BACKGROUND_OPACITY,
                                    alignment=alignment.center_right,
                                    padding=padding.only(top=5, left =5, right = 5, bottom=5),
                                    content = Text(f'Getting Diagnosis',  size=TEXT_SIZE, color=TEXT_COLOR,
                                                font_family='Poppins Regular', weight=FontWeight.W_300)
                                )
                            ]
                        )
                    ]
                ),
                Row(
                    alignment= MainAxisAlignment.START, 
                    controls=[
                        CircleAvatar(foreground_image_src=f'{self.dokinta_image_url}', width=45, height=45),
                        Column(
                            controls=[
                                Container(
                                    width = self.max_30_width,
                                    border_radius=15,
                                    bgcolor=MAIN_BACKGROUND_OPACITY,
                                    alignment=alignment.center_right,
                                    padding=padding.only(top=5, left =5, right = 5, bottom=5),
                                    content = Text(f'Seems you are down with a case of {self.disease_prediction}',  size=TEXT_SIZE, color=TEXT_COLOR,
                                                font_family='Poppins Regular', weight=FontWeight.W_300)
                                )
                            ]
                        )
                    ]
                ),
                Row(
                    alignment= MainAxisAlignment.CENTER, 
                    controls=[
                        FloatingActionButton(
                            width=150, 
                            content=Row(
                                alignment= MainAxisAlignment.CENTER, 
                                controls=[
                                    Icon(icons.ARROW_FORWARD, color= TEXT_COLOR, size=TEXT_SIZE), 
                                    Text('Talk to a Doctor', font_family='Poppins Regular', color= TEXT_COLOR, size= TEXT_SIZE)
                                ]
                            )
                        ),
                        FloatingActionButton(
                            width=150, 
                            content=Row(
                                alignment= MainAxisAlignment.CENTER, 
                                controls=[
                                    Icon(icons.ARROW_FORWARD, color= TEXT_COLOR, size=TEXT_SIZE), 
                                    Text('Get a prescription', font_family='Poppins Regular', color= TEXT_COLOR, size= TEXT_SIZE)
                                ]
                            )
                        )
                    ]
                ),

            ]
        )

        else:
            return self.conversation


if __name__ == '__main__':
    def main(page: Page):

        conversation = Conversation(page)

        page.add(
            conversation
        )

    app(target=main)