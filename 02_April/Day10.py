#OOP Concepts 

class Songs:
    def __init__(self, song_name, origin):
        self.song_name = song_name
        self.origin = origin

    def song_detail(self):
        print(f'Song Name: {self.song_name}\nOrigin: {self.origin}')

obj1 = Songs('samadhi - 5:55', 'Nepal')
obj1.song_detail()