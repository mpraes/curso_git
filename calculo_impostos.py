
valorunitarioproduto = (float(input("Informe valor unitario do produto adquirido: ")))
quantidadeproduto = int(input("informe quantidade adquirida do produto: "))

ipi = float(input("informe percentual do IPI: "))/100
icms = float(input("informe percentual do ICMS: "))/100
pis_cofins = float(input("informe percentual do pis/cofins: "))/100

calculoproduto = (valorunitarioproduto * quantidadeproduto)
calculoipi = valorunitarioproduto * ipi
calculoicms = valorunitarioproduto * icms
pis_cofins = valorunitarioproduto * pis_cofins
somaimpostos = calculoicms + calculoipi + pis_cofins * quantidadeproduto

print("O total de impostos pagos: " + str(somaimpostos))

