arquivo = open("texts/contatos.txt", "a")

novo = str(input("Insira novo contato. Nome e telefone: "))

frases = list()
frases.append(novo)

arquivo.writelines(frases)