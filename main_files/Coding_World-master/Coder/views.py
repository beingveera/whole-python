from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from Coder.models import signup,login,contact
import smtplib as s
import random as rn 




otp='\0'
lis=['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
        't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(1,7):
    r=rn.randrange(0,62)
    otp=lis[r]+otp   


def Signup(request):
    if request.method == 'POST':
        first_name=request.POST['first']
        last_name=request.POST['second']
        date=request.POST['birth']
        Mail=request.POST['mail']
        Passw=request.POST['pass']
        Cpass=request.POST['cpass']
        obj=s.SMTP('smtp.gmail.com',587)
        obj.starttls()
        obj.login("CodingWorld.User@gmail.com",'9829237552')
        sub="Coding World Sign Up Varification"
        body="Dear {} {} your Coding World Varification Otp is : {}.\n Coding World is a platform where you can learn all programming languages at a one place. Visit our website and become the master of the programming...{}".format(first_name,last_name,otp,"www.codingWorld.com")
        message="Subject:{}\n\n{}".format(sub,body)
        list_address=[Mail]
        obj.sendmail('CodingWorld.User@gmail.com',list_address,message)
        obj.quit()
        ins=signup(fname=first_name,lname=last_name,dob=date,Email=Mail,PassWord=Passw,CPassWord=Cpass)
        ins.save()

    return render(request,'ragister.html')

def Login(request):
    if request.method == "POST":
        OTP=request.POST['otp']
        if OTP in otp:
            print("login")
            return redirect(request,'/')
    return render(request,'login.html')
       


def Contact(request):
    if request.method =="POST":
        email=request.POST['Email']
        mess=request.POST['message']
        ins=contact(mail=email,text=mess)
        ins.save()
        


    return render(request,'contact.html')


def Home(request):
    return render(request,'mainHome.html')


def home(request):
    return render(request,'home.html')


def python_blog(request):
    return render(request,'python_blog.html')

def blog(request):
    return render(request,'blog.html')#blog.html

def c(request):
    return render(request,'c.html')


def python(request):
    return render(request,'pythontest.html')


def djangos(request):
    return render(request,'django.html')

def cplus(request):
    return render(request,'plus.html')

def c(request):
    return render(request,'c.html')

def kotlin(request):
    return render(request,'kotlin.html')

def java(request):
    return render(request,'java.html')

def machine(request):
    return render(request,'machine.html')

def sciense(request):
    return render(request,'sciense.html')

def swift(request):
    return render(request,'swift.html')

def php(request):
    return render(request,'php.html')

def css(request):
    return render(request,'css.html')

def js(request):
    return render(request,'javascript.html')

def html(request):
    
    return render(request,'html5.html')

def c(request):
    return render(request,'c.html')    


def boot(request):
    return render(request,'bootstrap.html')  


def course(request):
    return render(request,'course.html')  


def r(request):
    return render(request,'r.html')  


def flask(request):
    return render(request,'flask.html')  


def editor(request):
    var="<!DOCTYPE html>\n<html>\n<head>\n<title>Title of the page</title>\n</head>\n<body>\n<h1>This is a Heading of page</h1>\n<p>This is a paragraph.</p>\n</body>\n</html>"
    return render(request,'editor.html',{'val':var})


def tech(request):
    return render(request,'tech.html')    

def numpy(request):
    return render(request,'numpy.html')       
    
def pandas(request):
    return render(request,'pandas.html')   

def matplot(request):
    return render(request,'matplotlib.html')   
    
def tkinter(request):
    return render(request,'tkinter.html')   
    
def turtle(request):
    return render(request,'turtle.html')   
    
def pygame(request):
    return render(request,'pygame.html')   
    
def opencv(request):
    return render(request,'opencv.html')   
    
def kivy(request):
    return render(request,'kivy.html')   
    
def data_structure(request):
    return render(request,'data_structure.html')   
    
def data_base(request):
    return render(request,'database.html')   

def web_scrapping(request):
    return render(request,'web_scrapping.html')    

def django_vidoes(request):
    return render(request,'django_vidoes.html')       
    
def flask_vidoes(request):
    return render(request,'flask_vidoes.html')   

def data_sciense(request):
    return render(request,'data_sciense.html')   
    
def basic_modules(request):
    return render(request,'basic_modules.html')   
    
def advanced_modules(request):
    return render(request,'advance_modules.html')   
        
def projects(request):
    return render(request,'projects.html')




def c_sharph_vidoes(request):
    return render(request,'c_sharph.html')   
    
def c_lang_vidoes(request):
    return render(request,'c_vidoes.html')      

def c_plus_vidoes(request):
    return render(request,'c_plus_vidoes.html')   
    
def java_vidoes(request):
    return render(request,'java_vidoes.html')   

def kotlin_vidoes(request):
    return render(request,'kotlin_vidoes.html')   
    
def swift_vidoes(request):
    return render(request,'swift_vidoes.html')      

def golang_vidoes(request):
    return render(request,'go_lang_vidoes.html')   
    
def r_pro_vidoes(request):
    return render(request,'r_pro_vidoes.html')      

def html5_vidoes(request):
    return render(request,'html5_vidoes.html')   
    
def css3_vidoes(request):
    return render(request,'css_vidoes.html')     

def bootstrap_vidoes(request):
    return render(request,'bootstrap_vidoes.html')   
    
def javascript_vidoes(request):
    return render(request,'javascript_vidoes.html')    

def php_vidoes(request):
    return render(request,'php_vidoes.html')   
    
def jquery_vidoes(request):
    return render(request,'jquery_vidoes.html')     

def java_app_vidoes(request):
    return render(request,'java_app_vidoes.html')   
    
def flutter_app_vidoes(request):
    return render(request,'flutter_app_vidoes.html')   

def docker_vidoes(request):
    return render(request,'docker_vidoes.html')   
    
def aws_vidoes(request):
    return render(request,'aws_vidoes.html')   

def react_js_vidoes(request):
    return render(request,'react_js_vidoes.html')   
    
def asp_net_vidoes(request):
    return render(request,'asp_net_vidoes.html')   

def github_vidoes(request):
    return render(request,'github_vidoes.html')   
    
def linux_vidoes(request):
    return render(request,'linux_vidoes.html')   

def ruby_vidoes(request):
    return render(request,'ruby_vidoes.html')   







 






