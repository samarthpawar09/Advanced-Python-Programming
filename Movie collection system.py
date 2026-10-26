
import csv
import re

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    movies = list(reader)

print("All Movie Information:")
for movie in movies:
    print(movie)

keyword = input("\nEnter movie title keyword: ")

print("\nMatching Movies:")
found = False

for movie in movies:
    if re.search(re.escape(keyword), movie["Title"], re.IGNORECASE):
        print(movie)
        found = True

if not found:
    print("No matching movies found.")