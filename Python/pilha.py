class Pilha:
    def __init__(self, max_size=None):
        self.topo = None
        self.tamanho = 0
        self.max_size = max_size

    def is_empty(self):
        return self.tamanho == 0

    def push(self, valor):
        if self.max_size is not None and self.tamanho == self.max_size:
            return False

        novo_no = No(valor)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self.tamanho += 1
        return True

    def pop(self):
        if self.is_empty():
            return None

        valor = self.topo
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return valor

    def peek(self):
        if self.is_empty():
            return None

        return self.topo

    def list_items(self):
        if self.is_empty():
            return ['Topo da Pilha:\n', 'Base da Pilha\n']

        valores = []
        no_atual = self.topo
        while no_atual:
            valores.append(str(no_atual.dado) + '\n')
            no_atual = no_atual.proximo

        valores.insert(0, 'Topo da Pilha:\n')
        valores.append('Base da Pilha\n')
        return valores

    def get_size(self):
        return self.tamanho