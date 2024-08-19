from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def member_check(user):
    return user.userprofile.role == 'Member'

@user_passes_test(member_check)
def member_view(request):
    return render(request, 'member_view.html')