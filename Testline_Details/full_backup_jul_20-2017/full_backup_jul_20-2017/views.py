from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from Testline_Details.models import Testlines
from Testline_Details.forms import TestlinesForm, UserForm
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils import timezone
#import ldap3

def home(request):
    testline_list = Testlines.objects.all()
    context_dict = {"testline_list":testline_list}
    return render(request,'Testline_Details/home.html',context=context_dict)

def about(request):
    return render(request,'Testline_Details/about.html',context={})

@login_required
def editdetails(request,sbtsid):
    if request.method=='POST':
        sbtsobject = Testlines.objects.get(pk=sbtsid)
        detailsform = TestlinesForm(data=request.POST,instance=sbtsobject)
        if detailsform.is_valid():
            details = detailsform.save(commit=False)
            details.lastmodifiedby = request.user.username
            details.lastmodifiedon = timezone.localtime(timezone.now())
            details.save()
            return redirect('home')
        else:
            return HttpResponse("Something went wrong")    
    else:    
        try:
          sbtsobject = Testlines.objects.get(pk=sbtsid)
          detailsform = TestlinesForm(instance=sbtsobject)
          return render(request,'Testline_Details/editdetails.html',{'form':detailsform,'id':sbtsid})
        except Testlines.DoesNotExist:
            return render(request,'Testline_Details/doesnotexist.html',{})

       
def register(request):
    registered = False
    if request.method =="POST":
        user_form= UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)            
    else:
        user_form = UserForm()
    
    return render(request,'Testline_Details/register.html',{'user_form':user_form,'registered':registered})                


def user_login(request):
    
    next = ""
    if request.GET:
        next=request.GET['next']
    
    
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                if next == "":
                    return HttpResponseRedirect('/Testline_Details/')
                else:
                    return HttpResponseRedirect(next)
            else:
                return HttpResponse("Your account is disabled")
        else:
            return HttpResponse("Invalid login details.<p>Please try again")
    
    else:
        return render(request,'Testline_Details/login.html',{}) 

    
    
    '''
    next = ""
    if request.GET:
        next=request.GET['next']
    
    
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #user=authenticate(username=username,password=password)
    
    ldap_server="10.135.55.17"
    #username = "someuser"
    #password= "somepassword"
    # the following is the user_dn format provided by the ldap server
    user_dn = "employeeNumber=62012420,ou=Internal,ou=People,o=NSN"
    #(uid="+username+")"
    # adjust this to your base dn for searching
    base_dn = "ou=People,o=NSN"
    connect = ldap3.open(ldap_server)
    search_filter = "uid="+username
    try:
        #if authentication successful, get the full user data
        connect.bind_s(user_dn,password)
        result = connect.search_s(base_dn,ldap.SCOPE_SUBTREE,search_filter)
        # return all user data results
        connect.unbind_s()
        print result
    except ldap3.LDAPError:
        connect.unbind_s()
        print "authentication error"
    
    
    
    '''
    
@login_required(login_url='login') 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))                    
