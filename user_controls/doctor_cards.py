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

class DoctorCard(UserControl):
    def __init__(self, page, myPyrebase, doctor_id, name, speciality, image_url, online_status = True):
        super().__init__()
        self.page = page
        self.myPyrebase = myPyrebase 
        self.doctor_id = doctor_id
        self.name = name
        self.speciality = speciality
        self.image_url = image_url
        self.online_status = online_status
    
                            
    def navigate_to_chatroom(self, e):
        chat_room_id = self.myPyrebase.create_chat_room(self.doctor_id)
        self.myPyrebase.mark_messages_as_read(chat_room_id)
        chatroom_url = f"/chatroom?chat_room_id={chat_room_id}&doctor_id={self.doctor_id}"
        self.page.go(chatroom_url)
    
    def build(self):
        return Container(
                    width = 200,
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding = padding.only(top =15, left= 15, right=15, bottom =15),
                    border_radius= BORDER_RAD, 
                    content= Column(
                        horizontal_alignment= CrossAxisAlignment.CENTER, 
                        controls=[
                            Stack(
                                height=75, 
                                width=75,
                                controls=[ 
                                    Container(
                                        height=75, 
                                        width=75, 
                                        bgcolor=TEXT_COLOR,
                                        alignment = alignment.center,
                                        border_radius=50, 
                                        content= Container( content = Image(f'{self.image_url}', height=60, width=60, border_radius=50)),
                                    ),
                                    Container(
                                        alignment= alignment.top_right, 
                                        content = CircleAvatar(bgcolor= MAIN_BACKGROUND_OPACITY, radius= 15, height=20, width=20)
                                    ),
                                ]
                            ), 
                            Text(f'{self.name}', color=TEXT_COLOR, size=TEXT_SIZE, font_family='Poppins Regular'),
                            Text(f'{self.speciality}', color=TEXT_COLOR, size=TEXT_SIZE, font_family='Poppins Regular'), 
                            Container(height=15),
                            Row(
                                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                                controls=[
                                    Text('online' if self.online_status else 'offline', color=TEXT_COLOR, size=TEXT_SIZE, font_family='Poppins Regular'),
                                    IconButton(icon_color=TEXT_COLOR, icon_size=TEXT_SIZE, bgcolor=colors.TRANSPARENT, icon=icons.MESSAGE, on_click=self.navigate_to_chatroom)
                                ]
                            )
                        ]
                    )
                )

if __name__ == '__main__':
    def main(page: Page):
        page.window_width = BASE_WIDTH
        page.window_height = BASE_HEIGHT


        row_of_row = DoctorCard(page)

        page.add(row_of_row)

    app(target=main)