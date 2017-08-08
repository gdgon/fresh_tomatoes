class Movie():
    """Contains relevant information about a specific movie.

        Args:
            title (str): The title of the movie
            storyline (str): A short plot summary
            poster_image_url (str): URL of the movie's poster image
            trailer_youtube_url (str): YouTube page for the movie's trailer

        Attributes:
            title (str): The title of the movie
            storyline (str): A short plot summary
            poster_image_url (str): URL of the movie's poster image
            trailer_youtube_url (str): YouTube page for the movie's trailer

    """

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
