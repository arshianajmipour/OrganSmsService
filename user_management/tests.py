from django.test import TestCase
from django.test import TransactionTestCase, Client
from user_management.forms import LoginForm
from django.contrib.auth.models import User
from urllib.parse import urlencode


class UserManagementTestCase(TestCase):

    
    def setUp(self):

        self.form = LoginForm
        self.superuser = User.objects.create(username = "test1" )
        self.superuser.set_password ("test")
        self.superuser.save()
        self.superuser.is_staff = True
        self.superuser.is_superuser=True
        self.superuser.save()
        self.user2 = User.objects.create(username = "test2" )
        self.user2.set_password ("test")
        self.user2.save()
        self.client = Client()
        

    def test_correct_data_login_super_user(self):

        data = {
            "username" : "test1",
            "password" : "test",
            "captcha_0" : "XXXX",
            "captcha_1" : "PASSED",
        }
        form = self.form(data = data)
        
        self.assertTrue(form.is_valid())
        self.client.login(username=self.superuser.username, password='test') 
        response=self.client.get('/home/', {} , True)
        self.assertEqual(response.status_code, 200)  


    def test_correct_data_login_not_super_user(self):

        data = {
            "username" : "test2",
            "password" : "test",
            "captcha_0" : "XXXX",
            "captcha_1" : "PASSED",
        }
        form = self.form(data = data)
        
        self.assertTrue(form.is_valid())
        self.client.login(username=self.user2.username, password='test') 
        response=self.client.get('/home/', {} , True)
        self.assertEqual(response.status_code, 403)  


    def test_wrong_captcha(self):

        data = {
            "username" : "test2",
            "password" : "test",
            "captcha_0" : "XXXX",
            "captcha_1" : "ABCD",
        }
        form = self.form(data = data)
        
        self.assertFalse(form.is_valid())



