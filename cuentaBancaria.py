class CuentaBancaria():
    ''' Clase que nos permite la gestión de una Cuenta Bancaria genérica!
    '''
    
    def __init__(self, saldo_inicialCC,saldo_inicialCA, nombre, apellido, moneda = '$'):
        # TODO: Ver la forma de soportar cajas de ahorro y/o cuentas corrientes
        #Agrego en el constructor los argumentos que refieren a monto en cada cuenta:saldo_inicialCC, saldo_inicialCA
        self.movimientos = []
        self.saldoCC = saldo_inicialCC
        self.saldoCA= saldo_inicialCA
        self.nombre = nombre
        self.apellido = apellido
        self.moneda = moneda
        
    

    def depositar_CA(self, monto):
        '''Método que nos permite realizar un depósito bancario en Caja de Ahorro'''
        self.movimientos.append('DEPOSITO en CA: ' + str(monto))
        self.saldoCA = self.saldoCA + monto

    def depositar_CC(self, monto):
        '''Método que nos permite realizar un depósito bancario en Cuenta Corriente'''
        self.movimientos.append('DEPOSITO en CC: ' + str(monto))
        self.saldoCC = self.saldoCC + monto
        


    def extraer_CA(self, monto):
        '''Método que nos permite realizar una extracción de una caja de ahorro'''
        
        if self.saldoCA - monto >= 0:
            self.movimientos.append('EXTRACCION de CA: ' + str(monto))
            self.saldoCA = self.saldoCA - monto
        else:
           self.movimientos.append('SALDO INSUFICIENTE en CA: ' + str(monto)) 
           print("Saldo insuficiente en CA")

    def extraer_CC(self, monto):
        '''Método que nos permite realizar una extracción de una caja de ahorro'''
        
        if self.saldoCC - monto >= 0:
            self.movimientos.append('EXTRACCION de CC: ' + str(monto))
            self.saldoCA = self.saldoCA - monto
        else:
           self.movimientos.append('SALDO INSUFICIENTE en CC: ' + str(monto)) 
           print("Saldo insuficiente en CC")
        
           

    def datos_titular(self):
        '''Método que nos permite mostrar los datos del titular y su saldo'''
        return self.apellido + ', ' + self.nombre + " con el saldo: " + str(self.saldo) + " " + self.moneda
    
    def datos_saldo(self):
        return self.saldoCC
        return self.saldoCA

    def _reset_saldo(self):
        self.saldoCC = 0 
        self.saldoCA=0

    def datos_movimientos(self):
        return list(self.movimientos) 