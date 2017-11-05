# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
from pprint import pprint

from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .messenger_api import (post_facebook_message,
                            get_user_information,
                            AttachmentTemplate)



class api_webhook(generic.View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        req = json.loads(self.request.body.decode('UTF-8'))
        try:
            action = req.get('result').get('action')
        except AttributeError:
            return 'json error'


        if action == 'greet':
            print "greet action...."
            print (req)
            speech = greet_action(req)
        elif action == 'admin':
            print "admin action...."
            print (req)
            speech = admin_action(req)
        else:
            speech = "Out of scope... :("


        data = {
            "speech": speech,
            "displayText": speech,
            # "data": data,
            # "contextOut": [],
            #"source": "Houzlook"
               }

        return JsonResponse(data)



def greet_action(req):
    senderId = req.get('originalRequest').get('data').get('sender').get('id')
    user_info = get_user_information(senderId)
    message = "hello Mr. "+ user_info['first_name'] + " nice to meet with u."
    
    #greet_img = AttachmentTemplate(url='https://media.giphy.com/media/3ov9jUIrBibUBgy2Oc/giphy.gif', type='image')
    #post_facebook_message(senderId, greet_img.get_message())

    return message


def admin_action(req):
    senderId = req.get('originalRequest').get('data').get('sender').get('id')
    actionIncomplete = req.get('result').get('actionIncomplete')
    if actionIncomplete == True:
        #speech = req.get('fulfillment').get('speech')
        print "api default prompts...."
        print req.get('result').get('fulfillment')
    else:
        user_name = req.get('result').get('parameters').get('name')
        password = req.get('result').get('parameters').get('password')
        for i in range(len(ADMIN)):
            if ADMIN[i]['name'] == user_name:
                online_list = "  \n".join([FB_USER[i]['first_name']+" "+str(FB_USER[i]['date_time'])+" sec ago" for i in range(len(FB_USER))])
                
                message = "Hello Admin "+ user_name +" nice to meet u again." + "\n ######### \n" + online_list
                break
            else:
                message = "Sorry only admins are allowed.."

        return message




    


ADMIN = [
    {"name": "sambit",
    "password": "pass1234"},

    {"name": "rohit",
    "password": "pass1234"},

    {"name": "raj",
    "password": "pass1234"}
        ]


FB_USER = [
    {
        "first_name": "sambit",
        "fb_id": "1624518630891854",
        "date_time": 10,
    },
    {
        "first_name": "sekhar",
        "fb_id": "1624518630891854",
        "date_time": 8,
    },
]
    


