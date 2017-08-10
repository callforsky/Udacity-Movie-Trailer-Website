import webbrowser

class Movie():
    """
    This class provides a way to store movie related information

    The __init__ creates an instance for each movie. Each movie is defined by 4
    attributes, as explained below.

    Attributes:
        movie_title(str): the official title of the movie
        movie_storyline(str): a sentence that summarizes the movie's story
        poster_image(str): a url that points to the box art of the movie
        trailer_youtube(str): a Youtube url that plays the trailer of the movie

    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        This function calls the webbrowser to open the movie trailer
        """
        webbrowser.open(self.trailer_youtube_url)
