from sqlite3 import connect
from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import (
    pre_init,
    pre_save,
    pre_delete,
    post_init,
    post_save,
    post_delete,
    pre_migrate,
    post_migrate,
)
from django.core.signals import (
    request_started,
    request_finished,
    got_request_exception
)
# db wrapper
from django.db.backends.signals import connection_created

# login receiver
# method 2 to connect signal to receiver
@receiver(user_logged_in, sender=User)
def login_success(sender,request,user, **kwargs):
    print("--------------------------------")
    print("Logged-in Signal... Run Intro..")
    print("Sender : ",sender)
    print("Request : ",request)
    print("User : ",user)
    print(f'kwargs : {kwargs}')
    

# connecting receiver to signal

# method 1 to connect signal to receiver
# user_logged_in.connect(login_success, sender=User)

# logout receiver

# method 2 to connect signal to receiver
@receiver(user_logged_out, sender=User)
def logging_out(sender,request,user, **kwargs):
    print("--------------------------------")
    print("Logged-out Signal... Run Outro..")
    print("Sender : ",sender)
    print("Request : ",request)
    print("User : ",user)
    print(f'kwargs : {kwargs}')


# method 1 to connect signal to receiver
# user_logged_in.connect(logging_out, sender=User)

# login failed receiver

# method 2 to connect signal to receiver
@receiver(user_login_failed)
def login_failed(sender,credentials,request, **kwargs):
    print("--------------------------------")
    print("Login-failed Signal... ")
    print("Sender : ",sender)
    print("Credentials : ",credentials)
    print("Request : ",request)
    print(f'kwargs : {kwargs}')


# method 1 to connect signal to receiver
# user_logged_in.connect(login_failed)

# model signals

"""@receiver(pre_save, sender=User)
def at_begin_save(sender, instance, **kwargs):
    print("--------------------------------")
    print("Pre-Save Signal... ")
    print("Sender : ",sender)
    print("Credentials : ",instance)
    print(f'kwargs : {kwargs}')
    """

# method 1 to connect signal to receiver
# pre_save.connect(at_begin_save, sender=User)

"""@receiver(post_save, sender=User)
def at_ending_save(sender, instance,created ,**kwargs):
    if created :
        print("--------------------------------")
        print("Post-Save Signal... ")
        print("New Record")
        print("Sender : ",sender)
        print("Created : ",created)
        print("Credentials : ",instance)
        print(f'kwargs : {kwargs}')
    else :
        print("--------------------------------")
        print("Post-Save Signal... ")
        print("Update Record")
        print("Sender : ",sender)
        print("Credentials : ",instance)
        print("Created : ",created)
        print(f'kwargs : {kwargs}')
    
"""
"""
NOTE : sender = User, User denotes model not specifically User
in place of that any model like POst,Product ,Profile ,..etc
can be put there from .models
"""

# method 1 to connect signal to receiver
# post_save.connect(at_ending_save, sender=User)
"""
@receiver(pre_delete, sender=User)
def at_begin_delete(sender, instance, **kwargs):
    print("--------------------------------")
    print("Pre_delete Delete... ")
    print("Sender : ",sender)
    print("Credentials : ",instance)
    print(f'kwargs : {kwargs}')
    

# method 1 to connect signal to receiver
# pre_delete.connect(at_begin_delete, sender=User)


@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print("--------------------------------")
    print("At Ending Delete... ")
    print("Sender : ",sender)
    print("Credentials : ",instance)
    print(f'kwargs : {kwargs}')
    

# method 1 to connect signal to receiver
# post_delete.connect(at_ending_delete, sender=User)


@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("--------------------------------")
    print("Pre Init Signal... ")
    print("Sender : ",sender)
    print(f"Args : {args}")
    print(f'kwargs : {kwargs}')
    

# method 1 to connect signal to receiver
# pre_init.connect(at_beginning_init, sender=User)



@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print("--------------------------------")
    print("Post Init Signal... ")
    print("Sender : ",sender)
    print(f"Args : {args}")
    print(f'kwargs : {kwargs}')
    
# method 1 to connect signal to receiver
# post_init.connect(at_ending_init, sender=User)


@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print("--------------------------------")
    print("At Beginning Request... ")
    print("Sender : ",sender)
    print("Environ : ",environ)
    print(f'kwargs : {kwargs}')
    
# method 1 to connect signal to receiver
# request_started.connect(at_beginning_request)

"""

"""@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print("--------------------------------")
    print("At Ending Request... ")
    print("Sender : ",sender)
    print(f'kwargs : {kwargs}')
    
# method 1 to connect signal to receiver
# request_finished.connect(at_ending_request)

@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print("--------------------------------")
    print("At Request Exception... ")
    print("Sender : ",sender)
    print("Request : ",request)
    print(f'kwargs : {kwargs}')
    """
# method 1 to connect signal to receiver
# got_request_exception.connect(at_req_exception)

"""@receiver(pre_migrate)
def before_install_app(sender,app_config, verbosity,interactive,
using,plan,apps, **kwargs):
    print("--------------------------------")
    print("Before_install_app... ")
    print("Sender : ",sender)
    print("App_config : ",app_config)
    print("Verbosity : ",verbosity)
    print("Interactive : ",interactive)
    print("Using : ",using)
    print("Plan : ",plan)
    print("Apps : ",apps)
    print(f'kwargs : {kwargs}')"""
    
# method 1 to connect signal to receiver
# pre_migrate.connect(before_install_app)

"""@receiver(post_migrate)
def at_end_migrate_flush(sender,app_config, verbosity,interactive,
using,plan,apps, **kwargs):
    print("--------------------------------")
    print("at_end_migrate_flush... ")
    print("Sender : ",sender)
    print("App_config : ",app_config)
    print("Verbosity : ",verbosity)
    print("Interactive : ",interactive)
    print("Using : ",using)
    print("Plan : ",plan)
    print("Apps : ",apps)
    print(f'kwargs : {kwargs}')"""
    
# method 1 to connect signal to receiver
# post_migrate.connect(at_end_migrate_flush)

@receiver(connection_created)
def conn_db(sender,connection, **kwargs):
    print("--------------------------------")
    print("Initial connection to the database ... ")
    print("Sender : ",sender)
    print("Connection : ",connection)
    print(f'kwargs : {kwargs}')

# method 1 to connect signal to receiver
# connection_created.connect(conn_db)
