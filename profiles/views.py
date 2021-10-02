from django.db.models import query


# Create your views here.
from .models import Profile
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

import json 
# Create your views here.

def getting_profiles(request):
    profiles=Profile.objects.all()
    context={
        "profiles":profiles
    }
    return render(request,"index.html",context)
def getProfiles(request):
    profiles=Profile.objects.all()
    print(profiles.values())
    return JsonResponse({"profiles":list(profiles.values())})

def create(request):
    return render(request,"form.html",{})

def insert(request):
    if request.method=="POST":
       first_name=request.POST['first_name']
       last_name=request.POST['last_name']
       email=request.POST['email']
       phone=request.POST['phone']
       new_profile=Profile(first_name=first_name,last_name=last_name,email=email,phone=phone)
       new_profile.save()
       return HttpResponse('New Profile created successfully')

def delete(request,pk):
           print(pk)
           if request.is_ajax():
                try:
                    profile=Profile.objects.get(id=pk)
                    print(profile)
                    profile.delete()
                    return JsonResponse({"message":"success","pk":pk})
                except:
                    return JsonResponse({"message":"Failure"})
               
           return JsonResponse({"message":"Wrong Route"})


def get_profile(request,ID):
    
    profile = Profile.objects.filter(id = ID).values()
    first_name=profile[0]["first_name"]
    last_name=profile[0]["last_name"]
    email=profile[0]["email"]
    phone=profile[0]["phone"]
    return JsonResponse({"id":ID,"first-name":first_name,"last-name":last_name,"email":email,"phone":phone})


def update(request):
    
    if request.method=="POST":
       profile_id=request.POST['profile_id']
       first_name=request.POST['first_name']
       last_name=request.POST['last_name']
       email=request.POST['email']
       phone=request.POST['phone']
       new_profile=Profile(id=profile_id,first_name=first_name,last_name=last_name,email=email,phone=phone)
       new_profile.save()
       print(profile_id,first_name,last_name,email,phone)
       return HttpResponse('Updated successfully')




