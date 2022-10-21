from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=200) #show article title
	slug=models.CharField(max_length=200) #show article URL
	body=models.TextField() #show article content
	pub_date=models.DateTimeField(default=timezone.now)
	#Make the article display by the pub_date time
	class Meta:
		ordering=('-pub_date',)

	def __str__(self):
		return self.title
