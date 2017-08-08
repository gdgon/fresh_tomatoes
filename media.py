class Movie():
    """Contains relevant information about a specific movie.

        Args:
            title: The title of the movie
            storyline: A short plot summary
            poster_image_url: URL of the movie's poster image
            trailer_youtube_url: YouTube page for the movie's trailer
    """

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
