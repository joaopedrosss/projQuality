from os import system,name

class Menu():
    def __init__(self, lista = ["Sair","Listar veículos","Procurar veículos","Logar no sistema"]):
        self.__actions = lista
    
    def mostrar(self):
        print("RENTAL CAR\nDigite o número da ação que deseja fazer\n------------")
        for i,action in enumerate(self.__actions):
            print("[{}] {}".format(i,action))
        print("------------")

    def limparTela(self):
        cmd = input("<Aperte qualquer botão para voltar ao menu principal>")
        if(name == "nt"): #windows
            system("cls")
        else:
            system("clear")

    
class MenuUsuario(Menu):
    
    def __init__(self, lista = ["Sair",
                                "Listar veículos",
                                "Procurar veículos",
                                "Alugar veículo",
                                "Devolver veículo",
                                "Ver veículos alugados",
                                "Deslogar no sistema"]):
        super().__init__(lista)
        #self.__actions.remove("Logar no sistema")
        #self.__actions.extends(["Alugar/Devolver veículos","Ver carros alugados","Deslogar no sistema"])
    

class MenuAdmin(Menu):
    def __init__(self, lista = ["Sair",
                                "Listar veículos",
                                "Procurar veículos",
                                "Alugar veículo",
                                "Devolver veículo",
                                "Ver usuários cadastrados",
                                "Cadastrar veículo",
                                "Editar dados de veículos",
                                "Cadastrar usuário",
                                "Editar dados de usuário",
                                "Remover usuário",
                                "Remover veículo",
                                "Deslogar"]):
        super().__init__(lista)