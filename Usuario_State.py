from Usuario import Usuario
def simOUnao(acao):
  
  while(True):
    confirm = input("Deseja {}? (s/n): ".format(acao)).lower()

    if confirm == "":
      print("Ação inválida\nInsira 'S' para confirma ou 'N' para cancelar")
    elif(confirm[0] == "s" or confirm[0] == "n"):
      break
    else:
      print("Ação inválida\nInsira 'S' para confirma ou 'N' para cancelar")
          
  
  return (confirm[0] == "s")

class UsuarioState():
    def __init__(self,lista_de_usuarios,lista_de_carros):
        self.usuario_comum = UsuarioComum(lista_de_carros,self)
        self.usuario_admin = UsuarioAdmin(lista_de_usuarios,lista_de_carros,self)
        self.usuario_sem_login = UsuarioSemLogin(lista_de_usuarios,self)
        self.state = self.usuario_sem_login

        self.usuario_atual = None

    def setUsuarioAtual(self,usuario):
       self.usuario_atual = usuario

    def changeToAdmin(self):
        self.state = self.usuario_admin
    
    def changeToComum(self):
       self.state = self.usuario_comum

    def changeToNoLogin(self):
       self.state = self.usuario_sem_login
    
    def alugar(self):
       self.state.alugar(self.usuario_atual)

    def devolver(self):
       self.state.devolver(self.usuario_atual)
    
    def mostrarUsuarios(self):
       self.state.mostrarUsuarios(self.usuario_atual)

    def cadastarCarro(self):
       self.state.cadastarCarro(self.usuario_atual)
    
    def cadastrarUsuario(self):
       self.state.cadastrarUsuario(self.usuario_atual)
    
    def editarCarro(self):
       self.state.editarCarro(self.usuario_atual)

    def editarUsuario(self):
       self.state.editarUsuario(self.usuario_atual)
    
    def removerCarro(self):
       self.state.removerCarro(self.usuario_atual)
    
    def removerUsuario(self):
       self.state.removerUsuario(self.usuario_atual)
    
    def mostrarAluguados(self):
       self.state.mostrarAluguados(self.usuario_atual)

    def menu(self):
       self.state.menu()

    def handleSessao(self,login,usuario_atual):
        self.state.handleSessao(login,usuario_atual)

class State():
    def menu(self):
       pass

    def alugar(self,usuario_atual):
        pass
    
    def alugar(self,usuario_atual):
       pass

    def devolver(self,usuario_atual):
       print("Ação Inválida")
       pass

    def mostrarUsuarios(self,usuario_atual):
       print("Ação Inválida")
       pass

    def cadastarCarro(self,usuario_atual):
       print("Ação Inválida")
       pass

    def cadastrarUsuario(self,usuario_atual):
       print("Ação Inválida")
       pass

    def editarCarro(self,usuario_atual):
       print("Ação Inválida")
       pass

    def editarUsuario(self,usuario_atual):
       print("Ação Inválida")
       pass

    def removerCarro(self,usuario_atual):
       print("Ação Inválida")
       pass

    def removerUsuario(self,usuario_atual):
       print("Ação Inválida")
       pass

    def mostrarAluguados(self,usuario_atual):
       print("Ação Inválida")
       pass

    def handleSessao(self,login,usuario_atual):
        pass
    


class UsuarioSemLogin(State):
    def __init__(self,lista_de_usuarios,context:UsuarioState):
       self.lista_de_usuarios = lista_de_usuarios
       self.context = context

    def menu(self):
    
       opcoes = ["Sair","Listar veículos","Procurar veículos","Logar no sistema"]

       print("------\nOlá!\nBem vindo!\nPode fazer o login no sistema com um desses usuários:\nUsuario Admin - <id>: augusto <senha>: pass1\nUsuário - <id>: ursulaf <senha>: pass4\n------")

       for i,action in enumerate(opcoes):
            print("[{}] {}".format(i,action))
    
    def handleSessao(self,login,usuario_atual):
        print("Login no sistema")
        print("---------------")
        print("Insira:")
        user_id = input("Id de Usuário: ")
        user_pass = input("Senha: ")

        user_maybe = Usuario("",user_id,False,user_pass)

        user_in = login.validateUser(user_maybe,self.lista_de_usuarios)

        if(user_in == None):
          print("Usuário não encontrado.\nLogin ou senha incorretos.")
        else:
          print("Login com sucesso!\n Olá,{}!".format(user_in.getNome()))
          user_in.logar()
          login.setSession(True)
          login.setUserInSession(user_in)

          if(user_in.getAdmin()):
            self.context.changeToAdmin()
          else:
             self.context.changeToComum()
          #b?
        

class UsuarioComum(State):
    def __init__(self,lista_de_carros,context:UsuarioState):
       self.lista_de_carros = lista_de_carros
       self.context = context

    def menu(self):
       opcoes = ["Sair","Listar veículos","Procurar veículos","Alugar veículo","Devolver veículo","Ver meus veículos alugados","Deslogar no sistema"]

       for i,action in enumerate(opcoes):
            print("[{}] {}".format(i,action))

    def alugar(self, usuario_atual):
          print("--- ALUGUEL  ---")
          carro_selecionado = usuario_atual.selecionarEm(self.lista_de_carros)

          if(carro_selecionado == None):
            print("Não foi possível selecionar tal veículo")
          else:
            #print(carro_selecionado.mostrar())
            asw = simOUnao("alugar {}".format(carro_selecionado.mostrar()))

            if(asw):
              usuario_atual.alugarCarro(carro_selecionado)
            else:
              print("AÇÃO CANCELADA!")
    
    def devolver(self,usuario_atual):
          print("--- DEVOLUÇÃO  ---")
          carro_selecionado = usuario_atual.selecionarEm(self.lista_de_carros) # TODO uma função filter?

          if(carro_selecionado == None):
            print("Não foi possível selecionar tal veículo")
          else:
            #print(carro_selecionado.mostrar())
            asw = simOUnao("devolver {}".format(carro_selecionado.mostrar()))

            if(asw):
              usuario_atual.devolverCarro(carro_selecionado)
            else:
              print("AÇÃO CANCELADA!")
    
    # Os códigos abaixo com "Sem acesso a essa funcionalidade!" são totalmente sem uso. 
    # Apenas sevrem de exemplo
    def mostrarUsuarios(self,usuario_atual):
       print("Sem acesso a essa funcionalidade!")
       return -1

    def cadastarCarro(self,usuario_atual):
       print("Sem acesso a essa funcionalidade!")
       return -1
    
    def cadastrarUsuario(self,usuario_atual):
       print("Sem acesso a essa funcionalidade!")
       return -1
    
    def editarCarro(self,usuario_atual):
       print("Ação Inválida")
       return -1
    
    def mostrarAluguados(self,usuario_atual):
       usuario_atual.mostrarCarrosAlugados()
    
    def handleSessao(self,login,usuario_atual):
          print("Encerrar sessão")
          print("----------")
          print("Tem certeza que quer deslogar no sistema?")
          
          aws = input("[s/n]> ").lower()

          if(aws == "s"):
            usuario_atual.deslogar()
            login.setSession(False)
            login.setUserInSession(None)
            self.context.changeToNoLogin()
    

       
class UsuarioAdmin(State):
    def __init__(self,lista_de_usuarios,lista_de_carros,context:UsuarioState):
       self.lista_de_usuarios = lista_de_usuarios
       self.lista_de_carros = lista_de_carros
       self.context = context

    def alugar(self,usuario_atual):
          print("--- ALUGUEL  ---")
          carro_selecionado = usuario_atual.selecionarEm(self.lista_de_carros)

          if(carro_selecionado == None):
            print("Não foi possível selecionar tal veículo")
          else:
            #print(carro_selecionado.mostrar())
            asw = simOUnao("alugar {}".format(carro_selecionado.mostrar()))

            if(asw):

              print("Para quem deseja alugar?")
              print("[0] Eu mesmo")
              print("[1] Outro usuário")

              try:
                alugarParaOutro = int(input("[0/1] >"))
              except:
                print("Valor inválido")

              if(not(alugarParaOutro)):
                usuario_atual.alugarCarro(carro_selecionado)
              else:
                usuario_para_alugar = usuario_atual.selecionarEm(self.lista_de_usuarios)

                asw_1 = simOUnao("alugar '{}' para '{}'".format(carro_selecionado.mostrar(),usuario_para_alugar.getNome()))

                if(asw_1):
                  usuario_para_alugar.alugarCarro(carro_selecionado)
                else:
                  print("AÇÃO CANCELADA")

            else:
              print("AÇÃO CANCELADA!")
    
    def devolver(self, usuario_atual):
          print("--- DEVOLUÇÃO  ---")
          carro_selecionado = usuario_atual.selecionarEm(self.lista_de_carros) # TODO uma função filter?

          if(carro_selecionado == None):
            print("Não foi possível selecionar tal veículo")
          else:
            #print(carro_selecionado.mostrar())
            asw = simOUnao("devolver {}".format(carro_selecionado.mostrar()))

            if(asw):
              if(carro_selecionado.getDono() == usuario_atual.getId()):
                usuario_atual.devolverCarro(carro_selecionado)
              else:
                usuario_escolhido = self.lista_de_usuarios.getById(carro_selecionado.getDono())

                if(usuario_escolhido != None):
                  usuario_escolhido.devolverCarro(carro_selecionado)
                else:
                  print("Não foi possível devolver o carro.")
            else:
              print("AÇÃO CANCELADA!")

    def mostrarUsuarios(self,usuario_atual):
       usuario_atual.mostrarUsuarios(self.lista_de_usuarios)

    def cadastarCarro(self,usuario_atual):
       usuario_atual.cadastarCarro(self.lista_de_carros)
    
    def cadastrarUsuario(self,usuario_atual):
       usuario_atual.cadastrarUsuario(self.lista_de_usuarios)
    
    def editarCarro(self,usuario_atual):
          carro_selecionado = usuario_atual.selecionarEm(self.lista_de_carros)

          if(carro_selecionado.getAlugado()):
            print("Não é possível editar os dados de um carro já alugado.\nÉ preciso que o veículo seja devolvido antes.")
          else:
            usuario_atual.editarCarro(carro_selecionado)
    
    def editarUsuario(self,usuario_atual):
        usuario_escolhido = usuario_atual.selecionarEm(self.lista_de_usuarios)

        usuario_atual.editarUsuario(usuario_escolhido,self.lista_de_usuarios)
    
    def removerCarro(self,usuario_atual):
       usuario_atual.removeCarro(self.lista_de_carros)
    
    def removerUsuario(self,usuario_atual):
       usuario_atual.removerUser(self.lista_de_usuarios)
    
    def mostrarAluguados(self,usuario_atual):
       usuario_atual.mostrarCarrosAlugados()
    
    def menu(self):
       opcoes = ["Sair","Listar veículos","Procurar veículos","Alugar veículo","Devolver veículo","Ver meus veículos alugados","Ver usuários cadastrados","Cadastrar veículo","Editar dados de veículos","Cadastrar usuário","Editar dados de usuário","Remover usuário","Remover veículo","Deslogar no sistema"]

       for i,action in enumerate(opcoes):
            print("[{}] {}".format(i,action))
    
    def handleSessao(self,login,usuario_atual):
          print("Encerrar sessão")
          print("----------")
          print("Tem certeza que quer deslogar no sistema?")
          
          aws = input("[s/n]> ").lower()

          if(aws == "s"):
            usuario_atual.deslogar()
            login.setSession(False)
            login.setUserInSession(None)
            self.context.changeToNoLogin()