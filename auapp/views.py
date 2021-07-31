from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import ProfileModel
from random import randrange
from django.core.mail import send_mail
from Task_Project.settings import EMAIL_HOST_USER

def usignup(request):
	if request.method == "POST":
		un = request.POST.get('un')
		em = request.POST.get('em')
		lo = request.POST.get('lo')
		try:
			usr = User.objects.get(username = un)
			return render(request, 'usignup.html', {'msg':'username already taken'})
		except User.DoesNotExist:
			try:
				usr = User.objects.get(email = em)
				return render(request, 'usignup.html', {'msg':'email already taken'})
			except User.DoesNotExist:
				pw=""
				text = "1234567890"
				for i in range(4):
					pw = pw + text[randrange(len(text))]
				print(pw)
				send_mail("Welcome to Task app ", "your password is " + pw, EMAIL_HOST_USER, [em])
				usr = User.objects.create_user(username = un, password = pw, email = em)
				usr.save()
				pr = ProfileModel(lo=lo, added_by=usr)
				pr.save()
				return redirect('ulogin')
	else:
		return render(request, 'usignup.html')

def ulogin(request):
	if request.method == "POST":
		un = request.POST.get('un')
		pw = request.POST.get('pw')
		usr = authenticate(username = un, password = pw)
		if usr is None:
			return render(request, 'ulogin.html', {'msg':'invalid credentials'})
		else:
			login(request, usr)
			return redirect('home')
	else:
		return render(request, 'ulogin.html')

def ulogout(request):
	logout(request)
	return redirect('ulogin')

def uresetpassword(request):
	if request.method == "POST":
		un = request.POST.get('un')
		em = request.POST.get('em')
		try:
			usr = User.objects.get(username = un) and User.objects.get(email = em)
			pw=""
			text = "1234567890"
			for i in range(4):
				pw = pw + text[randrange(len(text))]
			print(pw)
			send_mail("Welcome to Task app ", "your password is " + pw, EMAIL_HOST_USER, [em])
			usr.set_password(pw)
			usr.save()
			return redirect('ulogin')
		except User.DoesNotExist:
			return render(request, 'uresetpassword.html', {'msg':'invalid username/password'})			
	else:
		return render(request, 'uresetpassword.html')