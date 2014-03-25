from django.db import models

# Create your models here.

class Producer(models.Model):
	name =  models.CharField(max_length = 20)
	address = models.TextField(max_length = 300)
	def __unicode__(self):
		return self.name 	

class Shop(models.Model):
	name =  models.CharField(max_length = 20)
	address = models.TextField(max_length = 300)
	def __unicode__(self):
		return self.name 	

class Game(models.Model):
	name = models.CharField(max_length = 20)
	publishYear = models.IntegerField()
	genre = models.CharField(max_length = 10)	
	description = models.TextField(max_length = 300)
	producedBy = models.ForeignKey(Producer)
	soldBy = models.ForeignKey(Shop)
	def __unicode__(self):
		return self.name 	



