import PracticaPair

def test_PedirTotales_NmayoraX():
  N,X = PracticaPair.PedirTotales([8,2])
  if(N>=X):
      test= False
  else:
    test = True    
  assert test == True

def test_PedirTotales_NmenorX():
  N,X = PracticaPair.PedirTotales([2,8])
  if (N>=X):
    test = False
  else:
    test = True
  assert test == False

def test_PedirTotales_StringNumero():
  N,X = PracticaPair.PedirTotales(["Tres",2])
  e = None
  try: 
    print(N+X)
  except Exception as e: 
    print("Solo se aceptan numeros")
  assert e == None

def test_PedirTotales_NumeroString():
  N,X = PracticaPair.PedirTotales([2, "Uno"])
  e = None
  try:
    print (N+X)
  except Exception as e:
    print("Solo se aceptan numeros")
  assert e == None

def test_PedirTotales_String():
  N,X = PracticaPair.PedirTotales(["Tres", "Uno"])
  e = None
  try:
    int(N+X)
  except Exception as e:
    print("Solo se aceptan numeros")
  assert e == 'can only concatenate str (not "int") to str'

def test_PedirTotales_Int():
  N,X = PracticaPair.PedirTotales([8,2])
  e = None
  e= N+X
  assert e == 10

def test_Validar1():
  lista = [["asd",3],["psd",1],["papa",3]]
  pasar = PracticaPair.validar1(lista)
  assert pasar == False

def test_Validar5():
  lista = [["asd",3],["psd",6],["papa",3]]
  pasar = PracticaPair.validar5(lista)
  assert pasar == False




    


    
