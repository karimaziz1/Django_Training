from django.db import models
from AccoutnApp.models import Doctor
from AccoutnApp.models import Patient
class Appoitment(models.Modul):
    reason=models.TextField()
    discription =models.models.FileField(
        blank=True,
        upload_to='prescription/'
        
    )
    class status(models.TextChoices):
        PENDING="PENDING","en attente "
        CONFIRMED="CONFIRMED","confirme"
        CANCELLED="CANCELLED ","annule"
    status=models.CharField(max_length=10,choices=Status.choices,default=Status.PENFING)
    status=models.CharField(max_length=10,choices=[("PENDING","en attent"),("CONFIRMED","confirme"),("CANNCELLED","annule")])
    duration_munites=models.PositiveBigIntegerField(default=30)
    created_at =models.DateTimeField(auto_now=True)
    update_at=models.DateTimeField(auto_now=True)
    appointment_date=models.DateTimeField()
    doctor=models.models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appoitment')
    patient=models.ForeignKey(Patient ,on_delete=models.CASCAD, related_name="appoitment")
    
# Create your models here.
