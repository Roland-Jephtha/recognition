from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .utils import is_ajax, classify_face
import base64
from logs.models import Log
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from profiles.models import Profile, CustomUser
from django.contrib import messages

  
  
  
def index(request):
    return render(request, "index.html")



def auth_view(request):
    return render(request, "signin.html")
 
 
 
def register(request):
    if request.method== "POST":
        username = "user: " + request.POST["first_name"] 
        fname = request.POST["first_name"]
        lname = request.POST["last_name"]
        email = request.POST["email"]
        city = request.POST["city"]
        state = request.POST["state"]
        graduation_year = request.POST["year_of_graduation"]
        study_year = request.POST["year_of_study"]
        department = request.POST["department"]
        matric_no = request.POST["matric_no"]
        photo = request.FILES["photo_upload"]
        password = "12345"
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Used ')
            return redirect('register')
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username Already Used")
            return redirect('register')
        else:
        
            user = CustomUser.objects.create_user(username=username, email = email, password = password)
            user.first_name = fname
            user.last_name = lname
            user.department = department
            user.save()
            
            profile = Profile.objects.create(
                user = user,
                photo = photo,
                username = username,
                mat_no = matric_no,
                department = department,
                study_year = study_year,
                city = city,
                state = state,
                graduation_year = graduation_year,
                email = email,
                first_name = fname,
                last_name = lname
            )
            # profile.save()
            
            messages.success(request, 'Account Created successfully')

            
            return redirect("signin")
    return render(request, 'signup.html')

 
 
 
 
 
 
 
 
 

def face_view(request):
    return render(request, 'face.html', {})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    profiles = Profile.objects.get(user = request.user)
    context ={
        "profiles" : profiles
    }
    return render(request, 'dashboard.html', context)

def find_user_view(request):
    if is_ajax(request):
        photo = request.POST.get('photo')
        _, str_img = photo.split(';base64')

        # print(photo)
        decoded_file = base64.b64decode(str_img)
        print(decoded_file)

        x = Log()
        x.photo.save('upload.png', ContentFile(decoded_file))
        x.save()

        res = classify_face(x.photo.path)
        if res:
            user_exists = CustomUser.objects.filter(username=res).exists()
            if user_exists:
                user = CustomUser.objects.get(username=res)
                profile = Profile.objects.get(user=user)
                x.profile = profile
                x.save()

                login(request, user)
                return JsonResponse({'success': True})
        return JsonResponse({'success': False})
    