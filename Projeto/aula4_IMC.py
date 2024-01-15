"""nome = "darah"
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
print("Não se cobre tanto, seja feliz, do jeito que estiver se sentindo bem!") """

#Modelo: Seu IMC é imc e você está classificado como classificacao_imc





nome="Darah Leite"
peso= 74
altura=1.75
imc= peso/altura**2
classificacao_imc= str

if(imc<18.5):
    classificacao_imc= "Baixo peso"
elif(18.5<imc<24.99):
    classificacao_imc= "Normal"
elif(25<imc<29.99):
    classificacao_imc= "SobrePeso"
elif(imc>30):
    classificacao_imc= "Obesidade"
else:
    print("Erro nos dados!")


imc_alto_padrao= 21.5*altura**2
imc_baixo_padrao = 23*altura**2


linha_1= f"Olá {nome}, pelo seu peso de {peso}kg e altura de {altura}m, seu IMC é {imc:.2f}"
linha_2= f"Seu IMC está classificado como {classificacao_imc}"
linha_3= f"Para seu IMC ideal você deveria alcançar a meta de {imc_alto_padrao:.2f}, porém, creio que {imc_baixo_padrao:.2f} já estará de bom tamanho."
linha_4= f"Não se cobre tanto ;)"

print(linha_1, linha_2, linha_3, linha_4)
