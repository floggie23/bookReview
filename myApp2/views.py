
from django.shortcuts import render , redirect ,HttpResponse
from django.contrib import messages 
import bcrypt
from .models import *

def index(request):
    context = {
        "User": User.objects.get(id=request.session['userid']),
        "books": Book.objects.all
    }
    return render(request, "index.html", context)
def login(request):
    if "userid" in request.session :
        id=request.session['userid']
        return redirect("/")
    return render(request, "login.html")
def create(request):
    
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/login")
    else :
        password=request.POST['pass']
        re_pass =request.POST['re_pass']
        if password==re_pass :
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            print(pw_hash) 
            user= User.objects.create(first_name=request.POST['name'],email=request.POST['email'],last_name=request.POST['last_name'],password=pw_hash)
        return redirect("/login")
def signin(request):
    user = User.objects.filter(email=request.POST['email2'])
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password2'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/')
    return redirect("/login")
def logout(request):
    request.session.flush()
    return redirect("/login")
def booksadd(request):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "authors" :Author.objects.all()
    }
    return render(request, "addBook.html", context)
def bookCreate(request):
    book= Book.objects.create(title=request.POST['title'],user_id=request.session['userid'],desc=request.POST['desc'])
    review=Review.objects.create(text=request.POST['review'],book_id=book.id,rate=request.POST['rate'],user_id=request.session['userid'])
    author= Author.objects.create(name=request.POST['addauthor'])
    author.book.add(book)
    return redirect("/books/"+str(book.id))
def bookView(request,id):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "book" :Book.objects.get(id=id),
        "authors":Author.objects.all()
    }
    return render(request, "books.html", context)
def addReview(request,id):
    review=Review.objects.create(text=request.POST['review'],book_id=id,rate=request.POST['rate'],user_id=request.session['userid'])
    return redirect("/books/"+str(id))
def user(request,id):
    context = {
        "user": User.objects.get(id=id),
    }
    return render(request, "user.html", context)


