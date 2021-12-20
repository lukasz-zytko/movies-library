from random import Random
rand = Random()

class Movies:
    def __init__(self, title, year, genre, played=0):
        self.title = title
        self.year = year
        self.genre = genre
        self.played = played
    
    def __str__(self) -> str:
        return f"{self.title} ({self.year}) - liczba odtworzeń: {self.played}"
    
    def play(self,step=1):
        self.played += step
    
    @property
    def title_lenghter(self):
        title_lenght = len(self.title)
        return title_lenght

class TvSeries(Movies):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self) -> str:
        return f"{self.title} S{self.season}E{self.episode} - liczba odtworzeń: {self.played}"

movie1 = Movies(title = "Skazani na Shawshank", year = "1994", genre = "Dramat")
movie2 = Movies(title = "Nietykalni", year = "2011", genre = "Komedia")
movie3 = Movies(title = "Zielona Mila", year = "1999", genre = "Dramat")
movie4 = Movies(title = "Ojciec Chrzestny", year = "1972", genre = "Gangsterski")
movie5 = Movies(title = "Dwunastu Gniewnych Ludzi", year = "1957", genre = "Dramat Sądowy")
series1 = TvSeries(title = "Gra o Tron", year = "2011", genre = "Fantasy", episode=1, season=1)
series2 = TvSeries(title = "Czarnobyl", year = "2019", genre = "Dramat", episode=1, season=1)
series3 = TvSeries(title = "Breaking Bad", year = "2008", genre = "Kryminał", episode=1, season=1)
series4 = TvSeries(title = "Kompania Braci", year = "2001", genre = "Wojenny", episode=1, season=1)
series5 = TvSeries(title = "Biuro", year = "2005", genre = "komedia", episode=1, season=1)

library = [movie1, movie2, movie3, movie4, movie5, series1, series2, series3, series4, series5]
series_library = []
movies_library = []

def get_series():
    print("--- Lista seriali: ---")
    for item in library:
        if isinstance(item, TvSeries):
            series_library.append(item)
    for item in sorted(series_library, key = lambda item: item.title):
        print(item)

def get_movies():
    print("--- Lista filmów: ---")
    for item in library:
        if not isinstance(item, TvSeries):
            movies_library.append(item)
    for item in sorted(movies_library, key = lambda item: item.title):
        print(item)

def search():
    title = input("Jakiego filmu szukasz: ")
    for item in library:
        if item.title.lower() == title.lower():
            print(item)

#def generate_views_mulitplier():


def generate_views(seq=library):
    item = rand.choice(seq)
    item.played = rand.randint(0, 101)



generate_views()
#movie2.play()
#movie1.play(12)
#series1.play(98)
#series2.play(14)
get_series()
get_movies()
#search()
#print([rand.randint(0, 101), rand.randint(0, 101), rand.randint(0, 101)])
#print(rand.choice(library))

#print(dir(rand))

#for item in library:
#    if isinstance(item, TvSeries):
#        print(f"{item.title}"+str((25-item.title_lenghter)*" ")+f"{item.year}\t{item.genre}\t{item.episode}\t{item.season}\t{item.played}")
#    elif isinstance(item, Movies):
#        print(f"{item.title}"+str((25-item.title_lenghter)*" ")+f"{item.year}\t{item.genre}\tNa\tNA\t{item.played}")
#movie1.play()
#series1.play()
#print(movie1)
#print(series1)