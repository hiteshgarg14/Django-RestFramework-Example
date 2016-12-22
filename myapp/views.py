from django.shortcuts import render,redirect
from django.http import HttpResponse
from .tasks import read_all_models, update_a_model, delete_a_model, read_a_model, create_a_model
from .forms import MyModelForm

def home(request):
	content = read_all_models()
	sorted_list = sorted(content, key=lambda k: k['title'].title(), reverse = False)
	return render(request,'myapp/index.html',{'sorted_list':sorted_list})

def create(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		desc = request.POST.get('desc')
		d = {}
		d['title'] = title
		d['desc'] = desc
		if create_a_model(d):
			return redirect('myapp:home')
		else:
			return HttpResponse("Error Occured")		
	return render(request,'myapp/create.html')	

def delete(request,pk):
	if delete_a_model(pk):
		return redirect('myapp:home')
	else:
		return HttpResponse("Error Occured")	

def search(request):
	if request.method == 'POST':
		pk = request.POST.get('pk')
		try:
			content = read_a_model(pk)
		except:
			return render(request,'myapp/search.html',{'error':"No Result Found!"})		
		return render(request,'myapp/search_results.html',{'content':content})
	return render(request,'myapp/search.html')	

def update(request,pk):
	if request.method == 'POST':
		title = request.POST.get('title')
		desc = request.POST.get('desc')
		d = {}
		d['title'] = title
		d['desc'] = desc
		if update_a_model(pk,d):
			return redirect('myapp:home')
		else:
			return HttpResponse("Error Occured")
	content = read_a_model(pk)				
	return render(request,'myapp/update.html',{'content':content})	
			
