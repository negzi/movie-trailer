from  media import Movie
import fresh_tomatoes

""" This module is responsible for instantiating the movies inherited from the media"""

spectre = Movie("Spectre", 
                "James bond movie",
                "http://cdn0.theawl.com/wp-content/uploads/2015/09/CN_YqmzWEAEExOx.jpg-large.jpeg",
                "https://www.youtube.com/watch?v=7GqClqvlObY")

darknight = Movie("Dark_nieght", 
          "Batman movie",
          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [spectre, darknight]

fresh_tomatoes.open_movies_page(movies)
