import random
from django.shortcuts import render
from django.contrib.auth import get_user_model

from todo.models import Category, Todo

User = get_user_model()


# Create your views here.

def home(request):

    categories = Category.objects.all() # SELECT * FROM todo_category;
    users = User.objects.all()          # SELECT * FROM auth_user;
    categories_filtered = Category.objects.filter(is_active=True)

    a = random.randint(1,100)
    print(a, '####################################')


    
    return render( request=request, context={'fronta':a, 'categories':categories, 'users': users, 'categories_filtered':categories_filtered}, template_name='index.html')
