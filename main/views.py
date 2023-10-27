from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import (
		Header,
		Home,
		Service,
		AboutUs,
		Booking,
		Gallery,
		Testimonial,
		Chef,
	)

from django.views import generic
from . forms import ContactForm, BookingForm

def index(request):
	form = None
     
	if request.is_ajax():
		if (request.POST['tag'] == 'bookingForm'):
			form = BookingForm(request.POST)
		elif (request.POST['tag'] == 'contactForm'):
			form = ContactForm(request.POST)

		if form.is_valid():
			form.save()		
			return JsonResponse({
                'msg': 'valid'
            })
		else:
			print(form.errors.as_data())
			return JsonResponse({'msg': 'invalid'})

	header = Header.objects.all()
	home = Home.objects.all()
	services = Service.objects.filter(is_active=True)
	about_us = AboutUs.objects.all()
	testimonials = Testimonial.objects.filter(is_active=True)
	gallery = Gallery.objects.filter(is_active=True)
	chefs = Chef.objects.filter(is_active=True)
		
	context = {
		'header': header,
		'home': home,
		'services': services,
		'about_us': about_us,
		'testimonials': testimonials,
		'gallery': gallery,
		'chefs': chefs,
	}

	return render(request, 'main/index.html', context)