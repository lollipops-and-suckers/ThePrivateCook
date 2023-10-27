from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

from .validators import validate_num_of_stars


class Header(models.Model):

    class Meta:
        verbose_name_plural = 'Header'
        verbose_name = 'Header'

    title = models.CharField(max_length=20, blank=True, null=True, verbose_name="Meta Title")
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name="Meta description")
    keywords = models.TextField(max_length=500, blank=True, null=True, verbose_name="Meta keywords")
    favicon = models.ImageField(blank=True, null=True, verbose_name="Favicon", upload_to="favicons")
    favicon_apple = models.ImageField(blank=True, null=True, verbose_name="Apple touch favicon", upload_to="favicons")


class Home(models.Model):

    class Meta:
        verbose_name_plural = 'Home'
        verbose_name = 'Home'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True, upload_to="images")
    heroImage = models.ImageField(blank=True, null=True, upload_to="heroImage")
    heroText1 = models.TextField(blank=True, null=True)
    heroText2 = models.TextField(blank=True, null=True)
    heroText3 = models.TextField(blank=True, null=True)
    heroVideoURL = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class AboutUs(models.Model):

    class Meta:
        verbose_name_plural = 'About Us'
        verbose_name = 'About Us'

    name = models.CharField(max_length=20, blank=True, null=True)
    text_top = models.TextField(blank=True, null=True)
    text_bottom = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=40, blank=True, null=True)
    contact_email = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    image_big = models.ImageField(blank=True, null=True, upload_to="AboutUsImages")
    image_small = models.ImageField(blank=True, null=True, upload_to="AboutUsImages")
    
    VideoURL = models.CharField(max_length=500, blank=True, null=True)
    mytwitterURL = models.CharField(max_length=500, blank=True, null=True)
    myfacebookURL = models.CharField(max_length=500, blank=True, null=True)
    mywhatsappURL = models.CharField(max_length=500, blank=True, null=True)
    myinstagramURL = models.CharField(max_length=500, blank=True, null=True)
    mylinkedinURL = models.CharField(max_length=500, blank=True, null=True)

    image_booking = models.ImageField(blank=True, null=True, upload_to="AboutUsImages")
    
    def __str__(self):
        return self.name

Status = (('Read', 'Read'), ('Unread', 'Unread'))


class ContactProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(verbose_name="Subject", max_length=100)
    message = models.TextField(verbose_name="Message")
    status = models.CharField(verbose_name="Status", max_length=100, null=True, choices=Status, default="Unread")

    def __str__(self):
        return f'{self.name}'


class Testimonial(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["name"]
  
    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    stars = models.IntegerField(default=1, blank=True, null=True, validators=[validate_num_of_stars])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Service(models.Model):

    class Meta:
        verbose_name_plural = 'Services'
        verbose_name = 'Service'
        ordering = ["name"]

    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="service")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Chef(models.Model):

    class Meta:
        verbose_name_plural = 'Chefs'
        verbose_name = 'Chef'
        ordering = ["name"]

    name = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    bio = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="chefs")

    twitterURL = models.CharField(max_length=500, blank=True, null=True)
    facebookURL = models.CharField(max_length=500, blank=True, null=True)
    instagramURL = models.CharField(max_length=500, blank=True, null=True)
    linkedinURL = models.CharField(max_length=500, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Booking(models.Model):

    class Meta:
        verbose_name_plural = 'Bookings'
        verbose_name = 'Booking'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(verbose_name="Phone",max_length=50)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    people = models.IntegerField(null=True, blank=True)
    message = models.TextField(verbose_name="Message")


class Gallery(models.Model):

    class Meta:
        verbose_name_plural = 'Gallery'
        verbose_name = 'Gallery'

    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="Gallery")
    is_active = models.BooleanField(default=True)