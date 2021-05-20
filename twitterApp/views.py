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


def home(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            return redirect('home')
    else:
        tweets = TwitterPost.objects.all();
        form = PostForm()
    return render(request, 'twitterApp/home.html', {'form': form, 'tweets': tweets})
