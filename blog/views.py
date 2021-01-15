from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post
# posts = [
#     {
#         'author': 'John Doe',
#         'title': 'First Post',
#         'content': 'Nice blog Corey keep it up',
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Agreed',
#         'content': 'I agree with John',
#     },
#     {
#         'author': 'Jimmy Doe',
#         'title': '!!!!',
#         'content': 'Made you look!',
#     },
# ]


def home(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})
    # return render(request, 'blog/home.html', content) # The second paramater is a string of the path of the html file

def about(request):
    return render(request, 'blog/about.html') # Third paramater can be added to send things to the html page

def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/show.html', {'post': post})

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = ''

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/')

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/')

class PostDelete(DeleteView):
    model = Post
    success_url = '/'


def profile(request, username):
  user = User.objects.get(username=username)
  posts = Post.objects.filter(user=user)
  return render(request, 'profile.html', {'username': username, 'posts': posts})




# Create your views here.
