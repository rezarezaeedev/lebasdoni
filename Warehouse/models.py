from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators

User = get_user_model()


class ProductComment(models.Model):
	text = models.CharField(max_length=500)
	rate = models.SmallIntegerField(validators=[validators.MaxValueValidator(5,'Maximum rate number is 5.'), validators.MinValueValidator(1,'Minimum rate number is 1.')])
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product_info = models.ForeignKey('ProductInfo', on_delete=models.CASCADE, related_name = 'comment_set')
	created_at = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=1)


	def __str__(self):
		return f'{self.user}-{self.product_info.name}-{self.rate}'


class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product_info = models.ForeignKey('ProductInfo', on_delete=models.CASCADE)

	class Meta:
		unique_together = ['user', 'product_info']

	def __str__(self):
		return f'{self.user}-{self.product_info.name}'


class Sex(models.Model):
	sex = models.CharField(max_length=10, unique=True)
	sex_persian = models.CharField(max_length=10, unique=True, help_text='please enter sex name in persian/لطفا جنسیت را به فارسی تایپ کنید.')

	def __str__(self):
		return f'{self.sex}/{self.sex_persian}'


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class ProductInfo(models.Model):
	name = models.CharField(max_length=50)
	color = models.CharField(max_length=20)
	price = models.FloatField()
	sex = models.ForeignKey('Sex', on_delete=models.CASCADE)
	size = models.SmallIntegerField()
	more = models.TextField()
	category = models.ManyToManyField('Category')
	active = models.BooleanField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	# material = FK 2 Material

	def __str__(self):
		return f'{self.name} {self.color} {self.price}$'

	@property
	def average_rate(self):
		result = 0
		queryset = self.comment_set.all()
		queryset  = list(map(lambda x:x.rate ,queryset))
		if queryset:
			result = sum(queryset)/len(queryset)
		return result


class Product(models.Model):
	product_info = models.ForeignKey('ProductInfo', on_delete=models.CASCADE)
	is_available = models.BooleanField(default=True)
	is_reserved  = models.BooleanField(default=False)
	imported_time = models.DateTimeField(auto_now_add=True, editable=False)
	exported_time = models.DateTimeField(null=True, blank=True, editable=False)

	def __str__(self):
		return f'{self.pk}-Availablity:{self.is_available} ,Reservilty:{self.is_reserved}'