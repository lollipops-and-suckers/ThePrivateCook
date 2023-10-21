from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import (
		UserProfile,
		Service,
		AboutUs,
		Booking,
		Gallery,
		Testimonial,
		Event,
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
		
	services = Service.objects.filter(is_active=True)
	about_us = AboutUs.objects.all()
	testimonials = Testimonial.objects.filter(is_active=True)
	gallery = Gallery.objects.filter(is_active=True)
	events = Event.objects.filter(is_active=True)
	chefs = Chef.objects.filter(is_active=True)
		
	context = {
		'services': services,
		'about_us': about_us,
		'testimonials': testimonials,
		'gallery': gallery,
		'events': events,
		'chefs': chefs,
	}

	return render(request, 'main/index.html', context)