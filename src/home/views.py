from django.shortcuts import render
from .forms import SignUpForm, ContactForm

# Create your views here.
def index(request):
	title = 'Welcome'
	form = SignUpForm(request.POST or None)
	context = {
		"title" : title,
		"form" : form,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		context = {
			"title" : "thank you"
		}
	if request.user.is_authenticated():
		title = title + " " + str(request.user)

	return render(request, 'home.html', context)

def contact(request):
	form = ContactForm(request.POST or None)
	context = {
		"form": form,
	}

	return render(request, "contact.html", context)