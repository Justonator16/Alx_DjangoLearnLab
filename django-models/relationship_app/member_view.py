from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def member_check(user):
    return user.userprofile.role == 'Member'

@user_passes_test(member_check)
def member_view(request):
    return HttpResponse("Member Content")