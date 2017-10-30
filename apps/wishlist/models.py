from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validate_login(self, post):
        user = Users.objects.filter(email=post['email']).first()
        if user and bcrypt.checkpw(post['password'].encode(), user.password.encode()):
            return { 'status': True, 'user': user}
        else:
            return { 'status': False, 'error': 'Invalid credentials' }





    def validate_registration(self, post):
        #step 1: validate the form data
         errors = []
         if post['name'] == '':
             errors.append('Name cannot be blank')
         if post['email'] == '':
             errors.append('Email cannot be blank')
         user = Users.objects.filter(email=post['email']).first()
         if user:
             errors.append('Email already in use')
         if len(post['password']) < 8:
             errors.append('password must be at least eight characters')
         elif post['password'] != post['password_confirmation']:
             errors.append('Passwords do not match')
        #step2: if invalid create error messages
         if not errors:
             user = Users.objects.create(
                name=post['name'],
                email=post['email'],
                password=bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt(10))
             )
             return { 'status': True, 'user' : user }
         else:
             return { 'status': False, 'errors': errors }
        #step3: if valid create the user and the session

#vertify item
class ItemManager(models.Manager):
	def existitem(self, item, theuser):
		if item:
			if Items.objects.filter(item=item):
				theitem = Items.objects.get(item=item)
				addtowish = theitem.user.add(theuser)
			else:
				theitem = Items.objects.create(item=item, creator=theuser)
				addtowish = theitem.user.add(theuser)
			return theitem
		else:
			return False




class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Items(models.Model):
	item = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add = True)
	added_at = models.DateTimeField(auto_now= True)
	creator =  models.ForeignKey('Users', related_name="creator")
	user = models.ManyToManyField('Users', related_name='items')
	objects = ItemManager()
