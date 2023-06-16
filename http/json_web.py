import json
from urllib import request

url = 'https://python.bakyeono.net/data/movies.json' 
text_data = request.urlopen(url).read().decode() 
print(text_data)
print(type(text_data))

movies = json.loads(text_data)
sorted_by_year = sorted(movies,
    key = lambda t: t['year'])

print(sorted_by_year)

for movie in sorted_by_year:
    print(movie['year'], movie['title'],
        movie['genre'], movie['starring'])
    
# [
#     {
#         "title": "Interstella",
#         "genre": "SF",
#         "year": 2014,
#         "starring": ["M. McConaughey", "A. Hathaway", "J. Chastain"]
#     },
#     {
#         "title": "Braveheart",
#         "genre": "Drama",
#         "year": 1995,
#         "starring": ["M. Gibson", "S. Marceau", "P. McGoohan"]
#     },
#     {
#         "title": "Mary Poppins",
#         "genre": "Fantasy",
#         "year": 1964,
#         "starring": ["J. Andrews", "D. Van Dyke"]
#     }
# ]

# <class 'str'>
# [{'title': 'Mary Poppins', 'genre': 'Fantasy', 'year': 1964, 'starring': ['J. Andrews', 'D. Van Dyke']}, {'title': 'Braveheart', 'genre': 'Drama', 'year': 1995, 'starring': ['M. Gibson', 'S. Marceau', 'P. McGoohan']}, {'title': 'Interstella', 'genre': 'SF', 'year': 2014, 'starring': ['M. McConaughey', 'A. Hathaway', 'J. Chastain']}]
# 1964 Mary Poppins Fantasy ['J. Andrews', 'D. Van Dyke']
# 1995 Braveheart Drama ['M. Gibson', 'S. Marceau', 'P. McGoohan']
# 2014 Interstella SF ['M. McConaughey', 'A. Hathaway', 'J. Chastain']