# Pantryplate Project 
# By: Ali Asghar 

# Flask Application 
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Home Route - Displays the search form
@app.route('/')
def home():
    return render_template('index.html')

# Recipe Search Route - Handles form submission, queries Spoonacular API, and returns recipes
@app.route('/recipes', methods=['POST'])
def get_recipes():
    # Getting user input from the form
    ingredients = request.form.get('ingredients')  # e.g., "tomato, onion"
    cuisine = request.form.get('cuisine')         # e.g., "Italian"
    diet = request.form.get('diet')               # e.g., "vegetarian"

    # Spoonacular API setup
    api_url = "https://api.spoonacular.com/recipes/complexSearch"
    api_key = "f498348e93334cc486e380d128b6e1c0"  # Replace with your actual API key from Spoonacular
    params = {
        "apiKey": api_key,
        "includeIngredients": ingredients,
        "cuisine": cuisine,
        "diet": diet,
        "number": 15  # Limit to 5 results
    }

    # Make the request to the API
    response = requests.get(api_url, params=params)
    data = response.json()
    recipes = data.get('results', [])

    # Pass the recipes to the template for rendering
    return render_template('recipes.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)
