from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
#Para cambiar el nombre de la aplicacion
app.title = "Mi aplicacion con FastAPI"

#Para cambiar la version de la aplicacion
app.version = "0.0.1"

# Class from pydantic

# Validaciones: por defecto FastAPI tiene varias validaciones por defecto: si no exite un elemento en el query o su envio el tipo de dato que no corresponde. 
class Movies (BaseModel):
    id : Optional[int]
    title: str = Field(default = "No name", min_length= 4, max_length= 5)
    overview: str
    year: int = Field(default= 2022, le= 2022) # They values need to be min or equal than 2022
    rating: float
    category: int

    class Config():
        schema_extra = {
            "defaults" : {
                "id" : 1,
                "title" : "No name",
                "overview" : "Description",
                "year": 2022,
                "rating" : 0.0,
                "category" : "No category"
            }
        }

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


@app.get("/movies", tags= ['movies'])
def get_movies():
    return movies

# PARAMS: 
@app.get("/movies/{id}", tags= ['movies'])
def get_movies(id : int):
    result = list(filter(lambda item: item['id'] == id, movies))
    return result

# QUERY
# http://127.0.0.1:5000/movies/?category=Acci%C3%B3n
@app.get("/movies/", tags= ['movies'])
def get_movies_by_query(category : str, year : str = None): 

    def query_movies(item):
        print("Category => ", category)
        print("Category => ", year)
        return item['year'] == year and item['category'] == category

    if year is None: 
        return list(filter(lambda item: item['category'] == category, movies))
    else:
        return list(filter(query_movies, movies))

@app.post("/movies", tags= ['movies'])
def create_movies(movie: Movies):
    movies.append({
        "id" : movie.id,
        "title" : movie.title,
        "overview" : movie.overview, 
        "year" : movie.year,
        "rating" : movie.rating,
        "category" : movie.category
    })
    return movies

@app.put("/movies/{id}", tags= ['movies'])
def update_movie(id:int, movie : Movies):
    
    for item in movies: 
        if item['id'] == id:
                print(item)
                item["title"] = movie.title
                item["overview"] = movie.overview 
                item["year"] = movie.year
                item["rating"] = movie.rating 
                item["category"] = movie.category
                return movies
        else:
            return "The Id there is not in DB"
    
@app.delete("/movies/{id}", tags = ['movies'])
def delete_movie(id : int): 
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return movies
 



    