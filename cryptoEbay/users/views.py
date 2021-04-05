from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView

from products.models import Product

from .forms import(
    UserRegiesterForm,
    UserUpdateForm,
    ProfileUpdateForm
)

def register(request):
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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES,
                                   instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/profile.html', context)

class UserItemListView(ListView):
   model = Product
   template_name = 'users/user_post.html'
   context_object_name = 'items'
   paginate_by = 5 
   
   def get_queryset(self):
       user = get_object_or_404(User, username=self.kwargs.get('username'))
       return Product.objects.filter(author=user)