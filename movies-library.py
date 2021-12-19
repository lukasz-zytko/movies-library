class Movies:
    def __init__(self, title, year, genre, played=0):
        self.title = title
        self.year = year
        self.genre = genre
        self.played = played
    
    def __str__(self) -> str:
        return f"{self.title} ({self.year}) - obejrzany: {self.played} razy"
    
    def play(self):
        self.played += 1


class TvSeries(Movies):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self) -> str:
        return f"{self.title} S{self.season}E{self.episode} - obejrzany: {self.played} razy"


movie1 = Movies(title = "Skazani na Shawshank", year = "1994", genre = "Dramat")
movie2 = Movies(title = "Nietykalni", year = "2011", genre = "Komedia")
series1 = TvSeries(title = "Czarnobyl", year = "2019", genre = "Dramat", episode=1, season=1)
series2 = TvSeries(title = "Gra o Tron", year = "2011", genre = "Fantasy", episode=1, season=1)

movie1.play()
series1.play()
print(movie1)
print(series1)