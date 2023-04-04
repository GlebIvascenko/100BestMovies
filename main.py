import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

movie_titles = []

all_movies = soup.find_all(name='h3', class_='title')

movie_title = [movie.getText() for movie in all_movies]
movies = movie_title[::-1]


with open("movies.txt", mode="w") as file:
    for movie in movies:
        movie = movie.encode('ascii', 'ignore').decode('ascii')
        file.write(f"{movie}\n")

