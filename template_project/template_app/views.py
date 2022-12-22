from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'name':'hello world','number':55 }
    return render(request,'template_app/home.html',context)

def other(request):
    return render(request,'template_app/other.html')

def relative(request):
    return render(request,'template_app/relative_url_template.html')