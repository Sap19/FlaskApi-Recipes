from run import app
import json
import unittest
import random
from os import path

class FlaskTest(unittest.TestCase):
	# Test Recipe Get Url
	def test_recipes_get(self):
		tester = app.test_client(self)
		response = tester.get("recipes")
		statusCode = response.status_code
		self.assertEqual(statusCode, 200)
		self.assertEqual(response.content_type, "application/json")

	# Test Post recipe data with a new Recipe
	def test_recipes_post_new_data(self):
		rand = str(random.randint(1, 999))
		tester = app.test_client(self)
		response = tester.post("recipes",json={
			'name': 'butteredBagels' + rand,
			'ingredients': ['1 bagel','butter'],
			'instructions': ['cut the bagel','spread butter on bagel']
		})
		statusCode = response.status_code
		json_url = path.join(app.root_path, "../data.json")
		jsonData = json.load(open(json_url))
		found = False
		for recipe in jsonData['recipes']:
			if recipe['name'] == 'butteredBagels' + rand:
				found = True
		self.assertTrue(found)
		self.assertEqual(statusCode, 201)

	# Test Post recipe data with a repeated Recipe cause it to 400
	def test_recipes_post_repeated_data(self):
		tester = app.test_client(self)
		response = tester.post("recipes",json={
			'name': 'butteredBagels',
			'ingredients': ['1 bagel','butter'],
			'instructions': ['cut the bagel','spread butter on bagel']
		})
		statusCode = response.status_code
		json_url = path.join(app.root_path, "../data.json")
		jsonData = json.load(open(json_url))
		found = False
		for recipe in jsonData['recipes']:
			if recipe['name'] == 'butteredBagels':
				found = True
		self.assertTrue(found)
		self.assertEqual(statusCode, 400)

	# Test Put recipe data and checks if it was updated
	def test_recipes_put(self):
		tester = app.test_client(self)
		response = tester.put("recipes",json={
			'name': 'butteredBagels',
			'ingredients': ['1 bagel','2tbs butter'],
			'instructions': ['cut the bagel','spread butter on bagel']
		})
		statusCode = response.status_code
		json_url = path.join(app.root_path, "../data.json")
		jsonData = json.load(open(json_url))
		found = False
		for recipe in jsonData['recipes']:
			if recipe['name'] == 'butteredBagels':
				if recipe['ingredients'] == ['1 bagel','2tbs butter']:
					found = True
		self.assertTrue(found)
		self.assertEqual(statusCode, 201)

	# Test Put recipe data thats does exsist and checks if doesnt
	def test_recipes_non_existent_put(self):
		tester = app.test_client(self)
		response = tester.put("recipes",json={
			'name': 'pasta',
			'ingredients': ['1 bagel','2tbs butter'],
			'instructions': ['cut the pasta','spread butter on pasta']
		})
		statusCode = response.status_code
		self.assertEqual(statusCode, 404)
		self.assertEqual(response.content_type, "application/json")

	# Test get recipe details data and checks if it returns data
	def test_recipes_details_get(self):
		tester = app.test_client(self)
		response = tester.get("recipes/details/butteredBagels")
		statusCode = response.status_code
		self.assertEqual(response.json['details']['name'], 'butteredBagels')
		self.assertEqual(statusCode, 200)
		self.assertEqual(response.content_type, "application/json")

if __name__ == '__main__':
	unittest.main()
