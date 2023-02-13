from django.shortcuts import render

# Create your views here.


from .ctl.BaseCtl import BaseCtl
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.sessions.models import Session


from .ctl.LoginCtl import LoginCtl
from .ctl.WelcomeCtl import WelcomeCtl

from django.contrib.auth.decorators import login_required



@csrf_exempt
def actionId(request, page="", operation="", id=0):
    path = request.META.get('PATH_INFO')
    print("VVVVVVVVVVVVVVVV", path)
    if request.session.get('user') is not None and page != "":
        ctlName = page + "Ctl()"
        ctlObj = eval(ctlName)
        request.session['msg'] = None
        res = ctlObj.execute(request, {"id": id})
    elif page == "Registration":
        ctlName = "Registration" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id})
    elif page == "Home":
        ctlName = "Home" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id})
    elif page == "ForgetPassword":
        ctlName = "ForgetPassword" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id})
    elif page == "Login":
        ctlName = page + "Ctl()"
        ctlObj = eval(ctlName)
        request.session['msg'] = None
        print("MMMMMMMMMMM", request.session.get('msg'))
        res = ctlObj.execute(request, {"id": id, })
    else:
        ctlName = "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        request.session['msg'] = "Your Session has been Expired, Please Login again"
        res = ctlObj.execute(request, {"id": id, 'path': path})
    return res


@csrf_exempt
def auth(request, page="", operation="", id=0):
    global res
    if page == "Logout":
        Session.objects.all().delete()
        request.session['user'] = None
        out = "LOGOUT SUCCESSFULL"
        ctlName = "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id, "operation": operation, 'out': out})

    elif page == "ForgetPassword":
        ctlName = "ForgetPassword" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id, "operation": operation})
    return res

def index(request):
    res = render(request, 'project.html')
    return res
