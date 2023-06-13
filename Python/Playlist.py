class Song:

    def __init__(self, title):
        self.title = title
        self.next = None

class Playlist:
    def __init__(self):

        self.first_song = None
        self.last_song = None

    def is_empty(self):
        return self.first_song is None
    

    def add_in_playlist(self, title):

        new_song = Song(title)

        if self.is_empty():

            self.first_song = new_song
            self.last_song = new_song

        else:
            self.last_song.next = new_song
            self.last_song = new_song
    
    def play_next_song(self):
        if self.is_empty():
            print("A playlist está vazia.")
            return None
        
        current_song = self.first_song
        self.first_song = self.first_song.next

        

        
        

