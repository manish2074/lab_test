from django.shortcuts import render, redirect,reverse
from .models import Test,UserSession,Subtest,Patient
from django.template.loader import get_template
from django.http import HttpResponse
from project.utils import render_to_pdf




def home(request):
    name = None
    if request.method == 'POST':
        form_type = request.POST.get('form_type')    
        if form_type == "first-form":
            name = request.POST.get('name')
            test = Test()
            test.name = name
            print(name)
            test.save()
        elif form_type == "second-form": 
            choices = request.POST.get('choices')
            subtest = request.POST.get('subtest')
            reference = request.POST.get('reference')
            unit = request.POST.get('unit')
            
            sub = Subtest()
            sub.test = Test.objects.get(name=choices)
            sub.name = subtest
            sub.unit = unit
            sub.reference_value = reference
            sub.save()
        return redirect('home')
        
    elif  request.method == 'GET':
        form_type = request.GET.get('form_type')
        if form_type == 'third-form':
            selected = request.GET.getlist('selected')
            print(selected)
            url = reverse('report')+'?selected=%s&form_type=third-form' % (selected)  
            return redirect(url)
    return render(request,'main.html',{})     

def create_test_bills(request):
    if request.method == 'GET':
        selected = request.GET.getlist('selected')
        sub_test = Subtest.objects.filter(name__in=selected)
        # link = reverse('test_bills')+'?selected=%s' % (selected)
        # return redirect(link)
    return render(request,'report.html',{'sub_test':sub_test})    

# def detail_view(request,pk):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         gender = request.POST.get('gender')
#         detail = Patient()
#         detail.name = name
#         detail.age = age
#         detail.address = address
#         detail.gender = gender
#         detail.contact = contact
#         detail.save()
#     return render(request,'detail.html')    
# def print_test(request):
#     if request.method == 'GET':
#         sub_test = request.GET.getlist('sub_test')
#     pdf = render_to_pdf('invoice.html',{'sub_test':sub_test})
#     return HttpResponse(pdf, content_type='application/pdf')


def list_subtest(request):
    return{'subtest':Subtest.objects.all(),'test':Test.objects.all()}