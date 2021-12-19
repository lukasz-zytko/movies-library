class Movies:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        
        #variables
        self.watched = 0
    
    def __str__(self) -> str:
        return f"{self.title} ({self.year}"

Movie1 = Movies(title = "Skazani na Shawshank", year = "1994", genre = "Dramat")

print(Movie1)
