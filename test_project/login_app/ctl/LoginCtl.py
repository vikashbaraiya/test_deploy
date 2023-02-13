
from .BaseCtl import BaseCtl
from django.shortcuts import render, redirect
from login_app.utility.DataValidator import DataValidator
from login_app.models import User



class LoginCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form["login_id"] = requestForm["login_id"]
        self.form["password"] = requestForm["password"]

    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if (DataValidator.isNull(self.form["login_id"])):
            inputError["login_id"] = "Login can not be null"
            self.form["error"] = True
        else:
            if (DataValidator.isemail(self.form['login_id'])):
                inputError['login_id'] = "Login Id must be email"
                self.form['error'] = True

        if(DataValidator.isNull(self.form["password"])):
            inputError["password"] = "Password can not be null"
            self.form["error"] = True

        return self.form["error"]

    def display(self, request, params={}):
        self.form['out'] = params.get("out")
        print("displayyyyy")
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        print("submitttttttt")
        PATH = params.get('path')
        user = self.get_service().authenticate(self.form)
        if(user is None):
            print("submitttttttt noneeee")
            self.form['error'] = True
            self.form["messege"] = "Invalid ID or Password"
            res = render(request, self.get_template(), {"form": self.form})
        else:
            print("LLLLLLLLLLLLL", PATH)
            request.session["user"] = user
            request.session['name'] = user.role_Name
            if PATH is None:
                res = redirect('/LOGIN/Welcome/')
            else:
                res = redirect(PATH)
        return res

    # Template html of Role page
    def get_template(self):
        print("get_templatelogin---")
        return "login.html"

    # Service of Role
    def get_service(self):
        return UserService()

class UserService():
    def authenticate(self, params={}):
        userList = self.search2(params)
        if (userList.count() == 1):
            return userList[0]
        else:
            return None

    def search2(self, params):

        q = User.objects.filter()

        val = params.get("login_id", None)
        if(DataValidator.isNotNull(val)):
            q = q.filter(login_id=val)

        val = params.get("password", None)
        if(DataValidator.isNotNull(val)):
            q = q.filter(password=val)

        return q




