from django.shortcuts import render,redirect
from .models import TaskModel
from django.contrib.auth.models import User
from django.core.mail import send_mail
from Task_Project.settings import EMAIL_HOST_USER
from auapp.models import ProfileModel

def home(request):
	if request.user.is_authenticated:
		pr = ProfileModel.objects.get(added_by_id = request.user.id)
		try:
			city = pr.lo
			a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
			a2 = "&q=" + city
			a3 = "&appid=" + "cb2f054e870da798dcba13a342937ab9"
			wa = a1 + a2 + a3

			res = requests.get(wa)
			data = res.json()
			print(data)
			temp = data['main']['temp']
			desc = data['weather'][0]['description'] #dict of list --> dict
			icon_add = "http://openweathermap.org/img/w/" +data['weather'][0]['icon'] + ".png"
			msg = "city name="+str(city)+" temp="+str(temp)+" desc="+str(desc)
			return render(request,"home.html",{'msg':msg})
		except Exception as e:
			return render(request,"home.html",{'msg':'check city name'})
	else:
		return redirect('ulogin')

def create(request):
	if request.method == "POST":
		t1 = request.POST.get('t1')
		ta = TaskModel(Task = t1, usr_id = request.user.id)
		ta.save()
		return render(request, 'create.html', {'msg':'Task Added'})
	else:
		return render(request, 'create.html')

def view(request):
	data = TaskModel.objects.filter(usr_id = request.user.id)
	return render(request, 'view.html', {'data':data})

def delete(request, id):
	ta = TaskModel.objects.get(pk = id)
	ta.delete()
	return redirect('view')

def feedback(request):
	if request.method == "POST":
		t2 = request.POST.get('t2')
		u = User.objects.get(username = request.user)
		em = u.email
		send_mail("Welcome to task app", "feedback from " + u.username + " " + t2, em, [EMAIL_HOST_USER])
		msg = "Thanks {} for your feedback \n your feedback will be sent to developer via Email".format(u.username)
		return render(request, "feedback.html", {'msg':msg})
	else:
		return render(request, "feedback.html")
