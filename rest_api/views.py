from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Addresses
from .serializers import AddressesSerializer
from rest_framework.parsers import JSONParser


# from .models import Choice, Question

# Create your views here.
@csrf_exempt
def address_list(request):
    if request.method == "GET":
        query_set = Addresses.objects.all()
        serializer = AddressesSerializer(query_set, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


# class AddressSelect:
#     def __init__(self):
#         self.serializer = None

@csrf_exempt
def address(request, pk):
    obj_id = Addresses.objects.get(pk=pk)
    if request.method == "GET":
        serializer = AddressesSerializer(obj_id)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        obj_id.delete()

        return HttpResponse(status=204)

@csrf_exempt
def address_name(request, name):
    name = Addresses.objects.get(name=name)
    if request.method == "GET":
        serializer = AddressesSerializer(name)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        name.delete()

        return HttpResponse(status=204)

@csrf_exempt
def login(request):
    userid = None
    success = False

    if request.method == "POST":
        print("request " + str(request))
        print("body " + str(request.body))
        userid = request.POST.get("userid", "")
        userpw = request.POST.get("userpw", "")
        if userid == "" or userpw == "":
            success = False
        else:
            success = True

        print("userid = " + userid + " userpw = " + userpw)

    # return HttpResponse(status=200)
    return render(request, "result.html", {"userid": userid, "success": success})
        # data = JSONParser().parse(request)
        # search_name = data["name"]
        # obj = Addresses.objects.get(name=search_name)
        #
        # if data["phone_number"] == obj.phone_number:
        #
        #     return HttpResponse(status=200)
        #
        # else:
        #
        #     return HttpResponse(status=400)


def login_page(request):

    return render(request, "login.html")


# def index(request, year):
# return HttpResponse("Hello, world. You're at the polls index.")

# a_list = Question.objects.filter(pub_date__year=year)
# b_list = Choice.objects.filter(a_list)
# context = {'year': year, 'choice_list': b_list}
# return render(request, "templates/year_archive.html")
