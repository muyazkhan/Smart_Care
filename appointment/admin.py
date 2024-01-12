from django.contrib import admin
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.
class AppointmentModel(admin.ModelAdmin):
  list_display =["doctor_username","patient_username","appointment_type","appointment_status"]

  def doctor_username(self,obj):
    return obj.patient.user.username
  def patient_username(self,obj):
    return obj.doctor.user.username
  def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == "Running" and obj.appointment_type == "Online":
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('admin_email.html', {'user' : obj.patient.user, 'doctor' : obj.doctor})
            email = EmailMultiAlternatives(email_subject , '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
admin.site.register(Appointment,AppointmentModel)