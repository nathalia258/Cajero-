from datetime import datetime
print("---------------------------------------")
print("          Bienvenido al cajero         ")
print("---------------------------------------")
data = []

def validarDeuda(usuario):
  return usuario["deuda"]>0

def validarDatoVacio(dato):
  return not dato
 
def validarCadena(texto):
  return texto.isalpha()

def validarTipodeDato(numero):
  try:
    return int(numero)
  except:
    return False
  
def validarValor(valor):
  return valor%10000==0 and valor>0
  
def validarSiExiste(cedula):
  for i in data:
    if i["cedula"] == cedula:
      return i
  return False

def validarNegativo(valor):
  return valor<0
  
def registrar():
  nombre = input("Ingrese su nombre ")
  if validarDatoVacio(nombre) or validarCadena(nombre) == False:
    print("Debe ingresar un dato valido")
    return menuPrincipal()
  
  apellido = input("Ingrese su apellido ")
  if validarDatoVacio(apellido) or validarCadena(apellido)== False:
    print("Debe ingresar un dato valido")
    return menuPrincipal()

  cedula = input("Ingrese su cédula ")
  cedula = validarTipodeDato(cedula)
  if cedula == False or validarNegativo(cedula):
    print("Debe ingresar un dato valido")
    return menuPrincipal()
  if validarSiExiste(cedula):
    print("Ya se encuentra registrada")
    return menuPrincipal()
  
  edad = input("Ingrese su edad ")
  edad = validarTipodeDato(edad)
  if edad == False or validarNegativo(edad):
    print("Debe ingresar un dato valido")
    return menuPrincipal()

  clave = input("Ingrese una clave ")
  if validarDatoVacio(clave):
    print("Debe ingresar el dato requerido")
    return menuPrincipal()
  
  deposito = input("Para poder crear su cuenta, debe depositar una suma minima de 50.000, ingrese el valor que desea depositar ")
  deposito = validarTipodeDato(deposito)
  if deposito == False or validarValor(deposito) == False or deposito<50000:
    print("Debe ingresar un dato valido")
    return menuPrincipal()
  print("---------------------------------------")
  print("      Cuenta creada correctamente      ")
  print("---------------------------------------")
  fecha = datetime.now()
  diccionario = {"nombre": nombre, "apellido": apellido, "cedula": cedula, "edad": edad, "clave": clave, 'historial' : [], "saldo" : deposito, "fecha" : fecha, "deuda" : 0}
  data.append(diccionario)
  return menuPrincipal()

def ingresar():
  cedula = input("Ingrese su cédula ")
  cedula = validarTipodeDato(cedula)
  if validarDatoVacio(cedula) or cedula == False:
    print("Debe ingresar un dato valido")
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
    usuario['historial'].append(f"inició sesion {datetime.now()}")
    return menuUsuario(usuario)
  print ("Datos invalidos, ingrese nuevamente")
  return menuPrincipal()
  
def menuPrincipal():
  print("---------------------------------------")
  print("1.Registrar\n2.Ingresar\n3.Salir")
  op = input("Selecciona una opción: ")
  print("---------------------------------------")
  op = validarTipodeDato(op)
  if op == False:
    print("Error: Ingrese un dato válido.")
    return menuPrincipal()
  if op==1:
    return registrar()
  elif op==2:
    return ingresar()
  elif op==3:
    print("Vuelva pronto")
  else:
    print("Opción no valida")
    return menuPrincipal()
  
def depositoDeuda(usuario):
  deposito = input("Digite la cantidad a depositar ")
  if validarDatoVacio(deposito):
    print("Debe ingresar el dato requerido")
    return menuUsuario(usuario)
  if validarTipodeDato(deposito):
    deposito = validarTipodeDato(deposito)
    if validarNegativo(deposito)==False and validarValor(deposito):
      if validarDeuda(usuario):
        deuda = usuario["deuda"]
        op = input("Usted tiene una deuda. \n 1.Abonar a la deuda \n 2.Enviar al capital\nIngrese el numero correspondiente: ")
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
            usuario['historial'].append(f"Depositó {deposito:,} a la deuda. Deuda saldada, el restante {vueltos} se sumó al capital {datetime.now()}")
            return menuUsuario(usuario)
          deuda -= deposito
          usuario["deuda"] -= deposito 
          print("Abono realizado correctamente")
          usuario['historial'].append(f"Abonó {deposito} a la deuda {datetime.now()}")
          return menuUsuario(usuario)
        if op==2:
          usuario['saldo'] += deposito
          print("Deposito exitoso")
          usuario['historial'].append(f"Depositó {deposito} al capital {datetime.now()}")
          return menuUsuario(usuario)
    print("Debe ingresar un valor valido")
    return menuUsuario(usuario)
  
def deposito(usuario):
  deposito = input("Digite la cantidad a depositar ")
  deposito = validarTipodeDato(deposito)
  if not deposito or validarDatoVacio(deposito) or validarNegativo(deposito) or not validarValor(deposito):
     print("Debe ingresar un valor valido")
     usuario['historial'].append(f"Hubó un error al depositar {deposito} {datetime.now()}")
     return menuUsuario(usuario)
  usuario['saldo'] += deposito
  print("Deposito exitoso")
  usuario['historial'].append(f"Depositó {deposito} al capital {datetime.now()}")
  return menuUsuario(usuario)
 
def retiro(usuario):
  retiro = input("Digite la cantidad a retirar ")
  if validarDatoVacio(retiro):
    print("Debe ingresar el dato requerido")
    return menuUsuario(usuario)
  
  retiro = validarTipodeDato(retiro)
  if usuario["saldo"] - retiro >= 50000 and validarValor(retiro):
    usuario["saldo"] -= retiro
    print("Retiro exitoso")
    usuario['historial'].append(f"Retiró {retiro} {datetime.now()}")
    return menuUsuario(usuario)
  print("No puede retirar esa cantidad")
  usuario['historial'].append(f"Falló intento de retirar {retiro} {datetime.now()}")
  return menuUsuario(usuario)
  
def prestamo(usuario):
  prestamo = input("Digite la cantidad que quiere pedir prestado: ")
  cupo  = usuario["saldo"] * 4
  if validarDatoVacio(prestamo):
    print("Debe ingresar el dato requerido")
    return menuUsuario(usuario)
  prestamo = validarTipodeDato(prestamo)
  if validarValor(prestamo) and validarNegativo(prestamo)==False and prestamo<=cupo:
    print("Prestamo aprobado")
    usuario['historial'].append(f"Realizó un prestamo de {prestamo} {datetime.now()}")
    usuario["deuda"] = (prestamo)
    return menuUsuario(usuario)
  print("Prestamo rechazado, ingrese un valor valido")
  usuario['historial'].append(f"Falló intento de prestar {prestamo} {datetime.now()}")
  return menuUsuario(usuario)

def menuUsuario(usuario):
  print("---------------------------------------")
  print("1.Depositar\n2.Ver saldo\n3.Retirar\n4.Prestamo\n5.Salir")
  op = input("Ingrese una opcion: ")
  print("---------------------------------------")
  op = validarTipodeDato(op)
  if validarDatoVacio(op)==True or op == False:
    print("Debe ingresar un dato valido")
    return menuUsuario(usuario)
  if op==1:
    if validarDeuda(usuario):
      return depositoDeuda(usuario)
    return deposito(usuario)
  if op==2:
    if validarDeuda(usuario):
      print(f"Su saldo es de: { usuario['saldo'] }" )
      print(f"Su deuda es de: {usuario['deuda']}" )
      usuario['historial'].append(f"El usuario consultó su saldo y deuda {datetime.now()}")
      return menuUsuario(usuario)
    print(f"Su saldo es de: { usuario['saldo'] }" )
    usuario['historial'].append(f"El usuario consultó su saldo {datetime.now()}")
    return menuUsuario(usuario)
  if op==3:
    if validarDeuda(usuario):
      print("Tiene una deuda pendiente, no puede retirar.")
      usuario['historial'].append(f"Error al intentar retirar, tiene una deuda pendiente {datetime.now()}")
      return menuUsuario(usuario)
    return retiro(usuario)
  if op==4:
    if validarDeuda(usuario):
      print("Tiene una deuda pendiente, no puede realizar otro prestamo.")
      usuario['historial'].append(f"Error al pedir otro prestamo, tiene una deuda pendiente {datetime.now()}")
      return menuUsuario(usuario)
    return prestamo(usuario)
  if op==5:
    print("Sesión finalizada correctamente")
    usuario['historial'].append(f"Finalizo sesion {datetime.now()}")
    for i in usuario["historial"]:
      print (i)
    usuario["historial"] = []
    return menuPrincipal()
  print("Opcion invalida")
  return menuUsuario(usuario)

menuPrincipal()
