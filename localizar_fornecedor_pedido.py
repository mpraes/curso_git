
fornecedor = int(input("Digite codigo do Fornecedor: "))

listafornecedores = [134,109,140,156]

if fornecedor in listafornecedores:
    print('Fornecedor encontrado.')
    pedido_fornecedor = fornecedor
else:
    print("Fornecedor não encontrado, tente novamente ou verifique sua base de dados")

print('Fim da busca')
