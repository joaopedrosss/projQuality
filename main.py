from Carro import Carro,ListaCarros
from Usuario import Usuario, ListaUsuario,Admin
#from Menu import Menu,MenuUsuario, MenuAdmin
from Login import Login
from Usuario_State import UsuarioState
from os import system,name


def limparTela():
        cmd = input("<Aperte qualquer botão para voltar ao menu principal>")
        if(name == "nt"): #windows
            system("cls")
        else:
            system("clear")

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
#menu_de_usuario = MenuUsuario()




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


option = UsuarioState(lista_de_usuarios,lista_de_carros)

# _ SEM LOGIN

while True:
    if(sair):
      break
  
    usuario_atual = login.getUserInSession()

     # DEFINIR O ESTADO
    if(usuario_atual == None):
      option.changeToNoLogin()
      option.setUsuarioAtual(usuario_atual)
    else:
      print("U: {} @{}".format(usuario_atual.getNome(),usuario_atual.getId()))

      option.setUsuarioAtual(usuario_atual)
      if(usuario_atual.getAdmin()):
        option.changeToAdmin()
        print("->[admin]\n--------")
      else:
        option.changeToComum()

    option.menu()

    action = input(">")
    try:
      action = int(action)  
    except:
      print("Valor inválido. Digite novamente")

    if(usuario_atual == None):
      if(action == 13):
        action = 78
      if (action == 3):
        action = 13

    if(usuario_atual != None):
      if(action == 6 and not(usuario_atual.getAdmin())):
        action = 13
      if(action == 13 and not(usuario_atual.getAdmin())):
        action = 90
    
    match action:
      case 0: # SAIR
        break
      case 1:#  Listar veículos
          lista_de_carros.mostrar()
        
      case 2:# Procurar veículos
        carro_procurado = lista_de_carros.criarCarroParaPesquisa()
        
        if(carro_procurado != None):
          carros_encontrados = lista_de_carros.procurar(carro_procurado)
          lista_de_carros.mostrarCarrosEncontrados(carros_encontrados)

      case 3:# Alugar veículo
        option.alugar()
      
      case 4: # Devolver veículo
        option.devolver()
      
      case 5:# Ver meus veículos alugados
        option.mostrarAluguados()
      
      case 6:# Ver usuários cadastrados
        option.mostrarUsuarios()
      
      case 7: # Cadastrar veículo 
          option.cadastarCarro()
      
      case 8: #Editar dados de veículos
        option.editarCarro()
      
      case 9: # Cadastrar usuário
        option.cadastrarUsuario()
      
      case 10: # Editar dados de usuário
        option.editarUsuario()
      
      case 11: #	Remover usuário
        option.removerUsuario()
      
      case 12: # Remover veículo
        option.removerCarro()
      
      case 13: # Deslogar
        option.handleSessao(login,usuario_atual)
      
      case _:
          print("Ação Inválida")

    limparTela()    

# _ COM LOGIN DE USUÁRIO

# _ COM LOGIN DE ADMIN
