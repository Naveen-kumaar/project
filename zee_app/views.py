from django.shortcuts import render,redirect
from zee_app.models import Add_patientdetails
from zee_app.models import register


# Create your views here.
def home(request):
    return render (request,'home.html')

def Register(request):

    if request.method == 'POST':
    
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        role = request.POST.get('role')
        Password = request.POST.get('Password')
        C_Password = request.POST.get('C_Password')
        en = register(name=name,email=email,mobile=mobile,role=role,Password=Password,C_Password=C_Password)
        en.save()

        # myuser= User.objects.create_user(name,email,mobile,role,Password,C_Password)
        # myuser.save()



        return redirect('login')
    return render (request,'register.html')

def Login(request):
    return render(request,'login.html')

def create(request):
    
    if request.method == 'POST':
        date = request.POST.get('date')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        occupation = request.POST.get('occupation')
        address = request.POST.get('address')
        contactno = request.POST.get('contactno')
        chiefcomplaint = request.POST.get('chiefcomplaint')
        injury = request.POST.get('injury')
        history = request.POST.get('history')
        pain = request.POST.get('pain')
        site = request.POST.get('site')
        duration = request.POST.get('duration')
        onset = request.POST.get('onset')
        aggrvating = request.POST.get('aggrevating')
        factor = request.POST.get('factor')
        palpation = request.POST.get('palpation')
        test = request.POST.get('test')
        treatment = request.POST.get('treatment')

        en = Add_patientdetails(Date = date,Name = name,Age = age,Gender = gender,Occupation = occupation,
        Address = address,
        Contactno= contactno,
        Chief_complaint = chiefcomplaint,
        Injury = injury,
        History = history,
        Pain = pain,
        Site = site,
        Duration = duration,
        Onset = onset,
        A_factor = aggrvating,
        R_factor = factor,
        On_palpation = palpation,
        Special_test = test,
        Treatment= treatment)
        

        en.save()
        
    return render(request,'create.html')


def view(request):
    return render(request,'view.html')