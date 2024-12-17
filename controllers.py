from models import Entrada, Saida

financas = []

def adicionar_entrada(descricao, valor, observacoes, origem):
    financa = Entrada(descricao, valor, observacoes, origem)
    financas.append(financa)
    print("Entrada adicionado com sucesso!")


def adicionar_saida(descricao, valor, observacoes, data_vencimento, data_pagamento):
    financa = Saida(descricao, valor, observacoes, data_vencimento, data_pagamento)
    financas.append(financa)
    print("Saida adicionado com sucesso!")


def listar_financas():
    for i, financa in enumerate(financas, 1):
        if isinstance(financa, Entrada):
            print(f"{i}. Descrição: {financa.get_descricao()}, Valor: {financa.get_valor()}, Observações: {financa.get_observacoes()}, Origem: {financa.get_origem()}")
        elif isinstance(financa, Saida):
            print(f"{i}. Descrição: {financa.get_descricao()}, Valor: {financa.get_valor()}, Observações: {financa.get_observacoes()}, Data vcto: {financa.get_data_vencimento()}, Data pgto: {financa.get_data_pagamento()}")
        else:
            print(f"{i}. Descrição: {financa.get_descricao()}, Valor: {financa.get_valor()}, Observações: {financa.get_observacoes()}")


def atualizar_financa(index):
    if 0 <= index < len(financas):
        if isinstance(financas[index], Entrada):
            atributo = input("Digite o atributo de uma entrada que deseja alterar: ")
            if atributo == "Descrição":
                descricao = input("Digite a nova descrição: ")
                financas[index].set_descricao(descricao)
            elif atributo == "Valor":
                valor = input("Digite o novo valor: ")
                financas[index].set_valor(valor)
            elif atributo == "Observações":
                observacoes = input("Digite as novas observacoes: ")
                financas[index].set_observacoes(observacoes)
            elif atributo == "Origem":
                origem = input("Digite a nova origem: ")
                financas[index].set_origem(origem)
            else:
                print("Atributo inválido!")
                return
        elif isinstance(financas[index], Saida):
            atributo = input("Digite o atributo de uma saida que deseja alterar: ")
            if atributo == "Descrição":
                descricao = input("Digite a nova descrição: ")
                financas[index].set_descricao(descricao)
            elif atributo == "Valor":
                valor = input("Digite o novo valor: ")
                financas[index].set_valor(valor)
            elif atributo == "Observações":
                observacoes = input("Digite as novas observacoes: ")
                financas[index].set_observacoes(observacoes)
            elif atributo == "Data pgto":
                data = input("Digite a nova data de pagamento: ")
                financas[index].set_data_pagamento(data)
            elif atributo == "Data vcto":
                data = input("Digite a nova data de vencimento: ")
                financas[index].set_data_vencimento(data)
            else:
                print("Atributo inválido!")
                return
        else:
            print("Tipo de finança inválido!")
            return
        print("Finança atualizado!")
    else:
        print("Índice inválido!")


def remover_financa(index):
    if 0 <= index < len(financas):
        financas.pop(index)
        print("Finança removida!")
    else:
        print("Índice inválido!")