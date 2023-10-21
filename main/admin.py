from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    Booking,
    Testimonial,
    Event,
    Chef,
    Gallery,
    Service,
    AboutUs
    )

MAX_OBJECTS = 1

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name',)
     
    # Stop backend users from creating objects for this model.
    def has_add_permission(self, request):
        if self.model.objects.count() >= 0:
            return False
        return super().has_add_permission(request)         


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name',)
     
    # Stop backend users from creating objects for this model.
    def has_add_permission(self, request):
        if self.model.objects.count() >= 0:
            return False
        return super().has_add_permission(request)         

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','is_active')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    # Allow the user to only add one object for this model.
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)    