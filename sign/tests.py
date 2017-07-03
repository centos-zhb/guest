from django.test import TestCase
from sign.models import Event,Guest

# Create your tests here.
class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1,name="oneplus 3 event",status=True,limit=2000,address='shenzhen',start_time='2017-07-03 17:30:00')
        Guest.objects.create(id=1,event_id=1,realname='alen',phone='13711001101',email='alen@mail.com',sign=False)

    def test_event_models(self):
        '''测试发布会表'''
        result = Event.objects.get(name="oneplus 3 event")
        self.assertEqual(result.address,"shenzhen")
        self.assertTrue(result.status)

    def test_guest_models(self):
        '''测试嘉宾表'''
        result = Guest.objects.get(phone='13711001101')
        self.assertEqual(result.realname,"alen")
        self.assertFalse(result.sign)

    def tearDown(self):
        pass

if __name__ == '__main__':
    ModelTest(TestCase)