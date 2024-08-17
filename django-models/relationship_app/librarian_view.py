from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def librarian_check(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(librarian_check)
def librarian_view(request):
    return render(request, 'librarian_view.html')