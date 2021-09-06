
from django.http.response import JsonResponse 
# Create your views here.
from .models import Post
from django.views.generic import ListView


def post_list(request):
    post_list = Post.objects.all()
    resp = {"postList": list(post_list.values())}
    return JsonResponse(resp)
    
class Post_list_CBV(ListView):
    model = Post