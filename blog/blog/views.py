from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

def homePage(request):   
    
    return render(request,"index.html")
    
    # return HttpResponse("heloo sanajya  about us  page demo pages ")

def aboutus(request):

   return render(request,"aboutus.html")

def contactus(request):
  
  
    #   candidateName = request.POST.get('name')
     data ={}
     try:
         if request.method=="POST":
             name = request.POST.get('name')
             email = request.POST.get('email')
             
             data ={
                 'Name':name,
                 'Email':email
             }
             
             url ="/about-us/?output ={}".format(data)
             return redirect(url)
     except:
         pass
    
     return render(request,"contact.html",data)
 
 
def service (request):
    return render(request, 'service.html')

def faq (request):
    return  render(request,'faq.html')
