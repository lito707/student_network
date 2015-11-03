from django.shortcuts import render

# Create your views here.
def home(request):
	"""
	Render the home template
	"""
	template  = "home.html"
	return render(request, template)
