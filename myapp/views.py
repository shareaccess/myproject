from django.shortcuts import render
from django.http import HttpResponse
from sharepoint import SharePointSite, basic_auth_opener

# Create your views here.
def home(request):
    return render(request,'home.html')
def submit(request):
    site_url = request.GET['URL']
    opener = basic_auth_opener(site_url,'thiveya.d@hcl.com','Gokhul1809??')
    site = SharePointSite(site_url,opener)

    return render(request,'result.html',{'result':site})
