from no import No

class ListaLigada:
    def __init__(self, capacidade = 5):
        self.head = None
        self.capacidade = capacidade
        self.count = 0

    def is_empty(self):
        return self.head is None
    
    def is_full(self):
        return self.count >= self.capacidade
    
    def add(self, valor):
        if self.is_full():
            raise Exception("A lista ligada ordenada atingiu sua capacidade máxima.")
        
        new_node = No(valor)

        if self.head is None or valor < self.head.dado:
            new_node.prox = self
            self.head = new_node
            self.count+=1
        current = self.head
        return True
    
    def remove(self, valor):
        if self.is_empty():
            raise Exception("A lista ligada ordenada está vazia.")
        
        if self.head.dado == valor:
            self.head = self.head.prox
            self.count -= 1
            return True
        

        current = self.head

        while current.prox and current.prox.dado:
            current = current.prox

        if current.prox and current.prox.dado == valor:
            current.prox = current.prox.dado
            self.count -=1
            return True
        return False
    
    def contains(self, valor):
        current = self.head
        while current:
            if current.dado == valor:
                return True
            current = current.prox
        return False
    
    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.dado)
            current = current.prox
        return values
    
    def size(self):
        return self.count




