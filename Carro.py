from datetime import datetime

class Carro():

  def __init__(self, marca = "", modelo = "", ano = 0, preco = 0,assentos = 0,alugado=False,dono=""):
    self.__marca = marca.lower()
    self.__modelo = modelo
    self.__ano = ano
    self.__preco = float(preco)
    self.__assentos = int(assentos)
    self.__alugado = alugado
    self.__dono = dono

  def mostrar(self):
    return "{} {} {}".format(self.__marca,self.__modelo,self.__ano)
  
  def getPreco(self):
    return self.__preco
  def setPreco(self,value):
    
    try:
      newValue = float(value)
    except (TypeError, ValueError) as erro:
      raise type(erro)("Valor inválido")
    if(newValue < 0):
      print("Valor inválido: precisa ser um número positivo ou nulo")
      return
    
    self.__preco = newValue

  def getAno(self):
    return self.__ano 
  def setAno(self,value):
    
    try:
      newValue = int(value)
    except (TypeError, ValueError) as erro:
      raise type(erro)("Valor inválido")
    if(newValue < 0 or newValue > datetime.now().year):
      print("Valor inválido: precisa ser um número positivo ou ano até o ano atual: " + str(datetime.now().year))
      return
    
    self.__ano = newValue
    
  def getAssentos(self):
    return self.__assentos
  def setAssentos(self,value):
    
    try:
      newValue = int(value)
    except (TypeError, ValueError) as erro:
      raise type(erro)("Valor inválido")
    if(newValue <= 0):
      print("Valor inválido: precisa ser um número positivo")
      return
    
    self.__assentos = newValue
  
  def getDono(self):
    return self.__dono
  def setDono(self,value):
    self.__dono = value

  #TODO: tratmento de execeção nessas abaixo
  def getMarca(self):
      return self.__marca 
  def setMarca(self,value):
      self.__marca = str(value).lower()

  def getModelo(self):
      return self.__modelo
  def setModelo(self,value):
      self.__modelo = str(value).lower()

  def getAlugado(self):
    return self.__alugado
  def setAlugado(self,value):
    self.__alugado = value
  
class CarroPesquisado(Carro):
  def __init__(self,m="",md = "",a ="",p=0,asse = 0, al = False, dono = ""):
    super().__init__(m,md,a,p,asse,al,dono)
  
    self.__rangeAno = (0,0)
    self.__rangePreco = (0,0)
    self.__rangeAssentos = (0,0)
  
  def getRangeAno(self):
    return self.__rangeAno

  def setRangeAno(self,min,max):
    self.__rangeAno = (min,max)

  def getRangePreco(self):
    return self.__rangePreco

  def setRangePreco(self,min,max):
    self.__rangePreco = (min,max)

  def getRangeAssentos(self):
    return self.__rangeAssentos

  def setRangeAssentos(self,min,max):
    self.__rangeAssentos = (min,max)
    
class ListaCarros():
  def __init__(self,lista=[]):
        self.__lista = lista
  
  def getSize(self):
        return len(self.getCarro())

  def getCarro(self):
    return self.__lista
  
  def getByIdx(self,idx): #Retorne o carro na posição 'idx'
    return self.__lista[idx]

  def setCarro(self,value):
      self.__lista.append(value)
    
  def mostrar(self):
      print("""-------- lista de carros --------
<nome> <preço do aluguel> <número de assentos> <disponibilidade>
D: DISPONÍVEL
N/A: CARRO NÃO DISPONÍVEL (incluindo quem o alugou)
--------""")
      for count,carro in enumerate(self.__lista):
        disponivel = "D" if carro.getAlugado() is False else "N/A"

        contratante = "" if carro.getAlugado() is False else carro.getDono()

        print("[{}] {} R${:.2f} {} ({}) {}".format(count+1,
                                     carro.mostrar().capitalize(),
                                     carro.getPreco(),
                                     carro.getAssentos(),
                                     disponivel,
                                     contratante))
        #print(carro.getAno(),type(carro.getAno()))

      print("--------")
      return None

  def matchAtributes(self,atr_a,atr_b,option=1):
    #a: atributo já presente na lista
    #b: o que o usuario colocou
    
    if(option == 1): #string
      return (atr_a == atr_b) if atr_b != "" else 1

    if(option == 2): #range of values
      min_value = 0 if atr_b[0] == -1 else atr_b[0]
      max_value = atr_a if atr_b[1] == -1 else atr_b[1]

      return (atr_a >= min_value) and (atr_a <= max_value)

  def procurar(self,value):

    deuMatchCom = []
    for i,carro in enumerate(self.__lista):
      match_car = 0

      match_car += self.matchAtributes(carro.getMarca(),value.getMarca(),1)
      match_car += self.matchAtributes(carro.getModelo(),value.getModelo(),1)
      match_car += self.matchAtributes(carro.getPreco(),value.getRangePreco(),2)
      match_car += self.matchAtributes(carro.getAno(),value.getRangeAno(),2)
      match_car += self.matchAtributes(carro.getAssentos(),value.getRangeAssentos(),2)
      
      #print(match_car)
      if(match_car == 5):
        deuMatchCom.append(carro)

    return deuMatchCom

  def criarCarroParaPesquisa(self):
      print("- Pesquisa de Carro -")
      print("Preencha os campos abaixo para realizar a pesquisa")
      print("Caso não queira levar um campo em consideração, aperte 'ENTER' ao preencher")
      print("--------")
      print("- Insira -")

      carro_procurado = CarroPesquisado()

      marca = input("marca:").lower()
      modelo = input("modelo:").lower()

      ano_antigo = input("Do ano (inicial) :")
      ano_atual = input("até o ano (final) :")

      preco_min = input("preço (mínimo):")
      preco_max = input("preço (máximo):")
      assentos = input("Número de assentos (máximo):")

      try:
        #Flag -1: o valor númerico é inrrelavante no momento
        ano_antigo = int(ano_antigo) if ano_antigo != "" else -1
        ano_atual = int(ano_atual) if ano_atual != "" else -1 

        assentos = int(assentos) if assentos != "" else -1
        preco_min = float(preco_min) if preco_min != "" else -1
        preco_max = float(preco_max) if preco_max != "" else -1
      except:
        print("Valor inválido. O usuário digitou número inválido em um campo.\nTente novamente")
        return None

      carro_procurado.setMarca(marca)
      carro_procurado.setModelo(modelo)
      carro_procurado.setRangeAssentos(1,assentos)
      carro_procurado.setRangePreco(preco_min,preco_max)
      carro_procurado.setRangeAno(ano_antigo,ano_atual)
      
      
      
      return carro_procurado

  def mostrarCarrosEncontrados(self, carros_encontrados):
        print(" ----------- ")
        print("Carros econtrados:")

        if(carros_encontrados == []):
          print("Nenhum carro encontrado com tais parametros!")
        else:
          for carro in carros_encontrados:
            dispo = "DISPONIVEL" if carro.getAlugado() is False else "NÃO DISPONIVEL"

            print("{} R$ {:.2f} {}".format(carro.mostrar().capitalize(),carro.getPreco(),dispo))
        print(" ----------- ")

  def removeFrom(self,value):
        self.__lista.remove(value)

  