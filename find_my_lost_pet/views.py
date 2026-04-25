from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import CustomUser
from email_validator import EmailNotValidError,validate_email


# Create your views here.

def index(request):
    return render(request,"find_my_lost_pet/index.html",)

def sign_up(request):
    if request.method == "GET":
        return render(request,"find_my_lost_pet/sign_up.html")
    else:
        name = request.POST["name_input"]
        phone_number = request.POST["phone_number_input"]
        email = request.POST["email_input"]
        password = request.POST["password_input"]
        confirm_password = request.POST["confirm_password_input"]
        context = {}
        if name == "":
            context["name_input_error_message"] = "Empty field must be fulfilled"    
        if phone_number == "":
            context["phone_number_input_error_message"] = "Empty field must be fulfilled"          
        if password == "" :
            context["password_input_error_message"] = "Empty field must be fulfilled"
        if confirm_password == "":
            context["confirm_password_input_error_message"] = "Empty field must be fulfilled"
        if password != confirm_password:
            context["confirm_password_input_error_message"] = "Please make sure the password and the confirm password match"
        try:
            valid = validate_email(email)
        except EmailNotValidError as e:
            context["email_input_error_message"] = "Please write a valid email"
            return render(request,"find_my_lost_pet/sign_up.html", context=context)
        else:
            if "name_input_error_message" in context or "phone_number_input_error_message" in context or "email_input_error_message" in context or "password_input_error_message" in context or "confirm_password_input_error_message" in context:
                return render(request, "find_my_lost_pet/sign_up.html", context=context)
            user = CustomUser(name = name, phone_number = phone_number, email = email, password = password)
            user.save()
            messages.success(request,"User registered successfully, please proceed to login")
            return redirect("find_my_lost_pet:login")
    
def login(request):
    if request.method == "GET":
        return render(request,"find_my_lost_pet/login.html")
    else:
        email = request.POST["email_input"]
        password = request.POST["password_input"]
        context = {}
        if email == "":
            context["email_input_error_message"] = "Empty field must be fulfilled"
        if password == "" :
            context["password_input_error_message"] = "Empty fields must be fulfilled"
        try:
            user = CustomUser.objects.get(email = email)
        except CustomUser.DoesNotExist:
            if email and password :
                context["invalid_credentials"] = "Invalid Credentials"
            return render(request, "find_my_lost_pet/login.html",context=context)
        else:
            if user.password != password:
                context["invalid_credentials"] = "Invalid Credentials"
                return render(request, "find_my_lost_pet/login.html",context=context)
            return HttpResponseRedirect(reverse("find_my_lost_pet:index"))