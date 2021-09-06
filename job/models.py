from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from datetime import datetime
# Create your models here.

#https://www.youtube.com/playlist?list=PL8GFhcuc_fW4cxdkRtWIlln1DQ3CZwQen
'''
 [1] models.Model :-from django and  provide us :- 
    - validation 
    - html widget 
    - size of field 

 [2] after creation model :- writes the following commands to django cearate models
     - python manage.py makmigrations 
          -- job/migrations/0001_initial.py # وظيفه الكمند الاول 
     - python manage.py migrate 
          -- Applying job.0001_initial      # وظيفه الكمند الثاني 

 [3] information about fields :- in google 
      - https://docs.djangoproject.com/en/3.2/ref/models/fields/
      - documentation of Django :- 
         -- in search write ==> Model field referenc        
'''

'''
  1] after finishing from project save files on github :- 
        -- git add .
             -  ~/CinemaTicketsReservation_Api/CinemaTicketsReservation_Api$ git add .
        -- git commit -m "write_description"
             -  ~/CinemaTicketsReservation_Api/CinemaTicketsReservation_Api$ git commit -m "pro"
        -- git push 
             -  ~/CinemaTicketsReservation_Api/CinemaTicketsReservation_Api$ git commit -m "pro"       
'''

'''
 Relations :- 
    - One to Many  ex. [ user -posts] ==> in django known ForeginKey
    - Many to Many  ex [user -groups]
    - One to one [user -profile]
'''

JOB_TYPE = [
    ('FT', 'FULL TIME'),
    ('PT', 'PART TIME'),
]


class Category(models.Model):
    name = models.CharField(max_length= 25)
    
    def __str__(self):
          return self.name


class Jobs(models.Model):  #table
      title = models.CharField(max_length= 20) #column (field)
      job_type = models.CharField(max_length=2, choices=JOB_TYPE, default='FT')
      description = models.TextField(max_length= 1000) 
      publish_at = models.DateTimeField(auto_now= True)
      vacency = models.IntegerField(default= 1)
      salery = models.IntegerField(default= 0)
      experience =models.IntegerField(default= 1)
      category = models.ForeignKey(Category ,on_delete= models.CASCADE )

      def __str__(self):
          return self.title 

''' 
1] to activate project :- 
   - source ./python_env/bin/activate
2] to run server :-    
   - python manage.py runserver
3] to know libraries which installed on env :-
   - pip freeze 
4] to save libraries in text file :- 
  - pip freeze > requirements.txt   
'''   

class Post(models.Model):
     title = models.CharField(max_length= 50)
     content =models.TextField(max_length= 100)
     created_at = models.DateTimeField(default= datetime.now)
     image =models.ImageField(upload_to = 'post-image/')