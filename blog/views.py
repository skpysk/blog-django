from pyexpat.errors import messages
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render , HttpResponse
from .models import post , blogcomment
from django.contrib import messages
from blog.templatetags import extras
from django.core.paginator import Paginator
import math
# Create your views here.
def bloghome(request):
    posts = post.objects.all()
    #  return HttpResponse("blog home here")
    paginator = Paginator(posts, 1) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    print(page_number , 'hello')
  
    postss = paginator.get_page(page_number)
    
    return render(request, "blog/bloghome.html",{'post':postss })

def blogpost(request,slug):
    # return HttpResponse(f"blogpost here: {slug}")
    posts = post.objects.filter(slug=slug).first()
    posts.views = posts.views + 1
    posts.save()
    comment = blogcomment.objects.filter(post2=posts, parent= None)
    replies = blogcomment.objects.filter(post2=posts).exclude(parent=None) # not equals to aise 

    replydic = {}
    for reply in replies :
          if reply.parent.sno not in replydic.keys():
                replydic[reply.parent.sno] = [reply]
          else:
                replydic[reply.parent.sno].append(reply)
              
    return render(request, "blog/blogpost.html",{"post":posts,"comments":comment,"replydic":replydic})
    
def postcomment(request):
    if request.method == "POST":
         comments=request.POST.get('comment')
         user=request.user
         postSno =request.POST.get('postSno')
         posts= post.objects.get(sno=postSno)
         parentSno = request.POST.get('parentSno')
         if parentSno == "":
           comment=blogcomment(comment= comments, user=user, post2=posts)
           comment.save()
           messages.success(request, "Your comment has been posted successfully")
         else:
           parent = blogcomment.objects.get(sno=parentSno)
           comment=blogcomment(comment= comments, user=user, post2=posts , parent=parent)  
            
           comment.save()
           messages.success(request, "Your reply has been posted successfully")
    return redirect(f"/blog/{posts.slug}")
  
def listing(request):
    posts = post.objects.all()
    paginator = Paginator(posts, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})