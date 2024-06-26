from flet import * 
from utils import * 


def medical_information(page:Page, myPyrebase):

    def slider_changed(e):
        t.value = f"Weight changed to {e.control.value}"
        page.update()

    t = Text(font_family='Poppins Regular', size=TEXT_SIZE, color=TEXT_COLOR)

    weight = Slider(min=1, max=150, label= '{value}kg', secondary_active_color= MAIN_BACKGROUND, on_change= slider_changed)

    blood_group =Dropdown(
                    
                    width= page.height * 0.4,
                    options=[
                        dropdown.Option("O-"),
                        dropdown.Option("O+"),
                        dropdown.Option("A+"),
                        dropdown.Option("A-"),
                        dropdown.Option("B+"),
                        dropdown.Option("B-"),
                        dropdown.Option("AB+"),
                        dropdown.Option("AB-"),
                    ]
                )
    genotype = Dropdown(
                    width = page.height * 0.4, 
                    options = [
                    dropdown.Option('AA'), 
                    dropdown.Option('AS'), 
                    dropdown.Option('SS'), 
                    dropdown.Option('AC') 
                    ]
                )
    previous_ailments =TextField('',border_color= colors.BLACK, bgcolor= colors.TRANSPARENT, text_align= TextAlign.LEFT, text_size= 10, color=colors.BLACK, height= 75)

    def on_page_load():
        if myPyrebase.check_token() == "Success":
            build_info()
            page.update()
    
    def details_update(e):
        myPyrebase.add_medical_info(weight.value, blood_group.value, genotype.value, previous_ailments.value)
        page.update()
           
    def build_info():
        data = myPyrebase.get_medical_info()
        print(data)
        if data: 
            medical_data = data.get('medical_info', {})
            print(medical_data)
            if medical_data:
                weight.value = medical_data['weight']
                blood_group.value = medical_data['blood_group']
                genotype.value = medical_data['genotype']
                previous_ailments.value = medical_data['previous_ailments']
            page.update()



    medical_info_content = Column(
        [
            Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    IconButton(bgcolor=colors.TRANSPARENT, icon_color=TEXT_COLOR, icon =icons.CLOSE, icon_size=TEXT_SIZE, on_click = lambda _: page.go('/home')), 
                    Text('')
                ]   
            ),
            Container(height = 15), 
            Column(
                [
                    weight, 
                    t
                ]
            ), 
            Container(height = 15), 
            blood_group,
            Container(height = 15), 
            genotype,
            Container(height = 15), 
            previous_ailments,  
            Row(
            [
            FloatingActionButton(width = page.width * 0.8,on_click= lambda e:details_update(e),content=
                                Row(alignment= MainAxisAlignment.CENTER,
                                controls=  [
                                        Icon(icons.CHECK, color= colors.WHITE),
                                        Text('Accept Changes')
                                    ]
                                ))
            ],
            alignment= MainAxisAlignment.CENTER
        )
        ], 
        horizontal_alignment= CrossAxisAlignment.CENTER, 
    )

    


    medical_info_page = Container(
        alignment= alignment.center,
        height= page.height, 
        width = page.width, 
        bgcolor= SECONDARY_BACKGROUND,
        padding = padding.only(top=15, right = 15, left = 15, bottom = 15), 
        content = medical_info_content
    )





    return {
        'view': medical_info_page, 
        'load': on_page_load
    }