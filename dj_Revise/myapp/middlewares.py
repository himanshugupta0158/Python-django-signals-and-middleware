
'''
Note :
+-----------------------------------------+
| Activate this middlware from setting.py |
+-----------------------------------------+
'''

# function based middleware
"""
def my_middleware(get_response):
    print("+-------------------------+")
    print("| One Time Initialization |")
    print("+-------------------------+")
    def my_function(request):
        print("------------------------")
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        print("------------------------")
        return response
    
    return my_function
"""

# Class Based Middleware
class MyMiddleware:
    
    def __init__(self, get_response):    
        print("+-------------------------+")
        print("| One Time Initialization |")
        print("+-------------------------+")
        self.get_response = get_response
        
    def __call__(self,request):
        print("This is before view")
        # print(request)
        response = self.get_response(request)
        # print(response)
        print("This is after view")
        return response

class TurtleMiddleware:
    
    def __init__(self, get_response):    
        print("+--------------------------------+")
        print("| One Time Turtle Initialization |")
        print("+--------------------------------+")
        self.get_response = get_response
        
    def __call__(self,request):
        print("This is Turtle before view")
        # print(request)
        response = self.get_response(request)
        # print(response)
        print("This is Turtle after view")
        return response

class TurtleReturnsMiddleware:
    
    def __init__(self, get_response):    
        print("+----------------------------------------+")
        print("| One Time Turtle Returns Initialization |")
        print("+----------------------------------------+")
        self.get_response = get_response
        
    def __call__(self,request):
        print("This is Turtle Returns before view")
        # print(request)
        response = self.get_response(request)
        # print(response)
        print("This is Turtle Returns after view")
        return response



