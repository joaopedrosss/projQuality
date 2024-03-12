from Carro import Carro

class Usuario():
    
    def __init__(self,nome= '',id = '',logado = False,passw = "",admin = False,carros = []):
        self.__nome = nome
        self.__id = id
        self.__carros = carros
        self.__login = logado
        self.__admin = admin
        self.__password = passw

    """    
    def alugarCarro(self,carro):
        print("------------")
        print("Aluguel/Devolução de Veículos")
        print("------------")
    """

    def mostrarCarrosAlugados(self):
        print("--- CARROS ALUGADOS ---")
        for carro in self.getCarros():
            print("{} R${:.2f}".format(carro.mostrar().capitalize(),carro.getPreco()))
        print("---                 ---")

    def getAdmin(self):
        return self.__admin
   
    def getPass(self):
        return self.__password
    def setPass(self,value):
        self.__password = value

    def getLogin(self):
        return self.__login
    def setLogin(self,value):
        self.__login = value
    
    def getNome(self):
        return self.__nome
    def getId(self):
        return self.__id
    def getCarros(self):
        return self.__carros
    
    def setNome(self, value):
        self.__nome = value
    def setId(self,value):
        self.__id = value

    def logar(self):
        self.setLogin(True)
    def deslogar(self):
        self.setLogin(False)

    def selecionarEm(self,lista): #lista = lista_objeto
        lista.mostrar()

        carro_idx = input("Digite o indíce do item desejado >")

        try:
            carro_idx = int(carro_idx)
        except:
            print("Valor inválido.\nTente novamente")
            return None
        
        if(carro_idx <= 0 or carro_idx > lista.getSize()):
            print("Indíce inválido.\nTente novamente")
            return None
        else:
            return lista.getByIdx(carro_idx-1)
        
    def alugarCarro(self,carro):        
        if(carro.getAlugado() is False):
            carro.setAlugado(True)
            carro.setDono(self.getId())
            self.__carros.append(carro)
            print("Carro alugado com sucesso")
        else:
            print("O veículo já está alugado.\nNão é possível aluga-lo.")

    def devolverCarro(self,carro):
        if((carro.getAlugado() is True) and carro.getDono() == self.getId()):
            carro.setAlugado(False)
            carro.setDono("")
            self.__carros.remove(carro)
            print("Veículo devolvido com sucesso")
        else:
            print("O veículo não foi alugado por você.\nNão é possível devolver tal veículo.")
 
class Admin(Usuario):
    def __init__(self,nome= '',id_ = '',logado = False,passw = "",admin = True,carros = []):
        super().__init__(nome,id_,logado,passw,admin,carros)
    
    def cadastarCarro(self,lista):
        print("---- Cadastro de Carro ----")
        print("- Insira -")
        try:
            marca = input("marca:")
            modelo = input("modelo:")
            ano = int(input("ano:"))
            preco = float(input("preço de aluguel:"))
            lugares = int(input("número de lugares:"))
        except:
            print("Input inválido em campo.\nNão é possível cadastrar carro.")

        
        confirm = self.simOUnao("cadastrar carro '{} {} {}'".format(marca,modelo,ano)) 

        if(confirm is True):
          lista.setCarro(Carro(marca,modelo,ano,preco,lugares))
          print("Carro cadastrado com sucesso!")
        else:
          print("Cadastro cancelado!")
        
    def cadastrarUsuario(self,lista_de_usuarios):
        print("---- Cadastrar usuário ----")
        print("Digite os dados do usuário que deseja cadastrar")
        print("- Insira -")
        nome_usuario = input("Nome:").lower().split()

        nome_usuario = self.juntarNome(nome_usuario)

        #print(nome_usuario)

        id_usuario = ""
        while True:
          id_usuario = input("Id:").lower()

          if id_usuario in lista_de_usuarios.getIds():
            print("Esse id já existe.\nInsira outro,por favor.")
          else:
            break
    
        senha = input("Senha:")

        
        admin = self.simOUnao("seja um usuário admin")

        asw = self.simOUnao("cadastar este usuário: 'nome:{} senha:[{}] id:[{}]' admin:{}".format(nome_usuario,senha,id_usuario,admin))

        if(asw):
            if(admin):
                lista_de_usuarios.setUsuarios(Admin(nome_usuario,id_usuario,False,senha,True))
            else:
                lista_de_usuarios.setUsuarios(Usuario(nome_usuario,id_usuario,False,senha,False))
            print("Usuário cadastrado com sucesso")
        else:
            print("Ação cancelada")

    def editarCarro(self,carro):

        print("---- Editar dados de carro ----")

        confirmar = self.simOUnao("editar dados do carro '{}'".format(carro.mostrar()))

        if(confirmar):
            print("Insira os novos dados")
            print("Caso não queira fazer modificações, aperter ENTER no campo selecionado")

            new_marca = input("marca [{}] :".format(carro.getMarca())).strip().lower()

            new_model = input("modelo [{}] :".format(carro.getModelo())).strip().lower()

            new_ano = input("ano [{}] : ".format(carro.getAno())).strip().lower()

            new_preco = input("preço [R$ {:.2f}] : ".format(carro.getPreco())).strip()

            new_lugares = input("número de assentos [{}] :".format(carro.getAssentos())).strip()

            try:
                new_marca = carro.getMarca() if new_marca == "" else new_marca
                new_model = carro.getModelo() if new_model == "" else new_model
                new_ano = carro.getAno() if new_ano == "" else int(new_ano)
                new_preco = carro.getPreco() if new_preco == "" else float(new_preco)
                new_lugares = carro.getPreco() if new_lugares == "" else int(new_lugares)

            except:
                print("Valor inválido inserido em campo.\nTente novamente")

            carro.setAno(new_ano)
            carro.setMarca(new_marca)
            carro.setModelo(new_model)
            carro.setPreco(new_preco)
            carro.setAssentos(new_lugares)

            print("Dados editados com sucesso!")

        else:
            print("AÇÃO CANCELADA")

    def editarUsuario(self,user,lista):

        print("---- Editar dados de usuário ----")

        confirmar = self.simOUnao("editar dados do usuário '{}'".format(user.getNome()))

        if(confirmar):
            print("Insira os novos dados")
            print("Caso não queira fazer modificações, aperter ENTER no campo selecionado")

            new_nome = input("nome [{}] :".format(user.getNome())).strip()

            new_id = ""
            while True:
                new_id = input("id [{}] :".format(user.getId())).strip()

                if(new_id == ""):
                    break

                if new_id in lista.getIds():
                    print("Esse id já existe.\nTente novamente.\n")
                else:
                    break
                
            new_pasword = input("senha [{}] :".format(user.getPass())).strip()

            new_nome = user.getNome() if new_nome == "" else new_nome
            new_id = user.getId() if new_id == "" else new_id
            new_pasword = user.getPass() if new_pasword == "" else new_pasword

            user.setNome(new_nome)
            user.setId(new_id)
            user.setPass(new_pasword)

            print("Dados editados com sucesso!")
        else:
            print("Ação cancelada")

    def removeCarro(self,lista):
        print("----- Remoção de carro -----")
        carro = self.selecionarEm(lista)

        if(carro == None):
            print("Carro não encontrado.\nNão é possível remover")
            return
        if(carro.getAlugado() is True):
            print("Não é possível remover o carro, pois este está já alugado.\nPara remoção,faça a devolução do veículo.")
            return 
        
        confirmar = self.simOUnao("remover '{}' da base dados".format(carro.mostrar()))
        if(confirmar):
            lista.removeFrom(carro)
            print("Carro removido com sucesso")
        else:
            print("Ação cancelada")


    def removerUser(self,lista):
        print("----- Remoção de usuário -----")
        user = self.selecionarEm(lista)

        if(user == None):
            print("Usuário não encontrado.\nNão é possível remover")
            return
        if(user.getCarros() != []):
            print("Não é possível remover o usuário, pois este está em débito.\nPara remoção,o usuário precisa devolver os veículos alugados por ele.")
            for i in user.getCarros():
                print("-> {}".format(i.mostrar()))

            return 
        
        confirmar = self.simOUnao("remover '{}' da base dados".format(user.getNome()))
        if(confirmar):
            lista.removeFrom(user)
            print("Usuário removido com sucesso")
        else:
            print("Ação cancelada")

    def mostrarUsuarios(self,lista):
        print("Lista de Usuários cadastrados")
        print(" <nome> [<id]> [<senha>]")
        print(" ------------ ")
        
        if(lista.getUsuarios() == []):
            print("Não há usuários cadastrados.")
        else:
            for count,user in enumerate(lista.getUsuarios()):
                #print("{} [{}] <{}>".format(user.getNome(),user.getId(),user.getPass()))
                word = "{} {} [{}]".format(count+1,user.getNome(),user.getId())
                word += " [{}]".format(user.getPass())
                word += " (admin)" if user.getAdmin() else ""

                print(word)
                
        
        print(" ------------ ")

    def simOUnao(self,acao):
  
        while(True):
            confirm = input("Deseja {}? (s/n): ".format(acao)).lower()

            if confirm == "":
                print("Ação inválida\nInsira 'S' para confirma ou 'N' para cancelar")
            elif(confirm[0] == "s" or confirm[0] == "n"):
                break
            else:
                print("Ação inválida\nInsira 'S' para confirma ou 'N' para cancelar")

        return (confirm[0] == "s")

    def juntarNome(self,array):
        novo = []
        for i in array:
            novo.append(i.capitalize()) 
        
        #print(" ".join(novo))

        return " ".join(novo)
    
class ListaUsuario():
    def __init__(self,lista = []):
        self.__lista = lista

    def getSize(self):
        return len(self.getUsuarios())
    
    def getByIdx(self,idx): #Retorne o  na posição 'idx'
        return self.__lista[idx]

    def getUsuarios(self):
        return self.__lista
    
    def setUsuarios(self,value):
        self.__lista.append(value)

    def mostrar(self):
        print("Lista de Usuários cadastrados")
        print(" <nome> [<id]>")
        print(" ------------ ")
        
        if(self.getUsuarios() == []):
            print("Não há usuários cadastrados.")
        else:
            for count,user in enumerate(self.getUsuarios()):
                #print("{} [{}] <{}>".format(user.getNome(),user.getId(),user.getPass()))
                word = "{} {} [{}]".format(count+1,user.getNome(),user.getId())
                word += " (admin)" if user.getAdmin() else ""

                print(word)
                
        
        print(" ------------ ")

    def getById(self,id_procurado):
        for user in self.getUsuarios():
            if user.getId() == id_procurado:
                return user
        return None

    def getIds(self):
        array = []

        for i in self.getUsuarios():
            array.append(i.getId())
        
        return array

    def removeFrom(self,value):
        self.__lista.remove(value)

    def procurar(self,value):
        pass

    def theUserExist(self,value):
        pass
        
    






