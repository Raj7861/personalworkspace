from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    myDict={"name": "Siraj"}
    return render(request, "templatesApp/firstTemplate.html", context=myDict)