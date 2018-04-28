from django.shortcuts import get_object_or_404, render

from .models import Contact


def index(request, username):
    contact = get_object_or_404(Contact, user_name=username)
    return render(request, 'index.html', {'contact': contact})