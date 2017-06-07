from django.test import TestCase
from django.contrib.auth.models import User
from .models import Transaction
from .models import Category

# Create your tests here.

def get_accounts_succes(self,client):
    response = client.get('/accounts')
    assert response.status_code == 200

