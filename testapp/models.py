from django.db import models


class TestUser(models.Model):
    name = models.CharField(max_length=200, help_text="User Name")
    email = models.EmailField(unique=True)  # email
    mobile = models.CharField(max_length=15, null=True, blank=True)  # char
    address = models.TextField(null=True, blank=True)  # email
    pincode = models.PositiveIntegerField(default=1)  # int
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
