from django.contrib import admin
from django.utils.html import format_html
from . models import (
    Header,
    Home,
    ContactProfile,
    Booking,
    Testimonial,
    Chef,
    Gallery,
    Service,
    AboutUs
    )

MAX_OBJECTS = 1

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')

    # Allow the user to only add one object for this model.
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)  

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

    # Allow the user to only add one object for this model.
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)     

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ['status']
    search_fields = ['timestamp', 'name', 'email', 'subject', 'status',]
    list_display = ('timestamp', 'name', 'email', 'subject', 'status', '_')

    def _(self, obj): # Function to change the icons (unread - read)
        if obj.status == 'Read':
            return True
        else:
            return False

    _.boolean = True

    def status(self, obj): # Functions to color the text ( unread - read)
        if obj.status == 'Read':
            color = '#80c904'
        else:
            color = 'red'
        return format_html('<strong><p style"color:{}">{}</strong>'.format(color, obj.status))    
    
    status.allow_tags = True
        
    # Stop backend users from creating objects for this model.
    def has_add_permission(self, request):
        if self.model.objects.count() >= 0:
            return False
        return super().has_add_permission(request)         

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'name', 'email')
     
    # Stop backend users from creating objects for this model.
    def has_add_permission(self, request):
        if self.model.objects.count() >= 0:
            return False
        return super().has_add_permission(request)         

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name','is_active')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','is_active')

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'is_active')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name','is_active')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

    # Allow the user to only add one object for this model.
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)    