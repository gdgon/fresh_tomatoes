import fresh_tomatoes
import media


# Initialize movie list
movies = [media.Movie("The Godfather",
                      "The patriarch of an organized crime dynasty transfers"
                      " control to his reluctant son.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,704,1000_AL_.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=lLThoR1S0QQ"),

          media.Movie("The Godfather II",
                      "The early life and career of Vito Corleone in 1920s New"
                      " York is portrayed while his son, Michael, expands and"
                      " tightens his grip on the family crime syndicate.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjZiNzIxNTQtNDc5Zi00YWY1LThkMTctMDgzYjY4YjI1YmQyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,702,1000_AL_.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=8PyZCU2vpi8"),

          media.Movie("Spirited Away",
                      "During her family's move to the suburbs, a sullen"
                      " 10-year-old girl wanders into a world ruled by gods,"
                      " witches, and spirits, and where humans are changed"
                      " into beasts.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BOGJjNzZmMmUtMjljNC00ZjU5LWJiODQtZmEzZTU0MjBlNzgxL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=ByXuk9QqQkk"),

          media.Movie("Monty Python and the Holy Grail",
                      "King Arthur and his knights embark on a low-budget"
                      " search for the Grail, encountering many, very silly"
                      " obstacles.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNmNmZjViNTQtNDQ5Mi00MDYzLWI5YWMtNDUyZGNmMGZhNDg4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=LG1PlkURjxE"),

          media.Movie("Logan",
                      "In the near future, a weary Logan cares for an ailing"
                      " Professor X, somewhere on the Mexican border. However,"
                      " Logan's attempts to hide from the world, and his"
                      " legacy, are upended when a young mutant arrives,"
                      " pursued by dark forces.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQwODQwNTg4OV5BMl5BanBnXkFtZTgwMTk4MTAzMjI@._V1_.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=Div0iP65aZo"),

          media.Movie("Tropic Thunder",
                      "Through a series of freak occurrences, a group of"
                      " actors shooting a big-budget war movie are forced to"
                      " become the soldiers they are portraying.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNDE5NjQzMDkzOF5BMl5BanBnXkFtZTcwODI3ODI3MQ@@._V1_SY1000_CR0,0,711,1000_AL_.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=T-6YhRZowgc")]

# Show the movie trailer page
fresh_tomatoes.open_movies_page(movies)
