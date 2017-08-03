import media
import fresh_tomatoes

# List movies that to display on the website
# Each movie has 4 attributes: name, brief, box art, trailer url
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

titanic = media.Movie("Titanic",
                      "a love story on a sinking ship",
                      "https://t0.gstatic.com/images?q=tbn:ANd9GcQhYjUIu2o5v5u3rfJpCq5Cz0Q9WK--XdYxai_N2d0ImohPiIOp",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

interstellar = media.Movie("Interstellar",
                           "a team of pioneers undertakes a mission to find a new earth for humans",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=8EdxTFS3fD0")

rogue_one = media.Movie("Rogue One: A Star Wars Story",
                        "a group of unlikely heroes band together to steal the blueprint of the Death Star",
                        "http://cdn3-www.comingsoon.net/assets/uploads/gallery/star-wars-rogue-one/cwq_ccexuauhczm.jpg",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

king_kong = media.Movie("Kong: Skull Island",
                        "a team of explorers explored an uncharted island, the home of a mythic King Kong",
                        "http://api.comingsoon.net//images//2017/poster_57517_1486991879.jpg",
                        "https://www.youtube.com/watch?v=ddOTWvzk7IY")

# make sure you update the movie variable in the movies list!
# the item in the movies list should match the movie variables you list above
movies = [toy_story, avatar, titanic, interstellar, rogue_one, king_kong]

# the code below calls the fresh_totamotes script to produce a new html
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)

# print(toy_story.storyline)
# print(avatar.storyline)
# avatar.show_trailer()
# titanic.show_trailer()
