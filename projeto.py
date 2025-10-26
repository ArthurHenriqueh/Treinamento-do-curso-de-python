#Projeto fatiamento
nome=input("Qual seu nome?");print("Ao contrario:",nome[::-1]);print("Primeira letra:",nome[0]);print("Ultima letra:",nome[-1]); 
if ' ' in nome: print("Tem espaco"); 
else: print("Nao tem")
print("Numero de letras:",len(nome))
