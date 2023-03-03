from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
#Para cambiar el nombre de la aplicacion
app.title = "Mi aplicacion con FastAPI"

#Para cambiar la version de la aplicacion
app.version = "0.0.1"

#los tags nos permite agrupar las rutas de la aplicacion
@app.get("/", tags=['home'])
def message():
    
    print("Hello there! Im learning FastAPI")

    return HTMLResponse('<h1> Hello World </h1>')


movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar2',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 3,
        'title': 'Avatar3',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2010',
        'rating': 7.8,
        'category': 'Action'    
    }, 
]


@app.get("/movies", tags=['movies'])
def get_movies():
    return movies

# PARAMS: 
@app.get("/movies/{id}", tags=['movies'])
def get_movies(id : int):
    result = list(filter(lambda item: item['id'] == id, movies))
    return result

# QUERY
# http://127.0.0.1:5000/movies/?category=Acci%C3%B3n
@app.get("/movies/", tags=['movies'])
def get_movies_by_query(category : str, year : str = None): 

    def query_movies(item):
        print("Category => ", category)
        print("Category => ", year)
        return item['year'] == year and item['category'] == category

    if year is None: 
        return list(filter(lambda item: item['category'] == category, movies))
    else:
        return list(filter(query_movies, movies))

