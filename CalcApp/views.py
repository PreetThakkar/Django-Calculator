from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def start(request):
	return render(request, 'index.html')

def calculate(request):
	q = request.GET['query']
	try:
		ans = eval(q)
		result = {
			'query': q,
			"ans": ans,
			'success': True
		}
		return render(request, 'index.html', context=result)
	except Exception as e:
		return render(request, 'index.html', context={'error':False})
	