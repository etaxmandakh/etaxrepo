from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
# from .models import Greeting


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # u = User(password="123", is_superuser=True, username="bat", first_name="jojo", last_name="jojo1", email='bb@gmail.com', is_staff=True,  is_active=True)
    # u.save()
    # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    # user.is_staff = True
    # user.save()
    return HttpResponse("aabb")
    # return render(request, "index.html")


def db(request):

    # greeting = Greeting()
    # greeting.save()

    # greetings = Greeting.objects.all()
    return HttpResponse("bba")
    # return render(request, "db.html", {"greetings": greetings})

def test(request):
    return HttpResponse("test")







