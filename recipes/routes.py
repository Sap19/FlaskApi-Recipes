from flask import Flask, Blueprint, jsonify, request, make_response, current_app

from recipes.resources import (
	RecipesAPI,
	RecipesDetailsAPI
)

recipes = Blueprint("recipes", __name__)

recipes_view = RecipesAPI.as_view("recipes_api")
recipes_details_view = RecipesDetailsAPI.as_view("recipes_details_api")

recipes.add_url_rule(
	"/recipes/details/",
	defaults={'recipeName': None},
	view_func=recipes_details_view,
	methods=["GET"]
)
recipes.add_url_rule(
	"/recipes/details/<string:recipeName>",
	view_func=recipes_details_view,
	methods=["GET"]
)

recipes.add_url_rule(
	"/recipes",
	view_func=recipes_view,
	methods=["GET", "POST", "PUT"]
)
