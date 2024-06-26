from flet import * 
from utils import *

def DiseasePage(page: Page, myPyrebase, disease_name):

    """
    Disease Page 
    """

    dokinta_image = Image(src = 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/assets%2Fdokinta.png?alt=media&token=3e8ed1bc-2499-467c-99b1-6b9278e747ab', width= page.width * 0.65, height= page.height * 0.65)

    image_url = Image(src = '', width= page.width * 0.65, height= page.height * 0.65)
    drug_name = Text(f'', color= TEXT_COLOR, size= TEXT_SIZE,font_family='Poppins Regular')
    dosage = Text(f'', color= TEXT_COLOR, size= TEXT_SIZE,font_family='Poppins Regular')

    def shrink(e, splash):
        splash.width = 0
        splash.height =0
        page.update()

    def on_page_load():
        if str(disease_name).lower() == 'malaria':
            image_url.src = 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/Mosquito%20bite-pana.png?alt=media&token=f5b2d88a-9f93-4eaf-8d1f-0c0b22fc5c1f'
            drug_name.value = 'Reommended Drug ' + 'Amatem Softgel x 6'
            dosage.value = 'Reommended Dosage ' + 'One soft gel in the morning, and one at night'
        elif str(disease_name).lower() == 'typhoid':
            image_url.src = 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/Stomachache-bro.png?alt=media&token=2a4da893-b8b2-43d3-9adb-b1a4925f0184'
            drug_name.value = 'Reommended Drug ' + 'Ciprotab 500 by 10 Softlets | Ciprofloxacin'
            dosage.value = 'Reommended Dosage ' + 'One tablet twice daily'
        else:
            image_url.src = 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/Sneezing-bro.png?alt=media&token=5d633bef-cec5-4a12-9be8-000dad15d34d'
            drug_name.value = 'Reommended Drug ' + 'Paracetamol'
            dosage.value = 'Reommended Dosage ' + '4 times daily'


    splash3 = Container(
        bgcolor= SECONDARY_BACKGROUND,
        padding= padding.only(
            top=15, bottom=15, left=15, right = 15
        ),
        content= Column(
            alignment= MainAxisAlignment.START, 
            horizontal_alignment= CrossAxisAlignment.CENTER, 
            controls=[
                Container(height= 10), 
                Container(height= 25),
                dokinta_image, 
                dosage, 
                FloatingActionButton(
                    width = 250,
                    on_click =lambda _: page.go('/home'),
                    content= Row(
                        alignment = MainAxisAlignment.CENTER,
                        controls=[
                            Icon(icons.ARROW_FORWARD, color= TEXT_COLOR, size=TEXT_SIZE), 
                            Text('Return Home', font_family='Poppins Regular', color= TEXT_COLOR, size= TEXT_SIZE)
                        ]
                    )
                )

            ]
    )
    )

    splash2= Container(
        bgcolor= SECONDARY_BACKGROUND,
        padding= padding.only(
            top=15, bottom=15, left=15, right = 15
        ),
        content= Column(
            alignment= MainAxisAlignment.START, 
            horizontal_alignment= CrossAxisAlignment.CENTER, 
            controls=[
                Container(height= 10),
                Container(height= 25),
                dokinta_image, 
                drug_name, 
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
    splash1 = Container(
        bgcolor= SECONDARY_BACKGROUND,
        padding= padding.only(
            top=15, bottom=15, left=15, right = 15
        ),
        content= Column(
            alignment= MainAxisAlignment.START, 
            horizontal_alignment= CrossAxisAlignment.CENTER, 
            controls=[
                Container(height= 10), 
                Container(height= 25),
                image_url, 
                Text(f'You may have {disease_name}', color= TEXT_COLOR, size= TEXT_SIZE,font_family='Poppins Regular'), 
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
    

        

    disease_page_content = Stack(
        [
            splash3,
            splash2, 
            splash1
        ]
    )

    disease_page = Container(
        height = page.height,
        content = disease_page_content,



    )




    return{
        'view': disease_page, 
        'load': on_page_load
    }