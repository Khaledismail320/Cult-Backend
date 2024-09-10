from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed
from django.core.exceptions import ObjectDoesNotExist 
# Create your views here.
from .models import Messages
import json

@csrf_exempt
def newMessage(request):
    data=json.load(request)
    name=data['name']
    email=data['email']
    subject=data['subject']
    inquiryType=data['inquiryType']
    Message=data['Message']
    # Create a new message
    try:
        newMessage = Messages(name=name,email=email,subject=subject,inquiryType=inquiryType,Message=Message)
        newMessage.save()
        
        response = {
            "message": "User created successfully",
            }

        return HttpResponse( json.dumps(response),  status=200)
    except Exception as e:
        response = {
        "error": str(e),
        }
        return HttpResponse( json.dumps(response),  status=400)
    
    
@csrf_exempt 
def getAllMessages(request):
    try:
        messages = Messages.objects.all()
        response = {
            "messages": list(messages.values())
        }
        return JsonResponse(response, status=200)
    except Exception as e:
        response = {
        "error": str(e),
        }
        return HttpResponse( json.dumps(response),  status=400)
    

@csrf_exempt
def deleteMessage(request):
    try:
        data = json.load(request) 
        id=data['id']
        
        message = Messages.objects.get(id=id)
        message.delete()
        response = {
            "message": "Message deleted successfully",
            }
        return HttpResponse( json.dumps(response),  status=200)
    except ObjectDoesNotExist:
        response = {
            "error": "Message not found",
            }
        return HttpResponse( json.dumps(response),  status=400)
    except Exception as e:
        response = {
            "error": str(e),
            }
        return HttpResponse( json.dumps(response),  status=400)     