from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.


posts = [
    {
        'author':'Nikhil S Thomas',
        'title': 'Oppenheimer',
        'director': 'Christopher Nolan',
        'releaseDate': '21 July 2023',
        'description':'During World War II, Lt. Gen. Leslie Groves Jr. appoints physicist J. Robert Oppenheimer to work on the top-secret Manhattan Project. ',
        # 'poster':'./'
    }
]

def home(request):
    context = {'posts':Post.objects.all()}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})

def details(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post':post}
    return render(request, 'blog/details.html', context)
