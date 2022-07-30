from cuentaBancaria import CuentaBancaria

# Creación de objeto
x = CuentaBancaria(1000, 500000, 'Felipe', 'Morales')

# Invocación de métodos
print(x.datos_titular())

#Elegir cuenta 
x.cuenta()

# Operación de deposito
x.depositar_CA(100000)
print(x.datos_saldoCA())

# Operación de extracción
x.extraer_CC(900000)
print(x.datos_saldo())

# Imprimo el listado de movimientos de la cuenta
print(x.datos_movimientos())