#OOP Concepts 

class Songs:
    def __init__(self, song_name, origin):
        self.song_name = song_name
        self.origin = origin

    def song_detail(self):
        print(f'Song Name: {self.song_name}\nOrigin: {self.origin}')


class Song_Characteristics(Songs):
    def __init__(self, song_name, origin, type, singer):
        super().__init__(song_name, origin)
        self.type = type
        self.singer = singer

    def song_characteristecs(self):
        super().song_detail()



obj1 = Song_Characteristics('samadhi - 5:55', 'Nepal', 'Pop', 'Chirag Khadka')
obj1.song_characteristecs()