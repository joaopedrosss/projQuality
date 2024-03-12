
"""
from main import createCar,criarUsuario

usuarios_cadastrados = []

usuarios_cadastrados.append(criarUsuario("Augusto Guedes","augusto"))
usuarios_cadastrados.append(criarUsuario("Arthur Marques","marquesArthur"))
usuarios_cadastrados.append(criarUsuario("Rafael Pereira","rafael"))
usuarios_cadastrados.append(criarUsuario("Rafaela Goes","rafaela"))
usuarios_cadastrados.append(criarUsuario("Ursula Ferreira","ursulaf"))
usuarios_cadastrados.append(criarUsuario("Marcelo Cruz De Almeira","marceloCruz"))

carros_cadastrados = []

carros_cadastrados.append(createCar("ford","car",2010,500,4))
carros_cadastrados.append(createCar("fiat","uno",2010,420,4))
carros_cadastrados.append(createCar("fiat","elba",2008,320,4))
carros_cadastrados.append(createCar("fiat","tempra",1991,320,4))
carros_cadastrados.append(createCar("pegout","boxer furgao",2001,130,6))
carros_cadastrados.append(createCar("mcLaren","artura",2012,1200,2))
carros_cadastrados.append(createCar("ferrari","288 gto",1984,1300,2))
carros_cadastrados.append(createCar("honda","civic",2010,600,4))
carros_cadastrados.append(createCar("honda","velozte",2005,200,3))
carros_cadastrados.append(createCar("bulgati","aventador",2012,1000,2))
carros_cadastrados.append(createCar("bulgati","forza",2012,1500,2))

file = open("carro-data.txt","w")

for carro in carros_cadastrados:
    carData = "{} {} {} {} {} {} {}\n".format(carro.marca,
                                            carro.modelo,
                                            carro.ano,
                                            carro.preco,
                                            carro.lugares,
                                            carro.alugado,
                                            carro.dono)
    file.write(carData)


file.close()

file = open("cliente-data.txt","w")

for cliente in usuarios_cadastrado:
    clienteData = "{} {}\n".format(cliente.nome,cliente.id)

    file.write(clienteData)

file.close()
"""