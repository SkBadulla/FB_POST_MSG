from django.shortcuts import render
import facebook
import urllib.request as ur
import os.path
# Create your views here.
from django.http import HttpResponse 
def post_msg(request):
	tk = 'EAAgGyaNBCygBAM0fB0CfoE5gOZBgyZBYu5fZCOYahJ8R63ZCAKCRIGbrOSZCGvSlVCZA5kJILiLEBZBOImNlbCuUG1ZBUZB4iByZBY8hptfR5YpYFLpsuGpw16NF8dqXni9Pm5B30atrB1gu8ZCNm0OKCwjpSRLOaqKagLLZADiFBa9ojDA6Ec0N8gvZCVFiFd7EJTkO2yeaaUjQIBgZDZD'
	fb = facebook.GraphAPI(access_token=tk)
	#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	#mypath=os.path.join(BASE_DIR, 'static\images\python.png'),
	#fb.put_object(parent_object='me',connection_name='feed',message='Good Morning...')
	#fb.put_photo('https://devarea.com/wp-content/uploads/2017/11/python.png',message='my tril using python')
	#fb.put_photo(image=ur.urlopen('https://codehandbook.org/wp-content/uploads/2017/01/py.jpg'),message='my tril using python')
	fb.put_photo(image=ur.urlopen('https://drive.google.com/uc?export=download&id=1fIQ8cBrUtaHWctIwQ5jpORBRtefw895i'),message='my tril using python, getting image from Google drive')
	return HttpResponse("<h2>Done....</h2>")