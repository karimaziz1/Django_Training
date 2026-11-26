from django.db import models
from AccountApp.models import Doctor
from AccountApp.models import Patient
from django.utils import timezone
from django.core.exceptions import ValidationError
class Appointment(models.Model):
    reason=models.TextField()
    discription =models.FileField(
        blank=True,
        upload_to='prescription/'
        
    )
    class status(models.TextChoices):
        PENDING="PENDING","en attente "
        CONFIRMED="CONFIRMED","confirme"
        CANCELLED="CANCELLED ","annule"
    #status=models.CharField(max_length=10,choices=Status.choices,default=Status.PENFING)
    status = models.CharField(
    max_length=10,
    choices=status.choices,
    default=status.PENDING
)
    status=models.CharField(max_length=10,choices=[("PENDING","en attent"),("CONFIRMED","confirme"),("CANNCELLED","annule")])
    duration_munites=models.PositiveBigIntegerField(default=30)
    created_at =models.DateTimeField(auto_now=True)
    update_at=models.DateTimeField(auto_now=True)
    appointment_date=models.DateTimeField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appoitment')
    patient=models.ForeignKey(Patient ,on_delete=models.CASCADE, related_name="appoitment")
   
 #seance 3   26/11/2026
def clean(self):
    modified_date=self._state.adding or (
        Appoitment.objects.filter(
            pk=self.pk , Appoitment_date=self.appointment_date
        ).exists()
    )
    if modified_date and self.appointment_date<=timezone.now():
         raise ValidationError ("la date rdv doit etre > a la date  aujourd'hui")
     

#seance 3 26/11/2026 
class meta :
    ordering=["-appointement-date"]
    constrainet =[
        models.UniqueConstraint(
            fields=["docter","appointment-date"],
            name="unicite-patient-doctor-date",
            violation_error_message="erreur rdv  echoue"
        )
    ]
    def __str__(self):
        return f"le rdv est : {self.reason}"