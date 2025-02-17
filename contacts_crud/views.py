from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from contacts_crud.serializers import ContactSerializer
from contacts_crud.models import Contact

@csrf_exempt
def contactApi(request,id=0):
    if request.method=='GET':
        contact = Contact.objects.all()
        contact_serializer=ContactSerializer(contact,many=True)
        return JsonResponse(contact_serializer.data,safe=False)
    elif request.method=='POST':
        contact_data=JSONParser().parse(request)
        contact_serializer=ContactSerializer(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        contact_data=JSONParser().parse(request)
        contact=Contact.objects.get(id=id)
        contact_serializer=ContactSerializer(contact,data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        contact=Contact.objects.get(id=id)
        contact.delete()
        return JsonResponse("Deleted Successfully",safe=False)
