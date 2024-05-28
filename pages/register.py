from flet import * 

from utils import *
def RegisterPage(page: Page, myPyrebase = None):
    page.padding = 0
    page.adaptive = True
    

    page.fonts = {
        'Poppins Regular': '/fonts/poppins/Poppins-Regular.ttf',
        'Poppins Bold': '/fonts/poppins/Poppins-Bold.ttf'
    }

    def handle_sign_up(e):
        try:
            myPyrebase.register_user(name_input.value, username_input.value, email_input.value, password_input.value)
            name_input.value, username_input.value, email_input.value, password_input.value = '', '', '', ''
            page.go('/login')
        except:
            handle_sign_in_error()

    def handle_sign_in_error():
        page.snack_bar = SnackBar(
            content=Text("Something's wrong. Please Try Again.", color=colors.WHITE),
            bgcolor=colors.RED
        )
        page.snack_bar.open = True
        page.update()

    
    name_input = TextField(width=250, height= 50, bgcolor= TEXT_COLOR, text_size=TEXT_SIZE, border_color= TEXT_COLOR, color= MAIN_BACKGROUND)

    username_input = TextField(width=250, height= 50, bgcolor= TEXT_COLOR, text_size=TEXT_SIZE, border_color= TEXT_COLOR, color= MAIN_BACKGROUND)

    email_input = TextField(width=250, height= 50, bgcolor= TEXT_COLOR, text_size=TEXT_SIZE, border_color= TEXT_COLOR, color= MAIN_BACKGROUND)

    password_input = TextField(width=250, height= 50, bgcolor= TEXT_COLOR, text_size=TEXT_SIZE, border_color= TEXT_COLOR, color= SECONDARY_BACKGROUND, password= True)

    register_page_content = Column(
        alignment= MainAxisAlignment.CENTER,
        horizontal_alignment= CrossAxisAlignment.CENTER, 
        controls=[
            Row(
                alignment = MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    IconButton(icons.ARROW_BACK, icon_color= TEXT_COLOR, bgcolor= MAIN_BACKGROUND_OPACITY, icon_size=15, on_click= lambda _: page.go('/login'))
                ]
            ), 
            Column(
                controls=[
                  Container(
                        alignment= alignment.center, 
                        bgcolor= TEXT_COLOR, 
                        border_radius= BORDER_RAD, 
                        width= 270, 
                        height = 50,
                        padding= padding.only(left=10, right=10), 
                        content= Row(
                            spacing = 2,
                            
                            controls = [
                                Icon(icons.PERSON, color= SECONDARY_BACKGROUND, size= 15),
                                name_input
                            ]
                        )

                    ),
                    Container(
                        alignment= alignment.center, 
                        bgcolor= TEXT_COLOR, 
                        border_radius= BORDER_RAD, 
                        width= 270, 
                        height = 50,
                        padding= padding.only(left=10, right=10), 
                        content= Row(
                            spacing = 2,
                            
                            controls = [
                                Icon(icons.VERIFIED_USER, color= SECONDARY_BACKGROUND, size= 15),
                                username_input
                            ]
                        )

                    ),
                    Container(
                        alignment= alignment.center, 
                        bgcolor= TEXT_COLOR, 
                        border_radius= BORDER_RAD, 
                        width= 270, 
                        height = 50,
                        padding= padding.only(left=10, right=10), 
                        content= Row(
                            spacing = 2,
                            
                            controls = [
                                Icon(icons.EMAIL, color= SECONDARY_BACKGROUND, size= 15),
                                email_input
                            ]
                        )

                    ),
                    Container(
                        alignment= alignment.center, 
                        bgcolor= TEXT_COLOR, 
                        border_radius= BORDER_RAD, 
                        width= 270, 
                        height = 50,
                        padding= padding.only(left=10, right=10), 
                        content= Row(
                            spacing = 2,
                            
                            controls = [
                                Icon(icons.KEY, color= SECONDARY_BACKGROUND, size= 15),
                                password_input
                            ]
                        )

                    ),
                    ElevatedButton(bgcolor= SECONDARY_BACKGROUND, color= TEXT_COLOR, text='Register', width= 270, height= 50, on_click= handle_sign_up)  
                ]
            ),
            Row(
                alignment = MainAxisAlignment.CENTER,
                controls=[
                    Container(
                        height= 1, 
                        border_radius= BORDER_RAD, 
                        bgcolor= TEXT_COLOR, 
                        width= 100
                    ),
                    Text('OR', color= TEXT_COLOR, size= TEXT_SIZE, font_family= 'Poppins Regular'), 
                    Container(
                        height= 1, 
                        border_radius= BORDER_RAD, 
                        bgcolor= TEXT_COLOR, 
                        width= 100
                    )
                ]
            ),
            Row(
               alignment = MainAxisAlignment.CENTER,
               controls=[
                   Container(
                       alignment = alignment.center,
                       width= 50, 
                       height= 50, 
                       border_radius = 15,
                       bgcolor= SECONDARY_BACKGROUND, 
                       content = Image(src= 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/assets%2Fgoogle.png?alt=media&token=33618a5a-8417-4494-95b4-39bf1792cfd3', width= 55, height= 55)
                   ),
                   Container(
                       alignment = alignment.center,
                       width= 50, 
                       height= 50, 
                       border_radius = 15,
                       bgcolor= SECONDARY_BACKGROUND, 
                       content = Image(src= 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/assets%2Fgithub.png?alt=media&token=952afafe-10e4-4ca2-a7fb-d64edce270ce', width= 55, height= 55)
                   ),
                   Container(
                       alignment = alignment.center,
                       width= 50, 
                       height= 50, 
                       border_radius = 15,
                       bgcolor= SECONDARY_BACKGROUND, 
                       content = Image(src= 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/assets%2Fphone.png?alt=media&token=fcb4dff8-2ca5-4f5d-a26d-c6f21285f3bd', width= 55, height= 55)
                   )
               ]
            ),
            Container(height =9),
            Row(
                alignment = MainAxisAlignment.CENTER,
                controls =[
                    Text("Have an account already?", size= TEXT_SIZE, color= TEXT_COLOR, font_family='Poppins Regular'), 
                    Container(

                        content = Text("Login", size= TEXT_SIZE, color= MAIN_BACKGROUND, font_family='Poppins Regular'), 
                        on_click= lambda _: page.go('/login')
                    )
                ]
            )
        ]
    )
    
    register_content = Container(
         
        height=600,
        alignment= alignment.center, 
        bgcolor= MAIN_BACKGROUND_OPACITY, 
        border_radius= BORDER_RAD, 
        padding= padding.only(top=5, left=5, right=5, bottom=5), 
        content = register_page_content
    )

    register_page = Container(
                height= BASE_HEIGHT,
                alignment = alignment.center,
                bgcolor= SECONDARY_BACKGROUND,
                border_radius= BORDER_RAD, 
                 padding= padding.only(
            top=15, bottom=15, left=15, right = 15
        ),
                content= register_content
            )
  
    

    return {
        'view': register_page
    }