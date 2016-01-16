from django.shortcuts import redirect, render
from django.http import HttpResponse
import unirest

def home_page(request):

    return HttpResponse('<h1>Home Page</h1>')

def recipe_list(request):
    response = unirest.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?ingredients=apples%2Cflour%2Csugar&number=5",
      headers={
        "X-Mashape-Key": "QN5CLcAiQXmshOrib4vl7QifQAPjp1MjXoijsnsKdgztp93FnI",
        "Accept": "application/json"
      }
    )

    context = {
        'response': response
    }

    return render(request, 'recipes_list.html', context)
