from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# This is a Function-Based Views
def hello_world(request):
    return HttpResponse("Hello from Function-Based!")

# This is a Class-Based Views
class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello From Class-Based View!")

def student_profile(request):
    student = [
    {"name":"Juan Dela Cruz", "age":21, "course":"BSIT"},
    {"name":"Juan Dela Cruz", "age":21, "course":"BSIT"},
    {"name":"Juan Dela Cruz", "age":21, "course":"BSIT"},
    {"name":"Juan Dela Cruz", "age":21, "course":"BSIT"},



    ]
    return render(request, "student_profile.html", {"student":student})

def student_list(request):
    students = [
        {"name": "Ana", "age":22},
        {"name": "Mark", "age":20},
        {"name": "Liza", "age":23},
    ]
    return render(request, 'student_list.html', {"students":students})