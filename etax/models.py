from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

class Alltables(models.Model):
    craetedDate = models.DateTimeField("date created", null=True, blank=True)
    deletedDate = models.DateTimeField("date created", null=True, blank=True)
    class Meta:
        abstract = True

class PayerType(Alltables):
    typeName = models.CharField(max_length=200)

class Roles(Alltables):
    rolename = models.CharField(max_length=200)

class T_aimag(models.Model):
    aimagCode = models.CharField(max_length=2)
    aimagName = models.CharField(max_length=100)
    aimagDaraalal = models.IntegerField(default=0)

class T_sum(models.Model):
    aimag = models.ForeignKey(T_aimag, on_delete=models.CASCADE)
    sumCode = models.CharField(max_length=4)
    sumName = models.CharField(max_length=100)
    sumDaraalal = models.IntegerField(default=0)

class T_chiglel(models.Model):
    chiglelName = models.CharField(max_length=250)
    chiglelDaraalal = models.IntegerField(default=0)

class Payer(Alltables):
    payerType = models.ForeignKey(PayerType, on_delete=models.CASCADE)
    payername = models.CharField(max_length=200)
    regnum = models.CharField(max_length=30)
    sitdate = models.DateTimeField("sitdate created", null=True, blank=True)
    roleid = models.ForeignKey(Roles, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

    payerNum = models.CharField(max_length=11)
    lastname  = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    aimagNum = models.ForeignKey(T_aimag, on_delete=models.CASCADE,default=1)
    sumNum = models.ForeignKey(T_sum, on_delete=models.CASCADE)
    chiglelNum = models.ForeignKey(T_chiglel, on_delete=models.CASCADE,default=1)
    phone = models.CharField(max_length=200)
    regdate = models.DateTimeField("regdate created", null=True, blank=True)

class Logs(Alltables):
    servicename = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    logtype = models.CharField(max_length=200)

class Pages(Alltables):
    pagename = models.CharField(max_length=200)
    role2Page = models.ManyToManyField(Roles, through='Role2Page')

class Perm(models.Model):
    permname = models.CharField(max_length=200)

class Role2Page(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    page = models.ForeignKey(Pages, on_delete=models.CASCADE)
    perm = models.ForeignKey(Perm, on_delete=models.CASCADE)




















