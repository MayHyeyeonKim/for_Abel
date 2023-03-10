from django.shortcuts import render
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from students.models import Student

def home_page(request):
    # default to Stranger if no user_name provided
    name = request.GET.get("user_name", " Stranger")
    message = f"<html><h1>Welcome{name} to my Website</h1></html>"
    # return HttpResponse(message)
    # return render(request, 'base.html')
    return render(request, 'base.html', {'name': name})

def all_students(request):
    all_students = Student.objects.all()
    context = {'all_students': all_students}
    return render(request, 'all_students.html', context)

def students(request):
    # View logic goes here
    all_students = Student.objects.all()
    return render(request, 'all_students.html', {'all_students': all_students})
    # return HttpResponse("Hello, students!")

# def detail(request, id):
#     students_detail = Student.objects.get(id=id)
#     return render(request, 'detail.html', {'students_detail': students_detail})

def detail(request, id):
    if request.method == 'GET':
        try:
            students_detail = Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404('Student does not exist')
        return render(request, 'detail.html', {'students_detail': students_detail})
