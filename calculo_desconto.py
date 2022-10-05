#Aplicar desconto em itens

item1preco = float(input("Digite o preço do item 1: "))
item2preco = float(input("Digite o preço do item 2: "))
item3preco = float(input("Digite o preço do item 3: "))

item1quantidade = int(input("Digite quantidade do item1: "))
item2quantidade = int(input("Digite quantidade do item2: "))
item3quantidade = int(input("Digite quantidade do item3: "))

subtotalrvaloresitens = (item1quantidade * item1preco) + (item2quantidade * item2preco) + (item3quantidade * item3preco)

# desconto geral ou individual?

print("Valor total da compra: " + str(subtotalrvaloresitens))

#Aplicando desconto sobre total
desconto = float(input("Digite percentual de desconto (em decimal): "))
valordesconto = subtotalrvaloresitens * desconto
totalcomdesconto = subtotalrvaloresitens - valordesconto

print("Valor do desconto: " + str(valordesconto))
print("Valor final com desconto: " + str(totalcomdesconto))





