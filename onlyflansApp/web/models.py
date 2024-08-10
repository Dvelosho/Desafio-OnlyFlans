import uuid
from django.db import models

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField("https://acortar.link/Hs3SLR")
    slug = models.SlugField()
    is_private = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)