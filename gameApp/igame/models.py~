from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date
# Create your models here.

class Game(models.Model):
	name = models.CharField(max_length = 20)
	publishYear = models.IntegerField()
	genre = models.CharField(max_length = 10)	
	description = models.TextField(max_length = 300)
	gameCode = models.CharField(max_length = 10,default="")
	date = models.DateField(default = date.today)
	#user = models.ForeignKey(User,default = User.objects.get(id=1))
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('gameDetail',kwargs={'pk':self.pk}) 

class Shop(models.Model):
	name =  models.CharField(max_length = 20)
	address = models.TextField(max_length = 100)
	nif = models.CharField(max_length = 10,default="")
	date = models.DateField(default = date.today)
	#user = models.ForeignKey(User,default = User.objects.get(id=1))
	city = models.TextField(default=" ")
	country = models.TextField(blank=True,null=True)
	game = models.ForeignKey(Game,null = True, related_name = 'shops')
	def __unicode__(self):
		return self.name	
	def get_absolute_url(self):
		return reverse('shop:shop_detail',kwargs={'pk':self.pk}) 


class Producer(models.Model):
	name =  models.TextField()
	address = models.TextField(blank = True, null=True)
	nif = models.CharField(max_length = 10,default="")
	date = models.DateField(default = date.today)
	#user = models.ForeignKey(User,default = User.objects.get(id=1))
	city = models.TextField(default=" ")
	country = models.TextField(blank=True,null=True)
	game = models.ForeignKey(Game,null = True, related_name = 'producer')
	def __unicode__(self):
		return u"%s" % self.name
	def get_absolute_url(self):
		return reverse('gameproducer:gameproducer_detail',kwargs={'pk':self.pk}) 	
	

class Review(models.Model):
	RATING_CHOICES = ((1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'),(6,'six'),(7,'seven'),(8,'eight'),(9,'nine'),(10,'ten'))
	rating = models.PositiveSmallIntegerField('Rating(stars)',blank=False,default = 5,choices=RATING_CHOICES)
	coment = models.TextField(blank = True, null = True)
	user = models.ForeignKey(User,default = User.objects.get(id=1))
	date = models.DateField(default = date.today)

	class Meta:
		abstract = True
	

class gameReview(Review):
	game = models.ForeignKey(Game)
