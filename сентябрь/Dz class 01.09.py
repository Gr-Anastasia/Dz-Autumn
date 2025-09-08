class Song:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

class Album:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.music = list()

    def add_song(self, song):
        self.music.append(song)

    def get_song(self):
        return [f" Название: {song.name} | Автор: {song.author}" for song in self.music]


    def get_uniq_author(self):
        uniq_author = set()
        for song in self.music:
            uniq_author.add(song.author)
        return uniq_author

    def find_song(self, ms):
        if ms in self.music:
            return True
        else:
            return False

class MusicLibrary:
    def __init__(self):
        self.album = list()

    def add_album(self, album):
        self.album.append(album)

    def get_author_album(self, author):
        author_songs = set()
        for album in self.album:
            for song in album.music:
                if song.author == author:
                    author_songs.add(song)
        return [song.name for song in author_songs]


    def get_uniq_music_album(self):
        music_set = []
        for album in self.album:
            y = set(album.music)
            music_set.append(y)
        uniq_music = set.intersection(*music_set)
        return [music.name for music in uniq_music]

song_1 = Song("Smile", "Wolf Alice", "2021")
song_2 = Song("Love Story", "KUTE", "2025")
song_3 = Song("Rock That Body", "Black Eyed Peas", "2010")
song_4 = Song("Storms", "Wolf Alice", "2014")

album_1 = Album("Fovorits", "2025")
album_2 = Album("Party", "2022")
album_3 = Album("The road", "2018")

favorits_album = MusicLibrary()

album_1.add_song(song_1)
album_1.add_song(song_2)
album_1.add_song(song_3)
album_2.add_song(song_1)
album_2.add_song(song_3)
album_2.add_song(song_4)
album_3.add_song(song_3)

favorits_album.add_album(album_1)
favorits_album.add_album(album_2)
favorits_album.add_album(album_3)

print("Песни в альбоме", album_1.get_song())
print("Песни в альбоме: ", album_2.get_song())
print("Уникальные авторы в альбоме: ", album_2.get_uniq_author())
print("Поиск 3 песни в альбоме: ", album_2.find_song(song_3))
print("Поиск 2 песни в альбоме: ", album_2.find_song(song_2))

print("Все песни автора KUTE: ", favorits_album.get_author_album(song_2.author))
print("Песня song_3 во всех альбомов: ", favorits_album.get_uniq_music_album())



