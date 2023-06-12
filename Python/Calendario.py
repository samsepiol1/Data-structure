class Dia:
    def __init__(self, numero):
        self.numero = numero
        self.proximo = None


class Calendario:


    def __init__(self, ano, mes):
        self.ano = ano
        self.mes = mes
        self.primeiro_dia = None
        self.count = 0

    def is_full(self):
        return self.count <= 31

    def adicionar_dia(self, numero):

        if self.is_full():
                raise Exception("Calendário com número de dias inexistentes")
        
        novo_dia = Dia(numero)

        if self.primeiro_dia is None:
            self.primeiro_dia = novo_dia
        else:
            atual = self.primeiro_dia
            while atual.proximo is not None:
                atual = atual.proximo
                self.count+=1
            atual.proximo = novo_dia

            

    def remover_dia(self, numero):
        if self.is_full():
            raise Exception("Calendário com número de dias inexistentes")
        
        if self.primeiro_dia.numero == numero:
            self.primeiro_dia = self.primeiro_dia.proximo
        
        else:
            anterior = self.primeiro_dia
            atual = self.primeiro_dia.proximo

            while atual is not None:
                if atual == numero:
                    anterior.proximo = atual.proximo
                    break
                anterior = atual
                atual = anterior.proximo

    




    def obter_dias(self):
        dias = []

        atual = self.primeiro_dia
        while atual is not None:
            dias.append(atual.numero)
            atual = atual.proximo

        return dias

# Exemplo de uso
cal = Calendario(2023, 6)  # Cria um calendário para o mês de junho de 2023
cal.adicionar_dia(1)  # Adiciona o dia 1 ao calendário
cal.adicionar_dia(2)  # Adiciona o dia 2 ao calendário
dias = cal.obter_dias()  # Obtém a lista de dias do calendário
print(dias)
