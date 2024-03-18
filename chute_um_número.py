import random

def gerador():
  return random.randint(1,100)

def jogo():
  resposta = gerador()
  tentativa = 0 
  print("\nnumero gerado")
  
  chute = 0 
  while chute is not resposta:
    tentativa += 1 
    chute = int(input("chute um numero: "))
    if chute > resposta:
      print("menos que isso")
      
    elif chute < resposta:
        print("mais que isso")
        
    else:
        print("acertou, voce tentou" ,tentativa, "vezes")
        
while True:
  jogo()
  
