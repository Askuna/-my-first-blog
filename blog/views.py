from django.shortcuts import render

# Create your views here.
def post_list(reguest):
    return render(reguest, 'blog/post_list.html',{})
