from time import sleep

def film_check(film):
    if film=="Ghostbusters":
        message = " - yey it's Ghostbusters"
    else:
        message = " - boo, we want Ghostbusters"
    print(film, message)
    
my_favourite_films = [
    'Shawshank Redemption',
    "The Longest Day",
    "It's a wonderful life",
    "Casablanca",
    "Ghostbusters",
    "The Big Lewbosky",
    "World War Z"
]

for film in my_favourite_films:
    film_check(film)
    
for i in range(0,10):
    print(i)
    sleep(0.2)
    
for i in range(9,-1,-1):
    print(i)
    sleep(0.2)    