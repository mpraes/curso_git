arquivo = open("pasta_escrever_textos/contatos.txt", "a")

novo = str(input("Insira novo contato. Nome e telefone: ") + '\n')

frases = list()
frases.append(novo)

arquivo.writelines(frases)