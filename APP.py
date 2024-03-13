from Carro import Carro,ListaCarros
from Usuario import Usuario, ListaUsuario,Admin
from Menu import Menu,MenuUsuario, MenuAdmin
from Login import Login


class App():
    def __init__(self) -> None:
        self.sem_login = SemLogin()
        self.login_comum = LoginComum()
        self.login_admin = LoginAdmin()

        self.state = self.sem_login
    
    def setEstado(self,state):
        self.state = state

    


class State():

    def logar():
        pass
    def deslogar():
        pass


class SemLogin(State):
    def __init__(self,context: App):
        self.context = context

    def logar(self):
        pass
    

class LoginComum(State):
        pass

class LoginAdmin(State):
    pass