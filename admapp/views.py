from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests

def login(request):
    return render(request,'login.html')

def accept(request):
    if request.method=='POST':
        admin_id=request.POST['admin_id']
        password=request.POST['password']
        r=requests.post('https://cosc-api.herokuapp.com/login',data={'admin_id':admin_id,'password':password})
        p=r.json()['message']
    if p=="ALLOW ACCESS !!":
        return render(request,'admpage.html')
    else:
        content={"message":"Invalid Credentials"}
        return render(request,'login.html',content)

def adm(request):
    return render(request,'addcc.html')


def addcc(request):
    if request.method=='POST':
        name=request.POST['name']
        roll_no=request.POST['roll_no']
        club_id=request.POST['club_id']
        ph_no=request.POST['ph_no']
        email=request.POST['email'] 
        re=requests.post('https://cosc-api.herokuapp.com/addcc',data={'name':name,'roll_no':roll_no,'club_id':club_id,'ph_no':ph_no,'email':email})
        pp=re.json()['message']
        print(pp)
        if pp=="Succesfully sent a email given!":
            return render(request,'admpage.html')
        else:
            return render(request,'addcc.html')