from django.contrib.auth.backends import ModelBackend
from .models import UserSession
from django.contrib.sessions.models import Session

from django.contrib.auth.backends import ModelBackend

class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        if Session.objects.filter(usersession__user__username=username).exists():
            return None
        else:
            user = super().authenticate(request,username=username,password=password)    
            print(user)
        if user:
            request.session.save()
            UserSession.objects.get_or_create(
                user=user,
                session=Session.objects.get(pk=request.session.session_key)
            )
        return user 
