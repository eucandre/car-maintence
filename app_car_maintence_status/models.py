from django.db import models
from app_car.models import *


class Car_maintence_trip(models.Model):
	car = models.CharField(max_length=255)
	gas_capacity = models.FloatField()
	distance = models.FloatField(help_text= 'In km', blank = False, null= False)
	status = models.CharField(max_length = 255)
	tire1 = models.FloatField(default = 100)
	tire2 = models.FloatField(default = 100)
	tire3 = models.FloatField(default = 100)
	tire4 = models.FloatField(default = 100)

	def trip(self,car, distance):
		if self.distance:
			self.tire1 = self.distance - (self.distance/3)*(1/100)
			self.tire2 = self.distance - (self.distance/3)*(1/100)
			self.tire3 = self.distance - (self.distance/3)*(1/100)
			self.tire4 = self.distance - (self.distance/3)*(1/100)
			self.gas_capacity = self.distance/8
			return "Tire 1:{}%;Tire 2:{}%; Tire 3:{}%; Tire 4:{}%; Gas quantity:{}%".format(self.tire1,self.tire2,self.tire3,self.tire4,self.gas_capacity)

	def Refuel(self,car, gas_quantity):
		if self.distance:
			return "{}".format()
		

		



