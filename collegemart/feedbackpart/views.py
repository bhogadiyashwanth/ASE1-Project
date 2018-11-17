from django.shortcuts import render,redirect
from . models import Userlog
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def home(request):
    if request.method=='POST':
        name = request.user.username
        comments = request.POST['comments']
        Userlog.objects.create(name=name, comments=comments)
        return redirect('feedbackpart.home')
    else:
        return render(request,'feedbackpart/1.html')
