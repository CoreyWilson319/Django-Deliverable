from django.shortcuts import render
from django.http import HttpResponse
posts = [
    {
        'author': 'John Doe',
        'title': 'First Post',
        'content': 'Nice blog Corey keep it up',
    },
    {
        'author': 'Jane Doe',
        'title': 'Agreed',
        'content': 'I agree with John',
    },
    {
        'author': 'Jimmy Doe',
        'title': '!!!!',
        'content': 'Made you look!',
    },
]


def home(request):
    content = {
        'posts': posts
    }
    return render(request, 'blog/home.html', content) # The second paramater is a string of the path of the html file

def about(request):
    return render(request, 'blog/about.html') # Third paramater can be added to send things to the html page
# Create your views here.
