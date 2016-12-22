import requests


def read_all_models():
	r = requests.get("http://localhost:8000/mymodels/")
	return r.json()	

def update_a_model( pk , new_data): 
	r = requests.put("http://localhost:8000/make/"+ pk + "/", data=new_data)
	return r.json()

def delete_a_model(pk):
	r = requests.delete("http://localhost:8000/make/"+ pk + "/")
	return True

def read_a_model(pk):
	r = requests.get("http://localhost:8000/make/"+ pk + "/")
	return r.json()

def create_a_model(new_data):
	r = requests.post("http://localhost:8000/mymodels/",data=new_data)
	return True