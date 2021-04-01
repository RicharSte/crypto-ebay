from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegiesterForm 

def register(request):
    if request.method == 'POST':
        form = UserRegiesterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.succes(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegiesterForm()
    return render(request, 'users/registration.html', {'form':form, 'title':'Registration'})