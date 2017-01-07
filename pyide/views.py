# -*- coding: utf-8 -*-
# Hackerearth api
# Client Id: c4836616e36f7e78ff1255a0e4ec0b85b21da8c1a10e.api.hackerearth.com

# Client Secret Key: cac1db5448cc656abf0470f436d47f3e5d8d45c0

from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext

from django.views.decorators.csrf import ensure_csrf_cookie

# from .models import *
import requests
import datetime
import math
import json

def index(request):
	context_list = {}
	return render(request,"ide.html",context_list)


def compile(request):
	print "hello"
	COMPILE_URL = "http://api.hackerearth.com/code/compile/"
	CLIENT_SECRET = "cac1db5448cc656abf0470f436d47f3e5d8d45c0"
	source = request.GET.get('code')
	print source
	lang = request.GET.get('language')
	lang = lang.upper()
	data = {
		'client_secret': CLIENT_SECRET,
		'async': 0,
		'source': source,
		'lang': lang,
		'time_limit': 5,
		'memory_limit': 262144,
	}
	r = requests.post(COMPILE_URL,data=data)
	print r.json()
	run_status = r.json()['run_status']
	context_list = {
		'run_status': run_status,
	}
	return render(request,'ide.html',context_list)

def run(request):
	RUN_URL = "http://api.hackerearth.com/code/run/"
	CLIENT_SECRET = "cac1db5448cc656abf0470f436d47f3e5d8d45c0"
	source = request.GET.get('code')
	print source
	lang = request.GET.get('language')
	lang = lang.upper()
	data = {
		'client_secret': CLIENT_SECRET,
		'async': 0,
		'source': source,
		'lang': lang,
		'time_limit': 5,
		'memory_limit': 262144,
	}
	r = requests.post(RUN_URL,data=data)
	print r.json()['run_status']
	output =  r.json()['run_status']
	print output
	context_list = {
		'outputs': output['output_html'],
	}
	# context_list = {}
	# context_list['outputs'] = output
	# ret_value = []
	# ret_value.append(context_list)
	# ret_value = json.dumps(ret_value)
	ret_value = []
	ret_value.append(context_list)
	return HttpResponse(json.dumps(ret_value),content_type="application/json")