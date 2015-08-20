from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import response
from rest_framework.test import APIRequestFactory, APITestCase
from api.views import ListCreateView
from movie.models import Movie


class ListViewTests(APITestCase):

    def setUp(self):
        user = User.objects.create(username='bob', email='a@a.com', password='a')
        self.top_gun = Movie.objects.create(title="Top gun", owner=User.objects.get(pk=1))
        self.fast_times = Movie.objects.create(title="fast times", owner=User.objects.get(pk=1))
        self.stripes = Movie.objects.create(title="stripes", owner=User.objects.get(pk=1))

    # def testPost(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/movies/', {'title': 'fast times', 'owner': 'user'}, format='json')
    #     view = ListCreateView.as_view()
    #     response = view(request)
    #     self.assertEquals(response.content, {'title': 'fast times', 'owner': 'user'})

    def testGet(self):
        factory = APIRequestFactory()
        request = factory.get('/movie/1/')
        view = ListCreateView.as_view()
        response = view(request)
        response.render()
        self.assertContains(response, "Top gun")

#
# class DeleteViewTests(TestCase):
#
#     def testUpdate(self):
#         factory = APIRequestFactory()
#         request =