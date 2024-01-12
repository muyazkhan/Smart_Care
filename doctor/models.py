from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient


# Create your models here.
class specialization(models.Model):
  name = models.CharField(max_length=30)
  slug = models.SlugField(max_length=40)

  def __str__(self):
    return self.name

class designation(models.Model):
  name = models.CharField(max_length=30)
  slug = models.SlugField(max_length=40)

  def __str__(self):
    return self.name


class AvailableTime(models.Model):
  name = models.CharField(max_length=200)
  def __str__(self):
    return self.name

class Doctor(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  image = models.ImageField(upload_to="doctor/images/")
  Designation = models.ManyToManyField(designation)
  Specialization = models.ManyToManyField(specialization)
  available_time = models.ManyToManyField(AvailableTime)
  fee = models.IntegerField()
  meet_link =models.CharField(max_length=200)

  def __str__(self):
    return self.user.username



STAR_RATTING =[
  ('⭐','⭐'),
  ('⭐⭐','⭐⭐'),
  ('⭐⭐⭐','⭐⭐⭐'),
  ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
  ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]

class review(models.Model):
  reviewer = models.ForeignKey(Patient,on_delete=models.CASCADE)
  doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  ratting = models.CharField(choices=STAR_RATTING, max_length=10)

  def __str__(self):
    return f"Patient: {self.reviewer.user.username}"