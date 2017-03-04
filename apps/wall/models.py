from __future__ import unicode_literals

from django.db import models
from ..users.models import User, UserManager

class Message(models.Model):
	message = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
class Comment(models.Model):
	message_id = models.ForeignKey(Message)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		