from django.shortcuts import render, redirect
from .models import Message, Comment
from ..users.models import User, UserManager

def index(request):
	message = Message.objects.all()
	comment = Comment.objects.all()
	user = []
	if request.session['userID'] > 0:
		user = User.usermanager.get(id=request.session['userID'])
	print request.session['userID']
	context = {'messages': message,'comments':comment, 'user': user}
	return render(request, "wall/index.html", context)

def message(request):
	if request.method == "POST":
		Message.objects.create(message=request.POST['message'], user = User.usermanager.get(id=request.session['userID']))
	return redirect('wall:index')

def comment(request, id):
	if request.method == "POST":
		the_message = Message.objects.get(id=id)
		Comment.objects.create(comment=request.POST['comment'], message_id=the_message, user = User.usermanager.get(id=request.session['userID']))
	return redirect('wall:index')

def comment_delete(request, id):
	deleteComment= Comment.objects.get(id=id)
	deleteComment.delete()
	return redirect('wall:index')
