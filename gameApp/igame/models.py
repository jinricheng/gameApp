from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date
# Create your models here.

def get_default_user():
    	return User.objects.get(pk=1)

class Shop(models.Model):
	name =  models.CharField(max_length = 20)
	address = models.TextField(max_length = 100)
	cif = models.CharField(max_length = 10,default="")
	date = models.DateField(default = date.today)
	user = models.ForeignKey(User,default = get_default_user)
	city = models.TextField(default=" ")
	country = models.TextField(blank=True,null=True)
	def __unicode__(self):
		return self.name	
	def get_absolute_url(self):
		return reverse('igame:shop_detail',kwargs={'pk':self.pk}) 


class Producer(models.Model):
	name =  models.TextField()
	address = models.TextField(blank = True, null=True)
	nif = models.CharField(max_length = 10,default="")
	date = models.DateField(default = date.today)
	user = models.ForeignKey(User,default = get_default_user)
	city = models.TextField(default=" ")
	country = models.TextField(blank=True,null=True)
	def __unicode__(self):
		return u"%s" % self.name
	def get_absolute_url(self):
		return reverse('igame:producer_detail',kwargs={'pk':self.pk}) 	
	
class Game(models.Model):
	name = models.CharField(max_length = 20)
	publishYear = models.IntegerField()
	genre = models.CharField(max_length = 10)	
	description = models.TextField(max_length = 300)
	gameCode = models.CharField(max_length = 10,default="")
	date = models.DateField(default = date.today)
	price = models.IntegerField(max_length = 5, default = 0)
	user = models.ForeignKey(User,default = get_default_user)
	producedBy = models.ForeignKey(Producer,null = True, related_name = 'producedby')
	soldBy = models.ManyToManyField(Shop,null = True, related_name = 'soldby')
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('igame:game_detail',kwargs={'pk':self.pk}) 
	def averageRating(self):
        	ratingSum = 0.0
        	for review in self.gamereview_set.all():
            		ratingSum += review.rating
        	reviewCount = self.gamereview_set.count()
        	return ratingSum / reviewCount


class Review(models.Model):
	RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
	rating = models.PositiveSmallIntegerField('Rating(stars)',blank=False,default = 5,choices=RATING_CHOICES)
	comment = models.TextField(blank = True, null = True)
	user = models.ForeignKey(User,default = get_default_user)
	date = models.DateField(default = date.today)

	class Meta:
		abstract = True
	

class gameReview(Review):
	game = models.ForeignKey(Game)
