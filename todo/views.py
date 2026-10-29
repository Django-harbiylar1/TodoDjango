import random
from django.shortcuts import render
from django.contrib.auth import get_user_model

from todo.models import Category, Todo

User = get_user_model()


# Create your views here.

def home(request):

    categories = Category.objects.all()
    users = User.objects.all()

    a = random.randint(1,100)
    print(a, '####################################')


    
    return render( request=request, context={'fronta':a, 'categories':categories, 'users': users}, template_name='index.html')
