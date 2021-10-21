#! /usr/bin/env python

APP_VERSION = "1.0"

class Movie:
    def __init__(self, paTitle, paYear, paGenre, paEarnings, paRating, paDuration):
        self.aTitle = paTitle
        self.aYear = paYear
        self.aGenre = paGenre
        self.aEarnings = paEarnings
        self.aRating = paRating
        self.aDuration = paDuration
    def toString(self):
        return "{:20} {} {:10} ${:4} {:3}% {3}m".format(self.aTitle, 
                                                        self.aYear, 
                                                        self.aGenre, 
                                                        self.aEarnings, 
                                                        self.aRating, 
                                                        self.aDuration)

class MovieLibrary():
    def __init__(self):
        self.aMovies = list()
    def addMovie(self, paMovie):
        self.aMovies.append()
    def removeMovie(self, paMovieIndex):
        self.aMovies.pop(paMovieIndex)
    def showLibrary(self, paPrintIndex):
        if paPrintIndex:
            indexString = " ID "
        else:
            indexString = " "
        print("{} {:20} {} {:10} {:5} {:4} {4}".format( indexString,
                                                        "Title",
                                                        "Year"
                                                        "Genre",
                                                        "Earn",
                                                        "RAT",
                                                        "Time"))
        index = 0                                                        
        for movie in self.aMovies:
            if paPrintIndex:
                indexString = "{:3} ".format(index)
            else:
                indexString = ""
            print(indexString + movie.toString())
            index += 1
            
def menu(paMovieLibrary):
    
    while True:

        print("Welcome to Movie Library v{}".format(APP_VERSION))
        print(" Add Movie (1)")
        print(" Remove Movie (2)")
        print(" Show Library Content (3)")
        print(" End the Program (q)")
        opt = input("Select one option from the menu: ")
        if(opt == "1"):
            addMovie(paMovieLibrary)
            print("Movie added")
        elif(opt == "2"):
            removeMovie(paMovieLibrary)
            print("Movie removed")
        elif(opt == "3"):
            paMovieLibrary.printLibrary(False)
        elif(opt == "q"):
            print("Bye Bye")
            exit(0)
        else:
            print("Incorrect option")
    
    
def addMovie(paMovieLibrary):
    title = input("Enter movie title: ")
    year = input("Enter year: ")
    genre = input("Enter genre: ")
    earn = input("Enter earnings in $M: ")
    rating = input("Enter rating in %: ")
    duration = input("Enter duration in minutes")

    movie = Movie(title, year, genre, earn, rating, duration)

    paMovieLibrary.addMovie(movie)

def removeMovie(paMovieLibrary):
    paMovieLibrary.printLibrary(True)

    index = input("Enter movie index for removal: ")
    paMovieLibrary.removeMovie(int(index))
    

if __name__ == "__main__":
    library = MovieLibrary
    menu(library)