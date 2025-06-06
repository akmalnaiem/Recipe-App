from django.shortcuts import render,redirect
from vege.models import *

# Create your views here.

##CRUD Operation-
#Create-
def receipes(request):
    if request.method == "POST":
        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description =  receipe_description,
            receipe_image = receipe_image,
        )
        return redirect('receipes')              # Only redirect after POST
    
    return render(request,'receipes.html')       # Render template on GET


#Read
def read_items(request):
    queryset = Receipe.objects.all()

    #Search Functionality and Filter Functionality
    if request.GET.get("search"):
        # print(request.GET.get("search"))    # this will print the content written in search box means search is working..
        queryset = queryset.filter(receipe_name__icontains = request.GET.get("search"))   #"__icontains" is django keyword that check the value that pass is n the particular string or not just like we do in python if "r" in "receipe" same as that...

    context = {'receipes' : queryset}
    # return redirect("read_items")
    return render(request , 'read.html' , context)


#Delete
def delete_items(request , id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete() 
    return redirect("read_items")


#Update
def update_receipe(request , id):
    queryset = Receipe.objects.get(id = id)
    if request.method == "POST":
        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image :
            queryset.receipe_image = receipe_image
        
        queryset.save()

        return redirect("read_items")

    context = {'receipes' : queryset}
    return render(request , 'update.html' , context)
