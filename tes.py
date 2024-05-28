
from flet import * 
from utils import * 

# import requests

# # URL of your FastAPI endpoint hosted on Vercel
# url = "https://rnn-model-fasapi.onrender.com/predict"

# # Take user input
# user_input = input("Enter your symptoms: ")

# # JSON data to send to the endpoint
# data = {
#     "text": user_input
# }

# # Send POST request to the endpoint
# response = requests.post(url, json=data)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     prediction = response.json().get('Disease')
#     print("Prediction:", prediction)
# else:
#     print("Error:", response.text)

def main(page:Page):

    page.window_width = BASE_WIDTH
    page.window_height = BASE_HEIGHT
    page.padding = 0
    page.fonts = {
        'Poppins Regular': '/fonts/poppins/Poppins-Regular.ttf',
        'Poppins Bold': '/fonts/poppins/Poppins-Bold.ttf'
    }

    online_doctors = [{'doctor_id': 'kXPsqCEot3blDGp2IVAva7Ps4ij2', 'name': 'Smith Row', 'speciality': 'Medical Doctor', 'image_url': 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/download%20(1).jpeg?alt=media&token=7ec5832a-79fb-4381-b8f3-2d18d88708cb', 'is_online': False}, {'doctor_id': 'ruUa2Irl6jg3vUBGZSrRrpdqUFn1', 'name': 'Solumgolie Ike-Okafor', 'speciality': 'Medical Doctor', 'image_url': 'https://firebasestorage.googleapis.com/v0/b/dokinta-57cf8.appspot.com/o/download%20(1).jpeg?alt=media&token=7ec5832a-79fb-4381-b8f3-2d18d88708cb', 'is_online': True}]


    row_of_row = Row(
        scroll = True,
        controls=[

        ]
    )

    def print_doc_id(e, doctor_id):
        print(doctor_id)

    for doctor in online_doctors:
        doctor_id = doctor['doctor_id']
        print(doctor_id)
        image_url = doctor['image_url']
        name = doctor['name']
        speciality = doctor['speciality']
        row_of_row.controls.append(
            Container(
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
                                content= Container( content = Image(f'{image_url}', height=60, width=60, border_radius=50)),
                            ),
                            Container(
                                alignment= alignment.top_right, 
                                content = CircleAvatar(bgcolor= MAIN_BACKGROUND_OPACITY, radius= 15, height=20, width=20)
                            ),
                        ]
                    ), 
                    Text(f'{name}', color=TEXT_COLOR, size=TEXT_SIZE, font_family='Poppins Regular'),
                    Text(f'{speciality}', color=TEXT_COLOR, size=TEXT_SIZE, font_family='Poppins Regular'), 
                    Container(height=15),
                    Row(
                        alignment= MainAxisAlignment.SPACE_BETWEEN, 
                        controls=[
                            Text('online', color=TEXT_COLOR, size=TEXT_SIZE, font_family='Poppins Regular'), 
                            IconButton(icon_color=TEXT_COLOR, icon_size=TEXT_SIZE, bgcolor= colors.TRANSPARENT, icon= icons.MESSAGE, on_click= lambda e, doctor_id=doctor_id: print_doc_id(e, doctor_id))
                        ]
                    )
                ]
            )
        )
        )


    page.add(row_of_row)


app(target=main)


    