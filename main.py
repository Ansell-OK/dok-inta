from flet import * 
from utils import *
from route.flet_router import Router
from db.flet_pyrebase import PyrebaseWrapper

def main(page: Page):
    page.window_width = BASE_WIDTH
    page.window_height = BASE_HEIGHT
    page.padding = 0
    page.adaptive = True
    page.splash = None



    page.fonts = {
        'Poppins Regular': '/fonts/poppins/Poppins-Regular.ttf',
        'Poppins Bold': '/fonts/poppins/Poppins-Bold.ttf'
    }

    myPyrebase = PyrebaseWrapper(page)
    myRouter = Router(page, myPyrebase)

    page.on_route_change = myRouter.route_change

    page.add(
        myRouter.body
    )

    page.go('/')

    

    

app(target=main, assets_dir='assets')