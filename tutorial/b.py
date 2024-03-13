
class Pedido():
    def __init__(self) -> None:
        self.unpaid_objeto = UnpaidEstate()
        self.paid_objeto = PaidEstado()
        self.shipped_objeto = ShippedEstate()

        self.estado = self.unpaid_objeto

    def setEstate(self,state):
        self.estado = state

    def receivePayment(self): 
        self.estado.receivePayment()
    
    def ship(self):
        self.estado.ship()
    
    def mark(self):
        self.estado.mark()
        
    

class Estado():
    def receivePayment(self): 
        pass
    
    def ship(self):
        pass

    def mark():
        pass

class UnpaidEstate(Estado):
    def __init__(self,context:Pedido):
        self.context = context

    def receivePayment(self):
        self.context.setEstate(self.context.paid_objeto)
        print("pagamento aceito")

    def ship(self):
        print("Can't ship")
    
    def mark():
        print("cant amark")
    


class PaidEstado(Estado):
    def __init__(self,context:Pedido):
        self.context = context

    def receivePayment(self):
        print("pagamento já aceito.")

    def ship(self):
        self.context.setEstate(self.context.paid_objeto)
        print("Shiped")
    
    def mark():
        print("cant amark")

class ShippedEstate(Estado):
    def __init__(self,context:Pedido):
        self.context = context

    def receivePayment(self):
        print("pagamento já aceito.")

    def ship(self):
        print("já enviado")
    
    def mark():
        print("Já marcado")