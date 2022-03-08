from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    # a = 10/0
    print("+-------------------+")
    print("| This is Home View |")
    print("+-------------------+")
    return HttpResponse(
        """ 
+-----------------------------------------------------------+ <br>
| This is Home View and we are using middleware | <br>
+-----------------------------------------------------------+
        """
        )