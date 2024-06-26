from flet import * 
from utils import * 

def DoctorPage(page:Page, myPyrebase, doctor_id):

    image = Image('', width= 150, height=150, border_radius=100)
    name = Text('', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular')
    speciality = Text('', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular')
    phonenumber = Text('', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular')
    hospital = Text('', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular')
    email = Text('', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular')

    def on_page_load():
        image.src = ''
        name.value = ''
        speciality.value = ''
        phonenumber.value = ''
        hospital.value  = ''
        email.value = ''
        doctor_details = myPyrebase.get_doctor_info(doctor_id)
        if doctor_details:
            name.value = doctor_details['name']
            email.value = doctor_details['email']
            image.src = doctor_details['image_url']
            speciality.value = doctor_details['speaciality']
            phonenumber.value = doctor_details['phone']
            hospital.value = doctor_details['hospital']
            page.update()

    doctor_det_content = Column(
        [
           Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    IconButton(bgcolor=colors.TRANSPARENT, icon_color=TEXT_COLOR, icon =icons.CLOSE, icon_size=TEXT_SIZE, on_click= lambda _: page.go('/home')), 
                    Text('')
                ]   
            ),
            Container(
                    height=175, 
                    width=175, 
                    border_radius= 100, 
                    bgcolor= colors.WHITE, 
                    alignment= alignment.center, 
                    content= image
            ),
            Container( 
                    width = page.window_width * 0.8,
                    alignment= alignment.center_left, 
                    border_radius= 10,
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=10, left=10, right=10, bottom=10), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            Text('Name:', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular'),
                            name
                        ]
                    )
            ),
            Container( 
                    width = page.window_width * 0.8,
                    alignment= alignment.center_left, 
                    border_radius= 10,
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=10, left=10, right=10, bottom=10), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            Text('Speciality:', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular'),
                            speciality
                        ]
                    )
            ),
            Container( 
                    width = page.window_width * 0.8,
                    alignment= alignment.center_left, 
                    border_radius= 10,
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=10, left=10, right=10, bottom=10), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            Text('Phone Number', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular'),
                            phonenumber
                        ]
                    )
            ), 
            Container( 
                    width = page.window_width * 0.8,
                    alignment= alignment.center_left, 
                    border_radius= 10,
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=10, left=10, right=10, bottom=10), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            Text('Hospital', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular'),
                            hospital
                        ]
                    )
            ), 
            Container( 
                    width = page.window_width * 0.8,
                    alignment= alignment.center_left, 
                    border_radius= 10,
                    bgcolor= MAIN_BACKGROUND_OPACITY, 
                    padding= padding.only(top=10, left=10, right=10, bottom=10), 
                    content = Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls= 
                        [
                            Text('Email:', color= TEXT_COLOR, size= 15, font_family= 'Poppins Regular'),
                            email
                        ]
                    )
            ), 

        ], 
        horizontal_alignment= CrossAxisAlignment.CENTER

    )

    doctor_det = Container(
        height = page.window_height,
        bgcolor= SECONDARY_BACKGROUND,
        border_radius= BORDER_RAD, 
        padding= padding.only(
                top=15, bottom=15, left=15, right = 15
            ),
        content = doctor_det_content 
    )


    return {
        'view': doctor_det, 
        'load': on_page_load
    }