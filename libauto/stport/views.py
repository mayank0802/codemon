from django.shortcuts import render
from stport.models import student_info
def feedback(request):
	return render(request, 'feedback.html')
def register(request):
	if request.method == "POST":
		email = request.POST.get('email','')
		psw = request.POST.get('psw','')
		remail= request.POST.get('remail','')
		rpsw = request.POST.get('rpsw')
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		street = request.POST.get('street')
		city = request.POST.get('city')
		print(email,end="\n")
		stud_ID = student_info(student_email = email, student_password = psw, student_name = name, student_phone = phone, student_street = street, student_city = city)
		stud_ID.save()
	return render(request,'register.html')
def detail(request):
	return render(request,'detail.html')
def search(request):
	render(request,'search.html')
	#speech recognition
	import speech_recognition as sr
	import webbrowser as wb
	import bs4
	import lxml
	import requests

	chrome_path ="C:/Users/HP/AppData/Local/Google/Chrome/Application/chrome.exe"
	r= sr.Recognizer()

	with sr.Microphone() as source:

		print("say something\n")
		audio = r.record(source,duration =5)
	try:
	    text= r.recognize_google(audio)
	    print(text)
	    res = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + text+ '&callback=handleResponse')
	    soup = bs4.BeautifulSoup(res.text, 'lxml')
	    t = str(soup.select('body'))
	    f = open('C:/Users/HP/Desktop/sih_django/libauto/stport/templates/detail.html','w')
	    index =t.find('title')
	    while(t[index]!= ','):
	        if(t[index]!= '"'):
	            print(t[index], end="")
	            f.write(t[index])
	        index = index +1
	    f.write("</br>")    
	    index =t.find('author')
	    while(t[index]!= ','):
	        if(t[index]!= '"'):
	            print(t[index], end="")
	            f.write(t[index])
	        index = index +1    
	    f.close()   
	except Exception as e:
		print(e)
		
	return render(request,'detail.html')
def rlogin(request):
	if(request.method == 'POST'):
		uname = request.POST.get('user_name')
		pas = request.POST.get('pass_word')
		st  = student_info.objects.all().filter(student_name = uname)
		for info in st:
			if(info.student_password == pas):
				params = {'name':info.student_name, 'id':info.student_id, 'email' : info.student_email, 'city' : info.student_city, 'street': info.student_street, 'phone' : info.student_phone, 'issue': info.student_issue} 
				return render(request, 'search.html',params)
	return render(request,'rlogin.html')