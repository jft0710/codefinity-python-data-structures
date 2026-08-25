animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
new_animal_movies = list(animal_movies)
new_animal_movies.append("Dumbo")
new_animal_movies.append("Zootopia")
animal_movies = tuple(new_animal_movies)

print("Updated animal movies:", animal_movies)