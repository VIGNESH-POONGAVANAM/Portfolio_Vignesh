from django.http import HttpResponse
from django.shortcuts import render
from .forms import contactform

# Create your views here.
def portfolio_view(request):
    return render(request,"Index.html")

def storedb(request):
    if request.method == "POST":
        form = contactform(request.POST)
        NAME = request.POST.get("name")
        EMAIL = request.POST.get("email")
        MESSAGE = request.POST.get("message")
        form.Name = NAME
        form.Email = EMAIL
        form.Message = MESSAGE
        form.save()
        return HttpResponse("<script>alert('Success')</script>")
    return render(request,"Index.html") 