from django.db import models
from blog.models import CreatedDate


# class ContactInfo(CreatedDate):
#     address = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#     email = models.EmailField()
#     website = models.URLField()
#
#     def __str__(self):
#         return self.address


class ContactUS(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.full_name