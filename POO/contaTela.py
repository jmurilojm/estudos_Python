from conta import Conta,Cliente,Historico

cliente_1 = Cliente('Jose','Murilo',7377062444)
conta_1 = Conta('288-7',cliente_1,4500)

cliente_2 = Cliente('Jessica','Poliana',9279068482)
conta_2 = Conta('249-1',cliente_2,1500)


conta_1.extrato()
conta_1.depositar(56)
conta_1.transferir_para(conta_2,630)
conta_2.sacar(225)

conta_1.historico.imprime()
conta_2.historico.imprime()