from flet import *
from utils import * 
import datetime

def UserDetails(page: Page, myPyrebase):

    def change_date(e):
        return date_picker.value
    


    date_picker = DatePicker(
        on_change=change_date,
        first_date=datetime.date(1900, 1, 1),
        last_date=datetime.date(2024, 12, 31),
    )
    page.overlay.append(date_picker)

    fullname = Text('', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular')
    image = Image('', height= 150, width= 150, border_radius= 100)
    gender = Text('', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular')
    date_of_birth = Text('', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular')
    phone_number = Text('', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular')
    email = Text('', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular')

    fullname_input = TextField('', border_color= colors.TRANSPARENT, bgcolor= colors.TRANSPARENT, text_align= TextAlign.LEFT, text_size= 11, color=colors.BLACK, height= 50)
    gender_input = TextField('', border_color= colors.TRANSPARENT, bgcolor= colors.TRANSPARENT, text_align= TextAlign.LEFT, text_size= 11, color=colors.BLACK, height= 50)
    phone_number_input = TextField('', border_color= colors.TRANSPARENT, bgcolor= colors.TRANSPARENT, text_align= TextAlign.LEFT, text_size= 11, color=colors.BLACK, height= 50)
    email_input = TextField('', border_color= colors.TRANSPARENT, bgcolor= colors.TRANSPARENT, text_align= TextAlign.LEFT, text_size= 11, color=colors.BLACK, height= 50)

    page.padding = 0 
    page.adaptive = True

    def handle_add(e, screen):
        if myPyrebase.check_token() == "Success":
            myPyrebase.add_info(fullname_input.value, email_input.value, str(date_picker.value), gender_input.value, phone_number_input.value)
            screen.width = 0 
            screen.height = 0
        page.update()

    def start_edit(e, screen):
        screen.width = page.width
        screen.height = page.height
        page.update()
    
    def close_edit(e, screen):
        screen.width = 0
        screen.height = 0
        page.update()

    def on_page_load():
        fullname.value = ''
        image.src = ''
        gender.value = ''
        date_of_birth.value = ''
        phone_number.value = ''
        email.value = ''
        if myPyrebase.check_token() == "Success":
            user_info = myPyrebase.get_user_info()
            if user_info:
                fullname.value = user_info['name']
                fullname_input.value = user_info['name']
                image.src = user_info['image_url']
                gender.value = user_info['gender']
                gender_input.value = user_info['gender']
                date_of_birth.value = user_info['DOB'][:10]
                phone_number.value = user_info['phone_number']
                phone_number_input.value = user_info['phone_number']
                email.value = user_info['email']
                email_input.value = user_info['email']
                page.update()
            else: 
                pass
    
    user_details_edit_content = Column(
        horizontal_alignment= CrossAxisAlignment.CENTER,
        controls=[
            Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    IconButton(bgcolor=colors.TRANSPARENT, icon_color=TEXT_COLOR, icon =icons.CLOSE, icon_size=TEXT_SIZE, on_click= lambda e:close_edit(e, page_2)), 
                    Text('')
                ]   
            ),
            Stack(
               height= 150, 
               width=  150,
               controls=[
                   image,
                    Container(
                                alignment = alignment.bottom_right,
                                content = CircleAvatar(bgcolor= SECONDARY_BACKGROUND, radius= 50, height=30, width=30, content= IconButton(icon=icons.CAMERA_ALT, icon_color=TEXT_COLOR, icon_size= 13))
                            ),
               ]
           ),
           Container(height = 5),
           Container( 
                width = page.width * 0.8,
                height = 50,
                alignment= alignment.center_left, 
                border_radius= 10,
                bgcolor= TEXT_COLOR, 
                padding= padding.only(top=5, left=5, right=5, bottom=5), 
                content = Row(
                    alignment = MainAxisAlignment.SPACE_BETWEEN,
                    controls= 
                    [
                        fullname_input
                    ]
                )
            ),
            Container(height = 5),
            FloatingActionButton(
                width = page.width * 0.4,
                text="Pick date",
                icon=icons.CALENDAR_MONTH,
                on_click=lambda _: date_picker.pick_date(),
            ),
            Container(height = 5),
            Container( 
                width = page.width * 0.8,
                height = 50,
                alignment= alignment.center_left, 
                border_radius= 10,
                bgcolor= TEXT_COLOR, 
                padding= padding.only(top=5, left=5, right=5, bottom=5), 
                content = Row(
                    alignment = MainAxisAlignment.SPACE_BETWEEN,
                    controls= 
                    [
                        gender_input
                    ]
                )
            ),
            Container(height = 5),
            Container( 
                width = page.width * 0.8,
                height = 50,
                alignment= alignment.center_left, 
                border_radius= 10,
                bgcolor= TEXT_COLOR, 
                padding= padding.only(top=5, left=5, right=5, bottom=5), 
                content = Row(
                    alignment = MainAxisAlignment.SPACE_BETWEEN,
                    controls= 
                    [
                        phone_number_input
                    ]
                )
            ),
            Container(height = 5),
            Container( 
                width = page.width * 0.8,
                height = 50,
                alignment= alignment.center_left, 
                border_radius= 10,
                bgcolor= TEXT_COLOR, 
                padding= padding.only(top=5, left=5, right=5, bottom=5), 
                content = Row(
                    alignment = MainAxisAlignment.SPACE_BETWEEN,
                    controls= 
                    [
                       email_input
                    ]
                )
            ),
            Container(height = 5),
            Row(
                alignment= MainAxisAlignment.CENTER, 
                controls=[
                    FloatingActionButton(width = page.width * 0.4,on_click= lambda e:handle_add(e, page_2),content=
                                         Row(alignment= MainAxisAlignment.CENTER,
                                            controls=  [
                                                 Icon(icons.CHECK, color= TEXT_COLOR),
                                                 Text('Accept Changes')
                                             ]
                                         )),
                    FloatingActionButton(width = page.width * 0.4,  on_click= lambda e:close_edit(e, page_2),content=
                                         Row(
                                            alignment= MainAxisAlignment.CENTER,
                                             controls = [
                                                 Icon(icons.DELETE, color= TEXT_COLOR),
                                                 Text('Discard Changes')
                                             ]
                                         )),
                ]
            )

        ]


    )


    page_2 = Container(
            height = 0,
            width= 0,
            bgcolor= SECONDARY_BACKGROUND, 
            padding = padding.only(top=15, left=15, right =15, bottom=15),
            content = user_details_edit_content
    )

    user_details_content = Column(
        horizontal_alignment= CrossAxisAlignment.CENTER,
        controls=[
            Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    IconButton(bgcolor=colors.TRANSPARENT, icon_color=TEXT_COLOR, icon =icons.CLOSE, icon_size=TEXT_SIZE, on_click = lambda _: page.go('/home')), 
                    Text('')
                ]   
            ),
            Container(height=30),
            Container(
                    height=175, 
                    width=175, 
                    border_radius= 100, 
                    bgcolor= colors.WHITE, 
                    alignment= alignment.center, 
                    content= image
                ), 
                Container( 
                    width = page.width * 0.8,
                    alignment= alignment.center_left, 
                    border_radius= 10,
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=10, left=10, right=10, bottom=10), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            fullname,
                            IconButton(icons.EDIT, bgcolor= colors.TRANSPARENT, icon_color= TEXT_COLOR, icon_size= 15, on_click= lambda e:start_edit(e, page_2))
                        ]
                    )
                ),
                Container( 
                    width = page.width * 0.8,
                    alignment= alignment.center_left, 
                    border_radius= 10,
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=10, left=10, right=10, bottom=10), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            date_of_birth, 
                            IconButton(icons.EDIT, bgcolor= colors.TRANSPARENT, icon_color= TEXT_COLOR, icon_size= 15, on_click= lambda e:start_edit(e, page_2))
                        ]
                    )
                ),
                Container( 
                    width = page.width * 0.8,
                    alignment= alignment.center_left, 
                    border_radius= 10,
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=10, left=10, right=10, bottom=10), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            gender, 
                            IconButton(icons.EDIT, bgcolor= colors.TRANSPARENT, icon_color= TEXT_COLOR, icon_size= 15, on_click= lambda e:start_edit(e, page_2))
                        ]
                    )
                ),
                Container( 
                    width = page.width * 0.8,
                    border_radius= 10,
                    alignment= alignment.center_left, 
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=10, left=10, right=10, bottom=10), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            phone_number, 
                            IconButton(icons.EDIT, bgcolor= colors.TRANSPARENT, icon_color= TEXT_COLOR, icon_size= 15, on_click= lambda e:start_edit(e, page_2))
                        ]
                    )
                ), 
                Container( 
                    width = page.width * 0.8,
                    border_radius= 10,
                    alignment= alignment.center_left, 
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=10, left=10, right=10, bottom=10), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= [
                            email, 
                            IconButton(icons.EDIT, bgcolor= colors.TRANSPARENT, icon_color= TEXT_COLOR, icon_size= 15, on_click= lambda e:start_edit(e, page_2))
                        ]
                    )
                )
        ]
    )


    page_1 = Container(
        height = page.height, 
        bgcolor= SECONDARY_BACKGROUND, 
        padding = padding.only(top=15, left=15, right =15, bottom=15),
        content = user_details_content

    )

    user_details = Stack(
        [
            page_1, 
            page_2
        ]
    )

    return {
        'view': user_details, 
        'load': on_page_load
    }