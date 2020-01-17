from django.shortcuts import render
#from .models import student_info,login_info
import speech_recognition as sr
import webbrowser as wb
import bs4
import lxml
import requests
def feedback(request):
	return render(request, 'feedback.html')
def login(request):
	if request.method == "POST":
		uname= request.POST.get('user_name','')
		psw = request.POST.get('password', '')
		login_detail = login_info(uname = uname, psw = psw)
		login_detail.save()
	return render(request,'login.html')	
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
		stud_ID = student_info(student_email = email, student_password = psw, student_name = name, student_phone = phone, student_street = street, student_city = city)
		stud_ID.save()
	return render(request,'register.html')
def detail(request):
	return render(request,'detail.html')
def detaiil(request):
	chrome_path ="C:/Users/HP/AppData/Local/Google/Chrome/Application/chrome.exe"
	r= sr.Recognizer()
	with sr.Microphone() as source:
		print("say something\n")
		audio = r.record(source,duration =5)
		try:
			text= r.recognize_google(audio)
			res = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + text+ '&callback=handleResponse')
			soup = bs4.BeautifulSoup(res.text, 'lxml')
			t = str(soup.select('body'))
			author = ""
			title = ""
			lang=""
			publication = ""
			category = ""
			g=len(t)   
			stri =""
#			tl,ll,tc,ta=[],[],[],[]
			l = []
			for i in range(g-10):
				if t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]=='"title"':
					r=i+10
					while(t[r]!='"'):
						title=title+t[r]
						r+=1
				#	tl.append(title)
					if(stri != 'language' and stri != ''):
						l.append('null')
					l.append(title)
					stri = 'title'
					title = ""
				if t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]+t[i+7]+t[i+8]=='"authors"':
					r=i+19

					while(t[r]!='"'):
						author=author+t[r]
						r+=1
				#	ta.append(author)
					if(stri != 'title'):
						l.append('null')
					l.append(author)
					author = ""
					stri = "author"	
				if t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]+t[i+7]+t[i+8]+t[i+9]=="categories":
					r=i+21
					while(t[r]!='"'):
						category=category+t[r]
						r+=1
				#	tc.append(category)
					if(stri != 'author'):
						l.append('null')
					l.append(category)
					category = ''
					stri = "categories"	
				if t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]+t[i+7]=="language":
					r=i+12
					while(t[r]!='"'):
						lang=lang+t[r]
						r+=1
					if(stri != 'categories'):
						l.append('null')
					l.append(lang)
					stri = 'language'
				#	ll.append(lang)
					lang =''
	#		print(len(ta),len(tl),len(ll),len(tc),sep=" ")
			print(l)  
		except Exception as e:
			print(e)	
	return render(request,'detail.html')

def search(request):
    student_name = student_info.objects.all()
    return render(request, 'search.html', {'student_info':student_name})
