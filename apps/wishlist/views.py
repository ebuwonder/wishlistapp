from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from .models import Users, Items

# Create your views here.
def current_user(request):
    if 'user_id' in request.session:
        return Users.objects.get(id=request.session['user_id'])

def index(request):
    return redirect('/main')

def main(request):
    return render(request, 'wishlist/index.html')

def create(request):
    if request.method == 'POST':
        result = Users.objects.validate_registration(request.POST)
        if result['status'] == False:
            #create flash messages
            for error in result['errors']:
                messages.error(request, error)

            #redirect to home page
            return redirect('/main')
        else:
            #put the user_id into session
            request.session['user_id'] = result['user'].id
            return redirect('/success')

def success(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please login to visit your wishlist!')
        return redirect('/')
    else:
        theuser = models.Users.objects.get(id = request.session['user_id'])
        userlist = models.Items.objects.filter(user=theuser)
        allitem = models.Items.objects.exclude(user=theuser).order_by('-added_at')

        context={
            'current_user': current_user(request),
            "theuser" : theuser,
            "items" : userlist,
            'allitem' : allitem

    }

    return render(request, 'wishlist/success.html', context)



    #look up current user


    # context = {
    #     'current_user': current_user(request),
        # 'items' : userlist,
        # 'allitem' : allitem,
    # }


def login(request):
    return render(request, '/main')

def authenticate(request):
    if request.method == 'POST':
        result = Users.objects.validate_login(request.POST)
        if result['status'] == False:
            #generate error message
            messages.error(request, result['error'] )
            return redirect('/main')
        else:
            #save the user_id into session
            request.session['user_id'] = result['user'].id
            return redirect('/success')

def logout(request):
    request.session.flush()
    return redirect('/')



def additem(request):

	return render(request, 'wishlist/additem.html')

def displayitem(request, id):
	if models.Items.objects.filter(id=id):
		theitem = models.Items.objects.get(id=id)
		users = theitem.user.all()
		context = {
			'theitem' : theitem,
			"users" : users
		}
		return render(request, 'wishlist/item.html', context)
	else:
		return redirect('/success')




def additemprocess(request):

	if request.POST:
		theuser = models.Users.objects.get(id = request.session['user_id'])
		print theuser.name
		theitem = models.Items.objects.existitem(item=request.POST['item'], theuser = theuser)
		print theitem

		if theitem == False:
			messages.error(request, 'Item name cannot be blank!')
			return redirect('/additem')

	return redirect('/success')

def deleteitem(request, id):
    # DELETE the item completely from the data
	models.Items.objects.filter(id=id).delete()
	return redirect('/success')

def removeitem(request, id):
	theitem = models.Items.objects.get(id=id)
	theuser = models.Users.objects.get(id = request.session['user_id'])
	removeuser = theitem.user.remove(theuser)

	return redirect('/success')

def addthis(request, id):
	theitem = models.Items.objects.get(id=id)
	theuser = models.Users.objects.get(id = request.session['user_id'])
	removeuser = theitem.user.add(theuser)
	return redirect('/success')
