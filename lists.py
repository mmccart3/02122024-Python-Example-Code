my_favourite_films = [
    'Shawshank Redemption',
    "The Longest Day",
    "It's a wonderful life",
    "Casablanca",
    "Ghostbusters",
    "The Big Lewbosky",
    "World War Z"
]
my_favourite_films.append("Alien")
print(my_favourite_films)
#.pop() deletes the last item in the list
#.append("item") adds a new item to the end of the list 
my_favourite_films.pop()
my_favourite_films.pop()
print(my_favourite_films)

#.remove()
my_favourite_films.remove("The Longest Day")
print(my_favourite_films)
# remove removes a named item in the list
# whereas .pop() removes a numbered item in the list by default the last item

#.reverse()
my_favourite_films.reverse()
print(my_favourite_films)
# .reverse(reverses the current order of items in a list)

#.sort()
my_favourite_films.sort()
print(my_favourite_films)
#sorts the list alphabetically

#.count()
print(my_favourite_films.count("Casablanca"))
# counts the number of times the specified item appears in a list

my_other_favorite_films = [
    "The Big Lewbosky",
    "World War Z",
    "Alien"
]

#.extend()
my_favourite_films.extend(my_other_favorite_films)
print(my_favourite_films)
# combines two lists

rainbow_colours = (
    "red",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet"
)

print(rainbow_colours)

print(rainbow_colours[3])

