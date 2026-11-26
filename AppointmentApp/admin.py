from django.contrib import admin

# Register your models here.
from.models import Appointment

#admin.site.registre(Appointment)

@admin.action(description="make them confirmed")
def confirmed_appointment(model,req,queryset):
    queryset.update(status="CONFIRMED")
    
#enrig personalise
@admin.register(Appointment)
class AppointmentAdminpPers(admin.ModelAdmin):
    action=[confirmed_appointment]
    list_display=("reason","status","duration_minute","appointment_date")
    list_filter("reason", "appointment_date")
    list_editable=("status",)
    search_fileds=("status","status")
    ordering=("-appointment6_date",)
    list_per_page=2
    fieldsets = (
        ('Description', {
            'fields': ('reason', 'status', 'description')
        }),

        ('Date + Duration', {
            'fields': ('appointment_date', 'duration_minutes')
        }),

        ('Patients / Doctors', {
            'fields': ('doctor', 'patient')
        }),

        ('Planification', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

   

#@admin.register(Appointment)
#class AppointmentAdminpPers(admin.ModuelAdmin):
  #  list_display=("reason","status","duration_minute","appointment_date")  
   #  admin.site.register(Appointment,AppointmentAdminPers)