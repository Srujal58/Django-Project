from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import patientForm

def home_page (request):
    data={
        'title':'Home Page'
    }
    return render(request,"index.html",data)

def registration (request):
    return render(request,"registration.html")

def doctors (request):
     return render(request,"doctors.html")

def appointment(request):
    return render(request,"appointment.html")

def feedback(request):
    return render(request,"feedback.html")
    
def register_patient(request):
    form = patientForm()

    if request.method == 'POST':
        form = patientForm(request.POST)
        if form.is_valid():
            form.save()
            # Handle successful form submission, e.g., redirect or display a success message

    return render(request, 'registration.html', {'form': form})