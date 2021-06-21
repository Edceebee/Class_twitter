from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from allauth.account.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from twitterApp.forms import PostForm
from twitterApp.models import TwitterPost


# class Home(ListView, CreateView):
#     model = TwitterPost
#     template_name = 'twitterApp/home.html'
#     fields = '__all__'

# def home(request):
#     details = TwitterPost.objects.all()
#     context = {
#         'details': details
#     }
#     return render(request, "twitterApp/home.html", context)


@login_required()
def home(request):
    tweets = []
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            return redirect('home')
    else:
        tweets = TwitterPost.objects.all()
        form = PostForm()
    return render(request, 'home.html', {'form': form, 'tweets': tweets})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
            return render(request, 'signup.html', {'form': form})
