from django.db import models

from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    login_id = models.EmailField()
    password = models.CharField(max_length=20)
    confirmpassword = models.CharField(max_length=20, default='')
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50, default = '')
    gender = models.CharField(max_length=50,default='')
    mobilenumber = models.CharField(max_length=50,default='')
    role_Id = models.IntegerField()
    role_Name = models.CharField(max_length=50)

    def to_json(self):
        data = {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'login_id': self.login_id,
            'password': self.password,
            'confirmpassword': self.confirmpassword,
            'dob': self.dob,
            'address': self.address,
            'gender': self.gender,
            'mobilenumber': self.mobilenumber,
            'role_Id': self.role_Id,
            'role_Name': self.role_Name
        }

        return data

    class Meta:
        db_table = 'AWS_USER'


