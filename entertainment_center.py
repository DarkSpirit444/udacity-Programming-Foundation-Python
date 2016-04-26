import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
			"A story of a boy and his toys that come to life",
			"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
		     "A marine on an alien planet",
		     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

kfpanda = media.Movie("Kung Fu Panda 3",
                     "Po reunites with his long-lost father",
                     "http://tinyurl.com/grf5m5r",
                     "https://youtu.be/H-30B0cqh88")
#kfpanda.show_trailer()

movies = [ toy_story, avatar, kfpanda ]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
