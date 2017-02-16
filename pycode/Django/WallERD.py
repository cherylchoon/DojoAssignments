from django.db import models
class Users(models.Model):
    first_name = models.Charfield(max_length=38)
    last_name = models.Charfield(max_length=38)
    email = models.Charfield(max_length=50)
    password = models.Charfield(max_length=38)
    created_at = models.DateTimeField(auto_now_add)
    updated_at = models.DateTimeField(auto_now_add)
