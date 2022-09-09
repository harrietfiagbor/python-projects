import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.imdb.com/list/ls055592025/")
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, 'html.parser')
# print(soup.prettify())

movie_list = [tag.getText() for tag in soup.select(selector="h3 a")]
# print(movie_list)

with open("movie.txt", "w") as movie_file:
    number = 1
    for movie in movie_list:
        movie_file.write(f"{number}) {movie}\n")
        number += 1
