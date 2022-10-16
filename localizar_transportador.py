
transportadora = int(input("Digite CNPJ somente numeros ou Nome da Transportadora: "))

transportadora_lista = {123468345000234:'TRANSPORTADORA SIMOES LTDA',523468345000255: 'FRETES DO HABACUQUE', 673468345000278: 'ABX EXPRESS'}

for transportadora in transportadora_lista:
    if transportadora in transportadora_lista:
        print("Transportadora Encontrada")
        break
    else:
        print('Transportadora nao encontrada. tente novamente ou verifique sua base')

print('Fim do codigo')
