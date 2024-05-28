from flet import * 
from pages.splash import SplashPage
from pages.register import RegisterPage
from pages.login import LoginPage
from pages.home import HomePage
from pages.diagnosis import DiagnosisPage
from pages.chatroom import ChatroomPage


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
        self.page.update()

    def parse_route_params(self, route):
        params = {}
        if "?" in route:
            param_str = route.split("?")[1]
            for param in param_str.split("&"):
                key, value = param.split("=")
                params[key] = value
        return params

