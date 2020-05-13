
import requests

response = requests.get("https://randomuser.me/api")

def get_requests():
	response = requests.get("https://randomuser.me/api")	
	if response.status_code == 200:
		#print(response.json().get('results')) 
		results = response.json().get('results')
		return results


def get_name(results):
	name = results[0].get('name').get('first')
	return name 


def get_lastname(results):
	lastname = results[0].get('name').get('last')
	return lastname 


"""def get_country(results):
	location = results[0].get('location').get('country')
	return location"""


def get_user():
	dic = {}	
	results = get_requests()
	name = get_name()
	lastname = lastname()
	country = get_country()

	name = get_name(results)
	dic['name'] = name 
	print(dic)



for _ in range(10):
	get_user()
