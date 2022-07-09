from turtle import title
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , HttpResponse , redirect
from .models import contacts
from django.contrib import messages
from blog.models import post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
# Create your views here.
def home(request):
    # return HttpResponse("home page")
    return render(request,'home/home.html')

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name', '')
        print(name)
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '') # yha name=phone wala
        dsc=request.POST.get('ds', '')
        if len(name)<2 or len(email)<3 or len(phone)<4 or len(dsc)<4 :
            messages.error(request,"Plz Fill The Form Correctaly")
        else:
           contac = contacts(name=name,email=email,phone=phone,msg=dsc)# databse me jo variable he wo = python 
           contac.save()
           messages.success(request,"Your Message Has Been  Successfully Sent")
    return render(request,'home/contact.html')

def about(request):
    messages.success(request,"this is our about")
    return render(request,'home/about.html')

def search(request):
    search = request.GET['search']
    if len(search) > 70 :
        posts = post.objects.none() # empy query
    else:
        poststitle = post.objects.filter(title__icontains=search)
        postscontent = post.objects.filter(content__icontains=search)
        posts = poststitle.union(postscontent) # union can murge
    if len(search) == 0 :
        messages.warning(request,"No search results found. some blogs for you ...")
    if posts.count() == 0 :
        messages.warning(request,"No search results found. Please refine your query.")
    content = {"post":posts, "search":search}
    return render(request,"home/search.html",content)
    # return HttpResponse("hello search here")
    
def handlesinup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lastname = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['password2']
        # eror by user input fix
        if not username.isalnum() :
            messages.error(request,"Username should only contain letters and numbers")
            return redirect("/")
        if len(username) >10 :
            messages.error(request,"Username must be under 10 characters")
            return redirect("/")
        if len(username) <4 :
            messages.error(request,"Username must be at least 5 characters")
            return redirect("/")
        
        if  username in User.objects.all():
            messages.error(request,"this username already taken")
            return redirect("/")
        if password != confirmpassword :
            messages.error(request,"passwords do not match")
            return redirect("/")
        
            
        
        
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request,"Your Legend's Blog account has been successfully created")
        return redirect("/")
    else:
        return HttpResponse('404 - Not Found')
    
def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged in")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("/")
    return HttpResponse("404 - Not Found")

def handlelogout(request):
    logout(request)
    messages.success(request,"successfully loggout in")
    return redirect("/")
    