from django.test import TestCase
from common_app.models import State,City
from django.test import TransactionTestCase, Client
from django.contrib.auth.models import User
from urllib.parse import urlencode


class ServiceTestCase(TestCase):

    
    def setUp(self):

        self.user = User.objects.create(username = "test1" )
        self.user.set_password ("test")
        self.user.save()
        self.state1 = State.objects.create(title = "Tehran" , code = "021")
        self.state2 = State.objects.create(title = "Esfahan" , code = "031")
        self.city1 = City.objects.create(title = "tehran" ,code = "021" , state = self.state1)
        self.client = Client()


    def test_send_massage(self):

        response=self.client.post( '/api/service/send/' ,
         {"city" : self.city1.id , "content" : "hello"} )
        self.assertEqual( response.status_code , 200 )