from rest_framework.test import APITestCase
from . import models as mymodels
from django.contrib.auth import get_user_model


User = get_user_model()


class ProductCommentTests(APITestCase):
	def setUp(self):
		self.user = User.objects.create(username='reza')
		sex = mymodels.Sex.objects.create(sex='Men', sex_persian='مردانه')
		attributes = {
		'name':'nametest',
		'color':'colortest',
		"price":10,
		"sex_id":sex.pk,
		'size':20,
		"more":'textfortest '*10,
		}
		mymodels.ProductInfo.objects.create(**attributes)



	def test_average_calculator(self):
		product_info = mymodels.ProductInfo.objects.all().first()
		rate_list = [1, 2, 3, 4 ,5]
		avg_of_list = sum(rate_list)/len(rate_list)
		for i in rate_list:
			mymodels.ProductComment.objects.create(rate=i ,text=f'comment test-{i}', user=self.user, product_info=product_info)
		self.assertEqual(product_info.average_rate, avg_of_list, msg=f'The productinfo rate average calculate mistake.')
		product_info.comment_set.all().delete()
		self.assertEqual(product_info.average_rate, 0, msg=f'Should return zero when not exists no comments.')


