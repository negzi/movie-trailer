#!/bin/env python
import webbrowser

class Movie:
    """ The parent class for generating movies"""
    def __init__(self,movie_title, movie_story, poster_url, trailer_link):
        self.title = movie_title
        self.story = movie_story
        self.poster = poster_url
        self.trailer = trailer_link
    
    def show_movie_trailer(self):
        return webbrowser.open(self.trailer)
    
    def show_poster(self):
        return webbrowser.open(self.poster)
