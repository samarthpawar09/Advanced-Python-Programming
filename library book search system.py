
import csv
import re

with open("books.csv", "r") as file:
    reader = csv.DictReader(file)
    books = list(reader)

print("All Book Details:")
for book in books:
    print(book)

keyword = input("\nEnter book title keyword: ")

print("\nMatching Books:")
found = False

for book in books:
    if re.match(keyword, book["Title"], re.IGNORECASE):
        print(book)
        found = True

if not found:
    print("No matching books found.")
