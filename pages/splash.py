from flet import * 

from utils import *

def SplashPage(page: Page, myPyrebase = None):

    page.padding = 0
    page.adaptive = True

    def on_load():
        if myPyrebase.check_token():
            page.go('/home')
    

    page.fonts = {
        'Poppins Regular': '/fonts/poppins/Poppins-Regular.ttf',
        'Poppins Bold': '/fonts/poppins/Poppins-Bold.ttf'
    }


    def shrink(e, splash):
        splash.width = 0
        splash.height =0
        page.update()

    
        

    splash1 = Container(
        border_radius= BORDER_RAD, 
        bgcolor= SECONDARY_BACKGROUND,
        alignment= alignment.center,
        padding= padding.only(
                top=15, bottom=15, left=15, right = 15
            ),
        content= Column(
            alignment= MainAxisAlignment.START, 
            horizontal_alignment= CrossAxisAlignment.CENTER, 
            controls=[
                Container(height= 10),
                Row(
                    alignment = MainAxisAlignment.SPACE_BETWEEN, 
                    controls= [
                        Container(
                            on_click = lambda _: page.go('/login'),
                            content= Text('skip', font_family= 'Poppins Regular', size= TEXT_SIZE, color=TEXT_COLOR)
                        ), 
                        Container(
                            content = Text('')
                        )
                    ]
                ), 
                Container(height= 25),
                Image(
                    src = 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/assets%2FOnline%20Doctor-rafiki.png?alt=media&token=02c3fde2-7e64-4046-a456-940fd72a0909', width= 350, height= 550
                ), 
                Text('Diagnosis at your finger tips', color= TEXT_COLOR, size= TEXT_SIZE,font_family='Poppins Regular'), 
                FloatingActionButton(
                    width = 250,
                    on_click =lambda e:shrink(e, splash1),
                    content= Row(
                        alignment = MainAxisAlignment.CENTER,
                        controls=[
                            Icon(icons.ARROW_FORWARD, color= TEXT_COLOR, size=TEXT_SIZE), 
                            Text('Next', font_family='Poppins Regular', color= TEXT_COLOR, size= TEXT_SIZE)
                        ]
                    )
                )

            ]
        )

    )
    splash2 = Container(
        
        border_radius= BORDER_RAD, 
        bgcolor= SECONDARY_BACKGROUND,
        padding= padding.only(
            top=15, bottom=15, left=15, right = 15
        ),
        content= Column(
            alignment= MainAxisAlignment.START, 
            horizontal_alignment= CrossAxisAlignment.CENTER, 
            controls=[
                Container(height= 10),
                Row(
                    alignment = MainAxisAlignment.SPACE_BETWEEN, 
                    controls= [
                        Container(
                            on_click = lambda _: page.go('/login'),
                            content= Text('skip', font_family= 'Poppins Regular', size= TEXT_SIZE, color=TEXT_COLOR)
                        ), 
                        Container(
                            content = Text('')
                        )
                    ]
                ), 
                Container(height= 25),
                Image(
                    src = 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/assets%2FChat%20bot-rafiki.png?alt=media&token=8f373db3-232b-464a-98e2-fb02ecbb69bb', width= 350, height= 550
                ), 
                Text('AI-Assisted Diagnosis and prescription', color= TEXT_COLOR, size= TEXT_SIZE,font_family='Poppins Regular'), 
                FloatingActionButton(
                    width = 250,
                    on_click =lambda e:shrink(e, splash2),
                    content= Row(
                        alignment = MainAxisAlignment.CENTER,
                        controls=[
                            Icon(icons.ARROW_FORWARD, color= TEXT_COLOR, size=TEXT_SIZE), 
                            Text('Next', font_family='Poppins Regular', color= TEXT_COLOR, size= TEXT_SIZE)
                        ]
                    )
                )

            ]
        )


    )
    splash3 = Container(
        
        border_radius= BORDER_RAD, 
        bgcolor= SECONDARY_BACKGROUND,
        padding= padding.only(
            top=15, bottom=15, left=15, right = 15
        ),
        content= Column(
            alignment= MainAxisAlignment.START, 
            horizontal_alignment= CrossAxisAlignment.CENTER, 
            controls=[
                Container(height= 10),
                Row(
                    alignment = MainAxisAlignment.SPACE_BETWEEN, 
                    controls= [
                        Container(
                            content= Text('skip', font_family= 'Poppins Regular', size= TEXT_SIZE, color=TEXT_COLOR),
                            on_click = lambda _: page.go('/login')
                        ), 
                        Container(
                            content = Text('')
                        )
                    ]
                ), 
                Container(height= 25),
                Image(
                    src = 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/assets%2FRemedy-rafiki.png?alt=media&token=d173976d-ff4d-4aec-a1fe-17ce77daecb6', width= 350, height= 550
                ), 
                Text('Real Time Consultations & Prescriptions', color= TEXT_COLOR, size= TEXT_SIZE,font_family='Poppins Regular'), 
                FloatingActionButton(
                    width = 250,
                    on_click =lambda _: page.go('/login'),
                    content= Row(
                        alignment = MainAxisAlignment.CENTER,
                        controls=[
                            Icon(icons.ARROW_FORWARD, color= TEXT_COLOR, size=TEXT_SIZE), 
                            Text('Login', font_family='Poppins Regular', color= TEXT_COLOR, size= TEXT_SIZE)
                        ]
                    )
                )

            ]
        )

    )

    splash_content = Stack(
        controls=[
            splash3,
            splash2,
            splash1, 
        ]
    )

    splash = Container(
                
                height= BASE_HEIGHT,
                content= splash_content
            )


    return {
        'view': splash, 
        'load': on_load
    }