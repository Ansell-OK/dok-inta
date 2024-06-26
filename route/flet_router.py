from flet import * 
from pages.splash import SplashPage
from pages.register import RegisterPage
from pages.login import LoginPage
from pages.home import HomePage
from pages.diagnosis import DiagnosisPage
from pages.chatroom import ChatroomPage
from pages.user_details import UserDetails
from pages.medical_info import medical_information
from pages.disease import DiseasePage
from pages.doctor_details import DoctorPage


class Router:

    def __init__(self, page, myPyrebase):
        self.page = page
        self.myPyrebase = myPyrebase
        self.routes = {
            "/": SplashPage(page, myPyrebase),
            "/login": LoginPage(page, myPyrebase),
            "/register": RegisterPage(page, myPyrebase),
            "/home": HomePage(page, myPyrebase),
            "/diagnosis": DiagnosisPage(page, myPyrebase), 
            '/user_details': UserDetails(page, myPyrebase), 
            '/medical_info': medical_information(page, myPyrebase)
        }
        self.body = Container(content=self.routes['/']["view"])

    def route_change(self, route):
        route_path = route.route.split("?")[0]
        if route_path in self.routes:
            self.body.content = self.routes[route_path].get("view")
            if self.routes[route_path].get("load"):
                self.routes[route_path].get("load")()
        elif route_path == "/chatroom":
            params = self.parse_route_params(route.route)
            chat_room_id = params.get("chat_room_id")
            if chat_room_id:
                chatroom_page = ChatroomPage(self.page, self.myPyrebase, chat_room_id)
                self.body.content = chatroom_page["view"]
                chatroom_page["load"]()
        elif route_path == "/disease":
            params = self.parse_route_params(route.route)
            disease_name = params.get("disease_name")
            if disease_name:
                disease = DiseasePage(self.page, self.myPyrebase, disease_name)
                self.body.content = disease["view"]
                disease["load"]()
        elif route_path == "/doctor_details":
            params = self.parse_route_params(route.route)
            doctor_id = params.get("doctor_id")
            if doctor_id:
                details_page = DoctorPage(self.page, self.myPyrebase, doctor_id)
                self.body.content = details_page["view"]
                details_page["load"]() 
        self.page.update()

    def parse_route_params(self, route):
        params = {}
        if "?" in route:
            param_str = route.split("?")[1]
            for param in param_str.split("&"):
                key, value = param.split("=")
                params[key] = value
        return params

