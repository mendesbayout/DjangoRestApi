from django.test import TestCase
from .models import Cheff

class Chefftest(TestCase):
    def setUp(self):
        Cheff.objects.create(id="Sanji", direction="Wano", phone='330', curriculum="a")
        #Cheff.objects.create(id="Zeff", direction="East Blue", phone='001')
                
    def test_cheff(self):
        Sanji =  Cheff.objects.get(id='Sanji')
        Zeff = Cheff.objects.get(id="Zeff")
        self.assertEqual(Sanji.speak(), "Nakamaaaa")
        #self.assertEqual(Zeff.speak(), "sanjiiiiiii")
