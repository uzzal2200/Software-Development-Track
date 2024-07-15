from django.shortcuts import render
from posts.models import Post
def home(request):
    data = Post.objects.all()
    print(data)
    return render(request,'index.html',{'data': data})