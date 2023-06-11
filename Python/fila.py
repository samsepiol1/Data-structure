from no import No
class Fila:
    def __init__(self, max_size=None):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0
        self.max_size = max_size

    def is_empty(self):
        return self.tamanho == 0

    def is_full(self):
        return self.max_size is not None and self.tamanho == self.max_size

    def enqueue(self, valor):
        if self.is_full():
            raise Exception("A fila está cheia")

        novo_no = No(valor)

        if self.is_empty():
            self.primeiro = novo_no
        else:
            self.ultimo.proximo = novo_no

        self.ultimo = novo_no
        self.tamanho += 1
        return True

    def dequeue(self):
        if self.is_empty():
            raise Exception("A fila está vazia")

        valor = self.primeiro
        self.primeiro = self.primeiro.proximo
        self.tamanho -= 1

        if self.is_empty():
            self.ultimo = None

        return valor

    def peek_first(self):
        if self.is_empty():
            return None

        return self.primeiro

    def peek_last(self):
        if self.is_empty():
            return None

        return self.ultimo
    
    def display(self):
            if self.is_empty():
                return []
            valores = []
            no_atual = self.primeiro
            while no_atual:
                valores.append(no_atual.dado)
                no_atual = no_atual.proximo
            return valores

    def size(self):
        return self.tamanho