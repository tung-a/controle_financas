class Financa:
    def __init__(self, descricao, valor, observacoes):
        self.descricao = descricao
        self.valor = valor
        self.observacoes = observacoes

    
    def get_descricao(self):
        return self.descricao
    
    
    def get_valor(self):
        return self.valor
    

    def get_observacoes(self):
        return self.observacoes
    

    def set_descricao(self, descricao):
        self.descricao = descricao


    def set_valor(self, valor):
        self.valor = valor
    
    
    def set_observacoes(self, text):
        self.observacoes = text
    

class Entrada(Financa):
    def __init__(self, descricao, valor, observacoes, origem):
        super().__init__(descricao, valor, observacoes)
        self.origem = origem

    
    def get_origem(self):
        return self.origem
    
    
    def set_origem(self, origem):
        self.origem = origem

class Saida(Financa):
    def __init__(self, descricao, valor, observacoes, data_vencimento, data_pagamento):
        super().__init__(descricao, valor, observacoes)
        self.data_vencimento = data_vencimento
        self.data_pagamento = data_pagamento

    
    def get_data_vencimento(self):
        return self.data_vencimento
    
    
    def get_data_pagamento(self):
        return self.data_pagamento
    
    
    def set_data_vencimento(self, data):
        self.data_vencimento = data
    

    def set_data_pagamento(self, data):
        self.data_pagamento = data