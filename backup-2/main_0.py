from Carro import Carro,ListaCarros
from Usuario import Usuario, ListaUsuario,Admin
from Menu import Menu,MenuUsuario, MenuAdmin
from Login import Login


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

# INSTANCIE OBJETOS

lista_de_carros = ListaCarros()
lista_de_usuarios = ListaUsuario()
menu_de_opcoes = Menu()
menu_de_usuario = MenuUsuario()
menu_de_admin = MenuAdmin()


login = Login()
sair = False


# PEGUE OS CARROS NO ARQUIVO

carrosFile = open("carro-data.txt","rt")
for line in carrosFile:
  dados = line.split()
  #xprint(dados)

  alugado = True if dados[5] == "True" else False
  dono = dados[len(dados)-1] if len(dados) == 7 else ""
  ano = int(dados[2])
  marca = dados[0]
  modelo = dados[1]
  preco = dados[3]
  assentos = dados[4]

  carro = Carro(marca,modelo,ano,preco,assentos,alugado,dono)

  lista_de_carros.setCarro(carro)
carrosFile.close()

# PEGUE OS USUÁRIOS NO ARQUIVO

usersFile = open("cliente-data.txt","rt")

for line in usersFile:
  dados = line.split()
  nome = " ".join(dados[0].split("_"))
  id_user = dados[1]
  logado = True if dados[2] == "1" else False
  password = dados[3]

  admin = True if dados[4] == "1" else False

  #TODO : superar limitação do arquivo de texto (como armazenar uma lista de objetos num txt) com JSON

  user = None

  if(admin):
    user = Admin(nome,id_user,logado,password,True)
  else:
    user = Usuario(nome,id_user,logado,password)

  lista_de_usuarios.setUsuarios(user)
usersFile.close()

# INTERFACE 

#lista_de_usuarios.mostrar()

# _ TODO->ELIMINAR TRECHO ABAIXO (TESTES SOMENTE) 

"""
usuario_temp = Usuario()
usuario_temp = usuario_temp.selecionarEm(lista_de_usuarios)

login.setSession(True)
login.setUserInSession(usuario_temp)
menu_de_opcoes.limparTela()
"""

# _ SEM LOGIN

while True:

  if(sair):
    break

  if(login.getSession()): # _ Checar o login foi feito
    usuario_atual = login.getUserInSession()
    
    print("U: {} @{}".format(usuario_atual.getNome(),usuario_atual.getId()))

    if(usuario_atual.getAdmin()): # _ Chegar se foi um usuário admin
      print("->[admin]\n--------")
      menu_de_admin.mostrar()

      action = input(">")
      try:
        action = int(action)  
      except:
        print("Valor inválido. Digite novamente")

      match action:
        case 0:
          break

        case 1:# MOSTRAR CARROS *
          lista_de_carros.mostrar()
        
        case 2:# PROCURAR CARROS *
          carro_procurado = lista_de_carros.criarCarroParaPesquisa()
        
          if(carro_procurado != None):
            carros_encontrados = lista_de_carros.procurar(carro_procurado)
            lista_de_carros.mostrarCarrosEncontrados(carros_encontrados)
        
        case 3: # ALUGUEL * 

          print("--- ALUGUEL  ---")
          carro_selecionado = usuario_atual.selecionarEm(lista_de_carros)

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
                usuario_para_alugar = usuario_atual.selecionarEm(lista_de_usuarios)

                asw_1 = simOUnao("alugar '{}' para '{}'".format(carro_selecionado.mostrar(),usuario_para_alugar.getNome()))

                if(asw_1):
                  usuario_para_alugar.alugarCarro(carro_selecionado)
                else:
                  print("AÇÃO CANCELADA")

            else:
              print("AÇÃO CANCELADA!")

        case 4: # DEVOLUÇÃO
          print("--- DEVOLUÇÃO  ---")
          carro_selecionado = usuario_atual.selecionarEm(lista_de_carros) # TODO uma função filter?

          if(carro_selecionado == None):
            print("Não foi possível selecionar tal veículo")
          else:
            #print(carro_selecionado.mostrar())
            asw = simOUnao("devolver {}".format(carro_selecionado.mostrar()))

            if(asw):
              if(carro_selecionado.getDono() == usuario_atual.getId()):
                usuario_atual.devolverCarro(carro_selecionado)
              else:
                usuario_escolhido = lista_de_usuarios.getById(carro_selecionado.getDono())

                if(usuario_escolhido != None):
                  usuario_escolhido.devolverCarro(carro_selecionado)
                else:
                  print("Não foi possível devolver o carro.")
            else:
              print("AÇÃO CANCELADA!")

        case 5: # MOSTRAR USUÁRIOS 

          #lista_de_usuarios.mostrar()
          usuario_atual.mostrarUsuarios(lista_de_usuarios)
        
        case 6: # CADASTRAR CARRO 
          usuario_atual.cadastarCarro(lista_de_carros)

        case 8: # CADASTRAR USUÁRIO 
          usuario_atual.cadastrarUsuario(lista_de_usuarios)
        
        case 7: # EDITAR CARRO
          carro_selecionado = usuario_atual.selecionarEm(lista_de_carros)

          if(carro_selecionado.getAlugado()):
            print("Não é possível editar os dados de um carro já alugado.\nÉ preciso que o veículo seja devolvido antes.")
          else:
            usuario_atual.editarCarro(carro_selecionado)

        case 9: # EDITAR USUARIO
          usuario_escolhido = usuario_atual.selecionarEm(lista_de_usuarios)

          usuario_atual.editarUsuario(usuario_escolhido,lista_de_usuarios)

        case 11:
          usuario_atual.removeCarro(lista_de_carros)

        case 10:
          usuario_atual.removerUser(lista_de_usuarios)

        case 12:
          print("Encerrar sessão")
          print("----------")
          print("Tem certeza que quer deslogar no sistema?")
          
          aws = input("[s/n]> ").lower()

          if(aws == "s"):
            usuario_atual.deslogar()
            login.setSession(False)
            login.setUserInSession(None)
            #menu_de_opcoes.limparTela()
            #pass

    else: # _  _ Chegar se foi um usuário comum
      print("--------")
      menu_de_usuario.mostrar()

      action = input(">")
      try:
        action = int(action)  
      except:
        print("Valor inválido. Digite novamente")

      match action:
        case 0:
          break
        case 1: # MOSTRAR CARROS
          lista_de_carros.mostrar()
        
        case 2: # PROCURAR CARROS
          carro_procurado = lista_de_carros.criarCarroParaPesquisa()
        
          if(carro_procurado != None):
            carros_encontrados = lista_de_carros.procurar(carro_procurado)
            lista_de_carros.mostrarCarrosEncontrados(carros_encontrados)

        case 3: # ALUGAR 
          print("--- ALUGUEL  ---")
          carro_selecionado = usuario_atual.selecionarEm(lista_de_carros)

          if(carro_selecionado == None):
            print("Não foi possível selecionar tal veículo")
          else:
            #print(carro_selecionado.mostrar())
            asw = simOUnao("alugar {}".format(carro_selecionado.mostrar()))

            if(asw):
              usuario_atual.alugarCarro(carro_selecionado)
            else:
              print("AÇÃO CANCELADA!")

        case 4: # DEVOLVER 
          print("--- DEVOLUÇÃO  ---")
          carro_selecionado = usuario_atual.selecionarEm(lista_de_carros) # TODO uma função filter?

          if(carro_selecionado == None):
            print("Não foi possível selecionar tal veículo")
          else:
            #print(carro_selecionado.mostrar())
            asw = simOUnao("devolver {}".format(carro_selecionado.mostrar()))

            if(asw):
              usuario_atual.devolverCarro(carro_selecionado)
            else:
              print("AÇÃO CANCELADA!")
        
        case 5:# VER CARROS 
          usuario_atual.mostrarCarrosAlugados()

        case 6:
          print("Encerrar sessão")
          print("----------")
          print("Tem certeza que quer deslogar no sistema?")
          
          aws = input("[s/n]> ").lower()

          if(aws == "s"):
            usuario_atual.deslogar()
            login.setSession(False)
            login.setUserInSession(None)
            #menu_de_opcoes.limparTela()
            #pass

        case _:
          print("Ação Inválida")

    menu_de_usuario.limparTela()    

  else: # _ SEM LOGIN
    #menu_de_usuario.mostrar()
    print("------\nOlá!\nBem vindo!\nPode fazer o login no sistema com um desses usuários:\nUsuario Admin - <id>: augusto <senha>: pass1\nUsuário - <id>: ursulaf <senha>: pass4\n------")
    menu_de_opcoes.mostrar()
    
    action = input(">")
    try:
      action = int(action)  
    except:
      print("Valor inválido. Digite novamente")
    match action:
      case 0:
        sair = True
        break

      case 1: # MOSTRAR CARRO
        lista_de_carros.mostrar()
      
      case 2:# PROCURAR CARROS
        carro_procurado = lista_de_carros.criarCarroParaPesquisa()
        
        if(carro_procurado != None):
          carros_encontrados = lista_de_carros.procurar(carro_procurado)

          lista_de_carros.mostrarCarrosEncontrados(carros_encontrados)

        pass
      
      case 3:
        print("Login no sistema")
        print("---------------")
        print("Insira:")
        user_id = input("Id de Usuário: ")
        user_pass = input("Senha: ")

        user_maybe = Usuario("",user_id,False,user_pass)

        user_in = login.validateUser(user_maybe,lista_de_usuarios)

        if(user_in == None):
          print("Usuário não encontrado.\nLogin ou senha incorretos.")
        else:
          print("Login com sucesso!\n Olá,{}!".format(user_in.getNome()))
          user_in.logar()
          login.setSession(True)
          login.setUserInSession(user_in)

          #menu_de_opcoes.limparTela()
          

      case _:
        print("Ação invalida")
    
    menu_de_opcoes.limparTela()
