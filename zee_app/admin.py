from django.contrib import admin
from zee_app.models import register
from zee_app.models import Add_patientdetails
# from zee_app.models import login
# Register your models here.



# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list = ['name','email','mobile','role','Password','C_Password']

admin.site.register(register,RegisterAdmin)

# class LoginAdmin(admin.ModelAdmin):
#     list = ['name','email','Password']

# admin.site.register(login,LoginAdmin)
class patientdetail(admin.ModelAdmin):
    list = ['Date','Name','Age','Gender','Occupation','Address','Contactno','Cheif_complaint','Injury','History','Pain','Site','Duration','Onset','A_factor','R_factor','On_palpation','Special_test','Treatment']

admin.site.register(Add_patientdetails,patientdetail)
