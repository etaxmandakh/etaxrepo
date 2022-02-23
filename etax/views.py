from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from django.contrib.auth.models import User
# from .models import Greeting


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, UserSnipSerializer, User123Serializer

from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

class RegisterView(APIView):
    def post(self, request):
        serializer = User123Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')   #.decode('utf-8')
        print(token)
        print(    jwt.decode(token, 'secret', algorithms=['HS256'])   )
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSnipSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSnipSerializer


def init(request):
    # snippet = Snippet(code='foo = "bar"\n')
    # snippet.save()

    # snippet = Snippet(code='print("hello, world")\n')
    # snippet.save()

    snippet = Snippet.objects.get(pk=1)
    

    serializer = SnippetSerializer(snippet)
    # serializer = SnippetSerializer(Snippet.objects.all(), many=True)
    print(JSONRenderer().render(serializer.data))
    # return JsonResponse(serializer.data)
    return Response(serializer.data)
    # return HttpResponse("ok" +  str(JSONRenderer().render(serializer.data)))

@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        serializer = SnippetSerializer(Snippet.objects.all(), many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

def db(request):

    # greeting = Greeting()
    # greeting.save()

    # greetings = Greeting.objects.all()
    return HttpResponse("bba nemlee nemlee")
    # return render(request, "db.html", {"greetings": greetings})

def test(request):
    return HttpResponse("test")







