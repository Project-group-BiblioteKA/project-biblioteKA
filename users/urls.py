from django.urls import path
<<<<<<< HEAD:usuarios/urls.py
from usuarios.views import *
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = []
    
=======
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = []
>>>>>>> 523b0d32b062c118e877927d3271d604fd3b2fdd:users/urls.py
