# Python-django-signals-and-middleware
- This POC contains Both middleware ,settings and signals demonstration in django.
- There is a file name **Django_signals_notes.ipynb** which contains all notes about django settings, middleware and signals.
- Make sure that you have putted *yourapp_name.apps.yourapp_nameConfig* in installed app.
- If yor using signals put below in your very *YourAppConfig* class as its method.
> signals is file named signals.py in django yourapp folder which contains your django signals code
```
def ready(self) :
        import myapp.signals
```
- Same goes for middleware (There is also a middlwares.py file in your app just like for signals).

### To install Django just paste below in your command prompt (same for your virtual environment if your are using) / any code editor's terminal  :
```
python -m pip install django
```
### if you are using images in your model you may need to install below too :
```
pip install pillow
```
