from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
import re
import bcrypt

def index(request):
	users = User.usermanager.all()
	print "This is the userID session: "
	if 'userID' not in request.session:
		request.session['userID']= 0;
	print request.session['userID']
	context={"users": users}
	return render(request, "login/index.html", context)

def show(request):
	print "This is the userID showwwwww: "
	print request.session['userID']
	user = User.usermanager.get(id=request.session['userID'])
	if user:
		context = { "user" : user}
		return render(request, "login/show.html", context)
	else:
		return redirect('login:not_signed_in')

def edit(request, id):
	print "This is the userID and the url passed id in edit: "
	print request.session['userID']
	print id
	user = User.usermanager.get(id=id)
	bday = str(user.birthday)
	if request.session['userID'] != 0:
		print "user is still logged in"
		context = { "user" : user, "birthday" : bday}
		return render(request, "login/edit.html", context)
	else:
		return redirect('login:not_signed_in')

def update(request, id):
	print "This is the userID update: "
	print request.session['userID']
	request.session['validate'] = ""
	zipC = request.POST['zipC']
	firstName = request.POST['f_name']
	lastName = request.POST['l_name']
	maidenName = request.POST['m_name']
	email = request.POST['reg_email'].lower()
	birthday = request.POST['birthdate']
	user = User.usermanager.get(id=id)
	editUser = User.usermanager.updatePerson(id, zipC, firstName, lastName, maidenName, email, birthday, request)
	if editUser == True:
		return redirect('login:show')
	else:
		context = { "user" : user}
		return render(request, "login/edit.html", context)


def registrationPage(request):
	if "pageClear" not in request.session:
		request.session['pageClear']=True
		request.session['userID']=0
	else:
		request.session['fname_signedIn']=""
	if request.session['pageClear'] ==True:
		clear(request)
	users = User.usermanager.all()
	# print "________________________________*"
	# print type(users)
	# if len(users)>0:
	context={"users": users}
	
	load_index_pg= render(request, "login/registration.html", context)
	clear(request)
	request.session['userID']=0
	return load_index_pg

def register(request):
	print request.POST['birthdate']
	print "how birthday date is passed back"
	request.session['validate'] = ""
	zipC = request.POST['zipC']
	firstName = request.POST['f_name']
	lastName = request.POST['l_name']
	maidenName = request.POST['m_name']
	birthday = request.POST['birthdate']
	email = request.POST['reg_email'].lower()
	password = request.POST['reg_pw']
	confPassword = request.POST['conf_reg_pw']
	user = User.usermanager.registerPerson(zipC, firstName, lastName, maidenName, birthday, email, password, confPassword, request)
	print ":--)"
	print user
	if user == True:
		return redirect('wall:index')
	else:
		return redirect('login:regPage')
	

def login(request):
	entered_email = request.POST['login_email'].lower()
	entered_password = request.POST['login_password']
	user = User.usermanager.login(entered_email, entered_password, request)
	#user returns a tuple with two indexes(exists true/false, the users id if exists TRUE)

	if user == False:
		return redirect('login:index')
	else:
		request.session['userID']=user[1]
		request.session['pageClear']=True
		return redirect('wall:index')
		

def success(request):
	if request.session['userID']== 0:
		return redirect('login:not_signed_in')
	else:
		# signedInUser= User.usermanager.get(id=request.session['userID'])
		# context = {"users":signedInUser}
		return redirect("wall:index")

def destroy(request, id):
	User.usermanager.filter(id=id).delete()
	return redirect('login:regPage')

def clear(request):
	request.session['validate']=""
	request.session['zipC']=""
	request.session['fname']=""
	request.session['lname']=""
	request.session['mname']=""
	request.session['birthday']=""
	request.session['valEmail']=""
	request.session['loginEmail']=""
	request.session['pageClear']=False
	return redirect('login:regPage')

def signout(request):
	request.session['userID']=0
	return redirect('login:index')

def not_signed_in(request):
	return render(request, "login/not_signed_in.html")
	