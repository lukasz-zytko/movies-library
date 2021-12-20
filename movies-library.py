from datetime import date
from random import Random
rand = Random()

class Movies:
    def __init__(self, title, year, genre, played=0):
        self.title = title
        self.year = year
        self.genre = genre
        self.played = played
    
    def __str__(self) -> str:
        return f"{self.title} ({self.year})"
    
    def play(self,step=1):
        self.played += step

class TvSeries(Movies):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self) -> str:
        return "%s S%02.0fE%02.0f" % (self.title, self.season, self.episode)

movie1 = Movies(title = "Skazani na Shawshank", year = 1994, genre = "Dramat")
movie2 = Movies(title = "Nietykalni", year = 2011, genre = "Komedia")
movie3 = Movies(title = "Zielona Mila", year = 1999, genre = "Dramat")
movie4 = Movies(title = "Ojciec Chrzestny", year = 1972, genre = "Gangsterski")
movie5 = Movies(title = "Dwunastu Gniewnych Ludzi", year = 1957, genre = "Dramat")
movie6 = Movies(title = "Forest Gump", year = 1994, genre = "Komedia")
movie7 = Movies(title = "Lot nad kukułczym gniazdem", year = 1975, genre = "Psychologiczny")
movie8 = Movies(title = "Lista Schindlera", year = 1993, genre = "Wojenny")
movie9 = Movies(title = "Pulp Fiction", year = 1994, genre = "Gangsterski")
movie10 = Movies(title = "Siedem", year = 1995, genre = "Thriller")

series1 = TvSeries(title = "Gra o Tron", year = 2011, genre = "Fantasy", episode=11, season=11)
series2 = TvSeries(title = "Czarnobyl", year = 2019, genre = "Dramat", episode=1, season=1)
series3 = TvSeries(title = "Breaking Bad", year = 2008, genre = "Kryminał", episode=1, season=1)
series4 = TvSeries(title = "Kompania Braci", year = 2001, genre = "Wojenny", episode=1, season=1)
series5 = TvSeries(title = "Biuro", year = 2005, genre = "Komedia", episode=1, season=1)
series6 = TvSeries(title = "Biuro", year = 2005, genre = "Komedia", episode=2, season=1)
series7 = TvSeries(title = "Peaky Blinders", year = 2013, genre = "Kryminał", episode=1, season=1)
series8 = TvSeries(title = "Narcos", year = 2015, genre = "Biograficzny", episode=1, season=1)
series9 = TvSeries(title = "Prawo ulicy", year = 2002, genre = "Dramat", episode=1, season=1)
series10 = TvSeries(title = "House of Cards", year = 2013, genre = "Polityczny", episode=1, season=1)

library = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10,
    series1, series2, series3, series4, series5, series6, series7, series8, series9, series10]

def library_show():
    len = 80
    print('-' * len)
    print("|                         BIBLIOTEKA FILMÓW I SERIALI                          |")
    print('-' * len)
    print("|               tytuł              |  rok   |    gatunek     | sezon | odcinek |")
    for item in sorted(library, key = lambda item: item.year, reverse=True):
        if isinstance(item, TvSeries):
            print("| %-32s |  %-6s| %-15s|   %02.0f  |    %02.0f   |" % (item.title, item.year, item.genre, item.season, item.episode))
            #print(f"{item.title}"+str((30-item.title_lenghter)*" ")+f"{item.year}\t{item.genre}"+str((15-item.genre_lenghter)*" ")+f"{item.episode}\t{item.season}")
        elif isinstance(item, Movies):
            print("| %-32s |  %-6s| %-15s|   NA  |    NA   |" % (item.title, item.year, item.genre))
            #print(f"{item.title}"+str((30-item.title_lenghter)*" ")+f"{item.year}\t{item.genre}"+str((15-item.genre_lenghter)*" ")+f"NA\tNA")
    print('-' * len)

def get_series():
    print("\n--- Lista seriali: ---")
    for item in sorted(library, key = lambda item: item.title):
        if isinstance(item, TvSeries):
            print(item)

def get_movies():
    print("\n--- Lista filmów: ---")
    for item in sorted(library, key = lambda item: item.title):
        if not isinstance(item, TvSeries):
            print(item)

def search():
    title = input("Jakiego filmu szukasz: ")
    for item in library:
        if item.title.lower() == title.lower():
            print(f"Znaleziono: {item}")

def generate_views_mulitplier(func):
    def wrapper(*args, **kwargs):
        for i in range(10):
            func(*args, **kwargs)
        print("\n.....Ludzie oglądają..............")
    return wrapper

@generate_views_mulitplier
def generate_views(seq=library):
    item = rand.choice(seq)
    item.played = rand.randint(0, 101)

def top_titles(count=3,type=None):  
    today = date.today().strftime("%d.%m.%Y")
    if type == None:
        print('\n'+70*'-')
        print(f"^^^^^^ Lista TOP {count} najlepszych filmów i seriali dnia {today} ^^^^^^")
        print(70*'-')
        for no, item in enumerate(sorted(library, key = lambda item: item.played, reverse=True)[:count]):
            print("Nr %2.0f  %-35s - liczba wyświetleń: %3.0f" % (no+1, item, item.played))
            #print(f"Nr {no+1}:\t{item}"+str((26-item.title_lenghter)*" ")+f"- liczba wyświetleń: {item.played}")
    elif type == "m":
        print('\n'+70*'-')
        print(f"^^^^^^^^^^^^^ Lista TOP {count} filmów dnia {today} ^^^^^^^^^^^^")
        print(70*'-')
        for no,item in enumerate(sorted(library, key = lambda item: item.played, reverse=True)[:count]):
            if not isinstance(item, TvSeries):
                print("Nr %2.0f  %-35s - liczba wyświetleń: %3.0f" % (no+1, item, item.played))
    elif type == "s":
        print('\n'+70*'-')
        print(f"^^^^^^^^^^^^ Lista TOP {count} seriali dnia {today} ^^^^^^^^^^^")
        print(70*'-')
        for no, item in enumerate(sorted(library, key = lambda item: item.played, reverse=True)[:count]):
            if isinstance(item, TvSeries):     
                print("Nr %2.0f  %-35s - liczba wyświetleń: %3.0f" % (no+1, item, item.played))
    print(70*'-'+'\n')

def add_series(stitle, syear, sgenre, season_no, episodes_no):
    for i in range(1, episodes_no+1):
        library.append(TvSeries(title = stitle, year = syear, genre = sgenre, episode = i, season = season_no))

#add_series("Sherlock", 2010, "kryminał", 2, 5)
library_show()
generate_views()
#search()
#get_series()
#get_movies()
#movie1.play(12)
#series1.play(98)
#series2.play(14)
top_titles()