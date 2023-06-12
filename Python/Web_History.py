class Page:
    def __init__(self, url):

        # Informação que será inserida
        self.url = url

        # Aponta para o próxima pagina
        self.next = None

class WebHistory():

    def __init__(self):
        self.last_access = None
        self.tamanho = 0


    def is_empty(self):
        return self.tamanho == 0

    def add_page(self, url):

        new_page = Page(url)

        new_page.next = self.last_access

        self.last_access = new_page

    
    def remove_page(self, url):

        if self.is_empty():
            return None
        
        page_delete = self.last_access

        self.last_access = self.last_access.next

        page_delete.next = None
        
        



    def display_webhistory(self):
        current_page = self.last_access

        while current_page is not None:
            print(current_page.url)
            current_page = current_page.next

# Exemplo de uso
history = WebHistory()
history.add_page("https://www.google.com")
history.add_page("https://www.openai.com")
history.add_page("https://www.github.com")
history.display_webhistory()

        


      


