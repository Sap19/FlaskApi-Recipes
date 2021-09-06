from flask import Flask, Blueprint, json, jsonify, request, make_response, current_app, url_for, current_app as app
from os import path
import json as simplejson
from flask_restful import Resource

def JsonData():
	json_url = path.join(app.root_path, "../data.json")
	return json.load(open(json_url))

class RecipesAPI(Resource):
	def post(self):
		newRecipe = request.get_json()
		jsonData = JsonData()
		for recipe in jsonData['recipes']:
			if recipe['name'] == newRecipe['name']:
				responseObject = {
					"error": "Recipe already exists"
				}
				return make_response(jsonify(responseObject)), 400
		jsonData['recipes'].append(newRecipe)
		with open('data.json', 'w') as outfile:
			json.dump(jsonData, outfile)
		return make_response(), 201
	def get(self):
		jsonData = JsonData()
		recipeNames = []
		for recipe in jsonData['recipes']:
			recipeNames.append(recipe['name'])
		responseObject = {
			'recipeNames': recipeNames
		}
		return make_response(jsonify(responseObject)), 200
	def put(self):
		recipeToEdit = request.get_json()
		isEdit = False
		jsonData = JsonData()
		for recipe in jsonData['recipes']:
			if recipe['name'] == recipeToEdit['name']:
				recipe['instructions'] = recipeToEdit['instructions']
				recipe['ingredients'] = recipeToEdit['ingredients']
				isEdit = True
		if isEdit:
			with open('data.json', 'w') as outfile:
				json.dump(jsonData, outfile)
			return make_response(), 201
		responseObject = {
			"error": "Recipe does not exist"
		}
		return make_response(jsonify(responseObject)), 404

class RecipesDetailsAPI(Resource):
	def get(self, recipeName):
		jsonData = JsonData()
		recipeDetails = {}
		for recipe in jsonData['recipes']:
			if recipeName == recipe['name']:
				recipeDetails = recipe
		responseObject = {
			'details': recipeDetails
		}
		return make_response(jsonify(responseObject)), 200
