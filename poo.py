class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self._saldo = saldo
        self._titular = titular 
        
    def depositar(self, valor):
        if valor > 0:
            self._valor += valor 
            print(f'deposito de {valor} realizado com sucesso!')
        elif valor > self._saldo:
            print('Saldo insuficiente para saque.')
        else:
            print('Valor invalido para saque.')
    
    def exibir_saldo(self):
        print(f'Saldo da conta de {self._titular}: R$ {self._saldo}.')
        

          
    
    