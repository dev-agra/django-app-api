from django.test import SimpleTestCase
from .views import add_sum
# from rest_framework.test import APIClient


# Unit testing
class Test_SUM(SimpleTestCase):
    def test_add_sum(self):
        x, y = 5, 6
        res = add_sum(x, y)
        self.assertEqual(res, 11)

# URL testing
# class TestViews(SimpleTestCase):
#     def test_get_greetings(self):
#         # create client
#         client = APIClient()

#         # make request
#         res = client.get('/greetings/')

#         # check result
#         self.assertEqual(res.status_code, 200) #OK = 200
#         self.assertEqual(
#             res.data,
#             ["Hello!", "Namaskar", "Bonjour!", "Hola!"],
#         )
