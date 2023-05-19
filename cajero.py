from datetime import datetime
print("Bienvenido al cajero")
data = []

def menuPrincipal():
  op = input("Selecciona una opción \n 1.Registrar\n 2.Ingresar \n 3.Salir \n")
  op = validarTipodeDato(op)
  if op == False:
    print("Error: Ingrese un dato válido.")
    return menuPrincipal()
  if op==1:
    return registrar()
  elif op==2:
    return ingresar()
  elif op==3:
    print("Su sesion ha finalizado correctamente")
  else:
    print("Opción no valida")
    return menuPrincipal()
  
def registrar():
  nombre = input("Ingrese su nombre ")
  if validarDatoVacio(nombre):
    print("Debe ingresar el dato requerido")
    return menuPrincipal()
  if validarCadena(nombre)== False:
    print("El nombre solo debe contener letras")
    return menuPrincipal()
  apellido = input("Ingrese su apellido ")
  if validarDatoVacio(apellido):
    print("Debe ingresar el dato requerido")
    return menuPrincipal()
  if validarCadena(apellido)== False:
    print("El apellido solo debe contener letras")
    return menuPrincipal()
  cedula = input("Ingrese su cédula ")
  if validarDatoVacio(cedula):
    print("Debe ingresar el dato requerido")
    return menuPrincipal()
  cedula = validarTipodeDato(cedula)
  if cedula == False or validarNegativo(cedula):
    print("Error: Ingrese un dato válido.")
    return menuPrincipal()
  if validarSiExiste(cedula):
    print("Ya se encuentra registrada")
    return menuPrincipal()
  edad = input("Ingrese su edad ")
  if validarDatoVacio(edad):
    print("Debe ingresar el dato requerido")
    return menuPrincipal()
  edad = validarTipodeDato(edad)
  if edad == False or validarNegativo(edad):
    print("Error: Ingrese un dato válido.")
    return menuPrincipal()
  clave = input("Ingrese una clave ")
  if validarDatoVacio(clave):
    print("Debe ingresar el dato requerido")
    return menuPrincipal()
  deposito = input("Para poder crear su cuenta, debe depositar una suma minima de 50.000, ingrese el valor que desea depositar ")
  if validarDatoVacio(deposito):
    print("Debe ingresar el dato requerido")
    return menuPrincipal()
  deposito = validarTipodeDato(deposito)
  if deposito == False:
    print("Error: Ingrese un dato válido.")
    return menuPrincipal()
  if validarValor(deposito)== False or deposito<50000:
      print("Ingrese un valor válido")
      return menuPrincipal()
  print("Cuenta creada correctamente")
  fecha = datetime.now()
  diccionario = {"nombre": nombre, "apellido": apellido, "cedula": cedula, "edad": edad, "clave": clave, 'historial' : [], "saldo" : deposito, "fecha" : fecha, "deuda" : 0}
  data.append(diccionario)
  return menuPrincipal()

def ingresar():
  cedula = input("Ingrese su cédula ")
  if validarDatoVacio(cedula):
    print("Debe ingresar el dato requerido")
    return menuPrincipal()
  cedula = validarTipodeDato(cedula)
  if cedula == False:
    print("Error: Ingrese un dato válido.")
    return menuPrincipal()
  usuario = validarSiExiste(cedula)
  if usuario == False:
    print ("No se encuentra registrado")
    return menuPrincipal()
  clave = input("Ingrese su clave ")
  if validarDatoVacio(clave):
    print("Debe ingresar el dato requerido")
    return menuPrincipal()
  if usuario["clave"] == clave:
    print ("Ingreso exitoso")
    return menuUsuario(usuario)
  print ("Datos invalidos, ingrese nuevamente")
  return menuPrincipal()
  
def menuUsuario(usuario):
  usuario['historial'].append("inició sesion")
  op = input("Ingrese una opcion \n 1.Depositar \n 2.Ver saldo \n 3.Retirar \n 4.Prestamo \n 5.Salir ")
  if validarDatoVacio(op)==True:
    print("Debe ingresar el dato requerido")
    return menuUsuario(usuario)
  op = validarTipodeDato(op)
  if op == False:
    print("Error: Ingrese un dato válido.")
    return menuPrincipal()
  if op==1:
    if validarDeuda(usuario):
      depositoDeuda(usuario)
    deposito(usuario)
  if op==2:
    print(usuario["saldo"])
    print(usuario["deuda"])
    return menuUsuario(usuario)
  if op==3:
    if validarDeuda(usuario):
      print("Tiene una deuda pendiente, no puede retirar.")
      return menuUsuario(usuario)
    retiro(usuario)
  if op==4:
    if validarDeuda(usuario):
      print("Tiene una deuda pendiente, no puede realizar otro prestamo.")
      return menuUsuario(usuario)
    prestamo(usuario)
  if op==5:
    print("chaoooooooooooo")
    return menuPrincipal()

def depositoDeuda(usuario):
  deposito = input("Digite la cantidad a depositar ")
  if validarDatoVacio(deposito):
    print("Debe ingresar el dato requerido")
    return menuUsuario(usuario)
  if validarTipodeDato(deposito):
    deposito = validarTipodeDato(deposito)
    if validarNegativo(deposito)==False:
      if validarDeuda(usuario):
        deuda = usuario["deuda"]
        op = input("Usted tiene una deuda. Ingrese el numero correspondiente \n 1.Abonar a la deuda \n 2.Enviar al capital ")
        if validarDatoVacio(op)==True:
          print("Debe ingresar el dato requerido")
          return menuUsuario(usuario)
        op = validarTipodeDato(op)
        if op == False:
          print("Error: Ingrese un dato válido.")
          return menuPrincipal()
        if op==1:
          if deposito>deuda:
            vueltos = deposito-deuda
            usuario["saldo"] += vueltos
            usuario["deuda"] = 0
            print("Transaccion realizada, su deposito era mayor a la deuda")
            return menuUsuario(usuario)
          deuda -= deposito
          usuario["deuda"] -= deposito 
          print("Abono realizado correctamente")
          return menuUsuario(usuario)
        if op==2:
          usuario['saldo'] += deposito
          print("Deposito exitoso")
          return menuUsuario(usuario)
    print("Debe ingresar un valor valido")
    return menuUsuario(usuario)
  


  

def deposito(usuario):
  deposito = input("Digite la cantidad a depositar ")
  if validarDatoVacio(deposito):
    print("Debe ingresar el dato requerido")
    return menuUsuario(usuario)
  if validarTipodeDato(deposito):
    deposito = validarTipodeDato(deposito)
    if validarNegativo(deposito)==False:
      usuario['saldo'] += deposito
      print("Deposito exitoso")
      return menuUsuario(usuario)
    print("Debe ingresar un valor valido")
    return menuUsuario(usuario)
  
def retiro(usuario):
  retiro = input("Digite la cantidad a retirar ")
  if validarDatoVacio(retiro):
    print("Debe ingresar el dato requerido")
    return menuUsuario(usuario)
  if validarTipodeDato(retiro):
    retiro = validarTipodeDato(retiro)
    if usuario["saldo"] - retiro >= 50000 and validarValor(retiro):
      usuario["saldo"] -= retiro
      print("Retiro exitoso")
      return menuUsuario(usuario)
    print("No puede retirar esa cantidad")
    return menuUsuario(usuario)
  
def prestamo(usuario):
  prestamo = input("Digite la cantidad que quiere pedir prestado")
  cupo  = usuario["saldo"] * 4
  if validarDatoVacio(prestamo):
    print("Debe ingresar el dato requerido")
    return menuUsuario(usuario)
  if validarTipodeDato(prestamo):
    prestamo = validarTipodeDato(prestamo)
    if validarValor(prestamo) and validarNegativo(prestamo)==False and prestamo<=cupo:
      print("Prestamo aprobado")
      usuario["deuda"] = (prestamo)
      return menuUsuario(usuario)
  print("Prestamo rechazado, ingrese un valor valido")
  return menuUsuario(usuario)
  
def validarDeuda(usuario):
  deuda  = usuario["deuda"]
  if deuda>0:
    return True 
  return False

def validarDatoVacio(dato):
  if not dato:
    return True
  return False  

def validarCadena(texto):
  if texto.isalpha():
    return True
  return False

def validarTipodeDato(numero):
  try:
    return int(numero)
  except:
    return False
  
def validarValor(valor):
  if valor%10000==0 and valor>0:
    return True 
  return False
  
def validarSiExiste(cedula):
  for i in data:
    if i["cedula"] == cedula:
      return i
  return False

def validarNegativo(valor):
  if valor<0:
    return True
  return False
  
menuPrincipal()