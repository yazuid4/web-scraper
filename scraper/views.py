from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, FileResponse, HttpResponse
from  django.core.validators import URLValidator


import requests
from bs4 import BeautifulSoup
import re
import random
import os
import time;


from scraper.func_helpers import scraper, isValidUrl



def get_home(req, message='', link='', file_id=''):

	if req.method == 'POST':
		link = req.POST['link']
		keys = req.POST['mykeys'].strip().split(',')
	
	
		if not isValidUrl(link):
			message = 'Please enter a valid web page address...'
			return HttpResponseRedirect(reverse('home-message', args=[message]))

		lines = []
		try:
			lines = scraper(link, keys)
		except Exception as e:
			message = 'Server error, please retry again or use another url...'
			return HttpResponseRedirect(reverse('home-message', args=[message]))

		if len(lines) == 0:
			message = 'No visible text found, try with another page address or other keywords...'
			return HttpResponseRedirect(reverse('home-message', args=[message]))

		
    	#create a hash for it
		hash = random.getrandbits(64)
		file_id = str(hex(hash))[2:]
		ts = time.time()
		file_id += '_' + str(int(ts))

		f = open( 'results/file'+file_id+'.txt', 'w',  encoding='utf-8')
		for line in lines:
			f.write(line)
		f.close()
        
		message = "Click here to download the result of the extraction:"
		args = [message, file_id]
		return HttpResponseRedirect(reverse('home-result', args=args))
		

	context = {
	           'App': 'Scraper',
			   'link': link,
			   'message': message,
			   'file_id': file_id
			   }
			   
	return render(req, 'scraper_home/index.html', context)




def get_file(req, file_id):
    file_name = 'results/file'+file_id+'.txt'
    try:
    	f = open(file_name, 'rb')
    except:
     	return HttpResponse("<h3>Error 404: Not Found</h3>")

    return FileResponse(f, as_attachment=True, filename=file_name)
