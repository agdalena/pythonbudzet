from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    category_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.category_name

#class Account(models.Model):
#    login = models.CharField(max_length=100)
#    password = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.login

class Transaction(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    value = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='0')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __unicode__(self):
        return self.title

class Mail(models.Model):
    adress = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=300)

    def __unicode__(self):
        return self.message

class Filter(models.Model):
    dateStart = models.DateField()
    dateEnd = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='0')

    def __unicode__(self):
        return self.user


