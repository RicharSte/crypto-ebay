from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegiesterForm 

def register(request):
    print(request.method)
    if request.method == 'POST':
        form = UserRegiesterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegiesterForm()
    return render(request, 'users/registration.html', {'form':form, 'title':'Registration'})

@login_required
def profile(request):
    return render(request, 'users/profile.html')