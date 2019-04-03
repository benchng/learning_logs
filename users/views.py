from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def logout_view(request):
    '''Log the user out'''
    logout(request)
    return HttpResponseRedirect(reverse('logs:index'))

def register(request):
    '''Register a new user.'''
    # check whether or not we're responding to a POST request
    # if not we make an instance of UserCreationForm with no initial data
    if request.method != 'POST':
        # If we're responding to a POST request, we make an instance of UserCreationForm based on submitted data
        #Display blank registration form.
        form = UserCreationForm(data=request.POST)
        #If the submitted data is valid, we call the form's save() method to save the username and the hash of the pw & username

    else:
        #Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #save method returns the newly created user object, which we store in new_user
            #when user info is saved we log them in, which is a two step process, call to authenicate with new_username and pw
            #Log the user in and then redirect to home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            #if pw is correct we store it in authenicated_user
            login(request, authenticated_user)
            #creates a valid session of new user
            return HttpResponseRedirect(reverse('logs:index'))
            #registration is success

    context = {'form' : form}
    return render(request, 'register.html', context)