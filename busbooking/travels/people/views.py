from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView,  View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Customer
from catalogue.models import Stop

# Create your views here.

class HomeView(TemplateView):
	template_name = 'index.html'

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	stops = Stop.objects.all()
	# 	context['stops'] = stops
	# 	return context

class CategoryView(TemplateView):
    template_name = 'category.html'

class DetailView(TemplateView):
    template_name = 'detail.html'

class CustomerView(View):
	success_url='/success'
	template_name = 'signup.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		phone_number = request.POST.get('phone')
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('pass')
		repeat_password = request.POST.get('re_pass')

		if password != repeat_password:
			messages.error(self.request, "Passwords do not Match", extra_tags='alert alert-danger')
			return render(self.request, self.template_name)

		# Create UserProfile model
		if name!="" and phone_number!="" and password!="" and email!="":
			names = name.split(" ")
			first_name = names[0]
			last_name=""
			if len(names)>0:
				last_name = names[1]
			username = first_name.lower()
			user = User.objects.create(username=username, first_name=first_name, last_name=last_name, password=password)
			Customer.objects.create(user=user, phone=phone_number)
			return redirect(self.success_url)

		return render(self.request, self.template_name)
        