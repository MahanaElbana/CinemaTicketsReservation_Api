from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
from django.contrib.auth.models import User

class Meal(models.Model):
    title = models.CharField(max_length = 32)
    description = models.TextField(max_length = 360)
    

    def number_of_rating(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)

    def avarage_rating(self):
        sum = 0
        ratings = Rating.objects.filter(meal=self)
        #print(ratings)
        for items_of_rating in ratings:
            sum += items_of_rating.stars

        if len(ratings)>0:    
            return sum/len(ratings)

        else:
            return 0    

    def __str__(self):
           return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal , related_name = 'meal',on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name = 'user', on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
       
    class Meta:
        unique_together = (('user','meal'))
        index_together = (('user','meal'))


# source ./python_env/bin/activate        