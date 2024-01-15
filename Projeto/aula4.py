nome = "darah"
altura = 1.75
peso= 74
imc= peso/(altura**2)                  #peso/(altura)²
meta_alta= 21*(altura**2)
meta_baixa = 22.5*(altura**2)

print("Seu IMC é ", imc)
print("")

if(imc<18.5):
    print("BAIXO PESO")

elif(18.5<imc<24.99):
    print("NORMAL")

elif(25<imc<29.99):
    print("SOBREPESO")

elif(imc>30):
    print("OBESIDADE")

print("")

print("Sua META Alta é chegar a ", meta_alta)
print("")
print("Entretanto, creio que ", meta_baixa , "já está ótimo")
print("")
print("Não se cobre tanto, seja feliz, do jeito que estiver se sentindo bem!")