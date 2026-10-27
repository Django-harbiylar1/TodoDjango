import random
from django.shortcuts import render


# Create your views here.

def home(request):

    a = random.randint(1,100)
    print(a, '####################################')

    
    return render( request=request, context={'fronta':a}, template_name='index.html')
