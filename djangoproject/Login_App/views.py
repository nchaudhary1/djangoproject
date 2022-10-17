from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

def HomePage(request):
    return render(request,'Login_App/homepage.html')

def IndexPage(request):
    
    return render(request,'Login_App/indexpage.html')

@csrf_exempt
def AllStudentDetails(request):
    try:
        all_student = Student.objects.all()
    except:
        return HttpResponse('So Sorry! data not found', status = 404)
    if request.method == 'GET':
        students = StudentSerializer(all_student, many = True)
        return JsonResponse(students.data, safe = False)

    elif request.method == 'POST':
        input_data = JSONParser().parse(request)
        serializer = StudentSerializer(data = input_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else:
            return HttpResponse('Invalid Data', status = 400)

@csrf_exempt   
def SingleStudentDetails(request, pk):
    try:
        student = Student.objects.get(pk = pk)
    except:
        return HttpResponse('So sorry! Data not found', status = 404)

    if request.method == 'GET':
        student_data = StudentSerializer(student)
        return JsonResponse(student_data.data, status = 200)
    elif request.method == 'PUT':
        update_data = JSONParser().parse(request)
        serializer = StudentSerializer(student,data = update_data)

        if serializer.isvalid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else:
            return HttpResponse('Invalid Data', status = 400)
    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse('Successfully Deleted', status = 204)

