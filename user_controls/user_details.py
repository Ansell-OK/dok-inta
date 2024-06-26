from flet import * 

MAIN_BACKGROUND = '#0B1957'
MAIN_BACKGROUND_OPACITY = '#330B1957'
SECONDARY_BACKGROUND = '#9ECCFA'
SECONDARY_BACKGROUND_OPACITY = '#3b9eccfa'
LIGHT_SECONDARY = '#D1E8FF'
TEXT_COLOR = '#F8F3EA'
WHITE_OPACITY = '#33F8F3EA'

class UserDetails(UserControl):
    def __init__(self, page, fullname='Ike-Okaofr Solumgolie', date_of_birth='20/2/05', gender='Male', phone_number= '09050798781', email='isolumgolie@gmail.com', image_url='https://insearchofmedia.com/wp-content/uploads/2021/01/mfdoom.jpeg?w=1000'): 
        super().__init__()
        self.page = page 
        self.fullname = fullname
        self.date_of_birth = date_of_birth
        self.gender = gender 
        self.phone = phone_number
        self.email = email 
        self.image_url = image_url


    def build(self):
        return Column(
            horizontal_alignment= CrossAxisAlignment.CENTER, 
            spacing = 10,
            height= self.page.height * 0.75,
            controls=[
                Container(
                    height=175, 
                    width=175, 
                    border_radius= 100, 
                    bgcolor= colors.WHITE, 
                    alignment= alignment.center, 
                    content= Image(f'{self.image_url}', height= 150, width= 150, border_radius= 100)
                ), 
                Container( 
                    width = self.page.width * 0.6,
                    alignment= alignment.center_left, 
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=5, left=5, right=5, bottom=5), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            Text(f'{self.fullname}', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular'), 
                            IconButton(icons.EDIT, bgcolor= colors.TRANSPARENT, icon_color= TEXT_COLOR, icon_size= 15)
                        ]
                    )
                ),
                Container( 
                    width = self.page.width * 0.6,
                    alignment= alignment.center_left, 
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=5, left=5, right=5, bottom=5), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            Text(f'{self.date_of_birth}', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular'), 
                            IconButton(icons.EDIT, bgcolor= colors.TRANSPARENT, icon_color= TEXT_COLOR, icon_size= 15)
                        ]
                    )
                ),
                Container( 
                    width = self.page.width * 0.6,
                    alignment= alignment.center_left, 
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=5, left=5, right=5, bottom=5), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            Text(f'{self.gender}', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular'), 
                            IconButton(icons.EDIT, bgcolor= colors.TRANSPARENT, icon_color= TEXT_COLOR, icon_size= 15)
                        ]
                    )
                ),
                Container( 
                    width = self.page.width * 0.6,
                    alignment= alignment.center_left, 
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=5, left=5, right=5, bottom=5), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            Text(f'{self.phone}', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular'), 
                            IconButton(icons.EDIT, bgcolor= colors.TRANSPARENT, icon_color= TEXT_COLOR, icon_size= 15)
                        ]
                    )
                ), 
                Container( 
                    width = self.page.width * 0.6,
                    alignment= alignment.center_left, 
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=5, left=5, right=5, bottom=5), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= [
                            Text(f'{self.email}', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular'), 
                            IconButton(icons.EDIT, bgcolor= colors.TRANSPARENT, icon_color= TEXT_COLOR, icon_size= 15)
                        ]
                    )
                )
            ]
        )

if __name__ == '__main__':
    def main(page: Page):

        page.padding = 0 
        page.adaptive = True

        userDetails = UserDetails(page)

        page.add(
            userDetails
        )

    app(target=main)