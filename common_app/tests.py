from django.test import TestCase
from .models import State,City
from django.test import TransactionTestCase, Client
from django.contrib.auth.models import User
from urllib.parse import urlencode


class ApiTestCase(TestCase):

    
    def setUp(self):

        self.user = User.objects.create(username = "test1" )
        self.user.set_password ("test")
        self.user.save()
        self.state1 = State.objects.create(title = "Tehran" , code = "021")
        self.state2 = State.objects.create(title = "Esfahan" , code = "031")
        self.city1 = City.objects.create(title = "tehran" ,code = "021" , state = self.state1)
        self.client = Client()
        

    def test_get_states(self):

        response=self.client.get('/api/state', {} , True)
        self.assertEqual(len(response.json()), 2)  

    
    def test_get_cities(self):

        response=self.client.get('/api/city', {} , True)
        self.assertEqual(len(response.json()), 1)  


    def test_get_cities_of_state(self):

        response=self.client.get('/api/state/'+ str(self.state1.id), {} , True)
        self.assertEqual(len(response.json()), 1)  

        response=self.client.get('/api/state/'+ str(self.state2.id), {} , True)
        self.assertEqual(len(response.json()), 0)  