from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def librarian_check(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(librarian_check)
def librarian_view(request):
    return HttpResponse("Librarian Content")