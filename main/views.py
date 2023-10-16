from django.shortcuts import render
from django.contrib import messages
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

class IndexView(generic.FormView):
#class IndexView(generic.TemplateView, generic.FormView):
	template_name = "main/index.html"

	form_class = ContactForm

	success_url = "."

	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)

	def form_invalid(self, form):
		messages.error(self.request, 'Oh dear, please check the form and send again.')
		return super().form_invalid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		services = Service.objects.filter(is_active=True)
		about_us = AboutUs.objects.all()
		testimonials = Testimonial.objects.filter(is_active=True)
		gallery = Gallery.objects.filter(is_active=True)
		events = Event.objects.filter(is_active=True)
		chefs = Chef.objects.filter(is_active=True)
		
		context["services"] = services
		context["about_us"] = about_us
		context["testimonials"] = testimonials
		context["events"] = events
		context["chefs"] = chefs
		context["gallery"] = gallery
		return context


class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)