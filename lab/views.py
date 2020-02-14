from django.shortcuts import render, redirect,reverse,get_object_or_404
from django.db.models import Q
from .models import Test,UserSession,Subtest
from django.template.loader import get_template
from django.http import HttpResponse
from project.utils import render_to_pdf
from django.views.generic import ListView 


# def create_form(request,pk):

#     detail = get_object_or_404(Patient,pk=pk)
#     tname = detail.test.all()
#     print(tname)
#     if request.method == 'POST':
#         request.session['kathmandu'] = request.POST
#         return redirect('test_bills')
#     return render(request,'detail.html',{'detail':detail,'tname':tname,'dname':dname})
    
    

# def create_test_bills(request):
#     data = request.session.get('kathmandu')
#     print(data['name'])
#     pdf = render_to_pdf('invoice.html',{'name':data['name'],
#         'age':data['age'],
#         'address':data['address'],
#         'gender':data['gender'],
#         'rate':data['rate'],
#         'unit':data['unit'],
#         'results':data['results'],
#         'remarks':data['remarks'],
#         })
#     return HttpResponse(pdf, content_type='application/pdf')

def home(request):
    name = None
    if request.method == 'POST':
        name = request.POST.get('name')
        choices = request.POST.get('choices')
        subtest = request.POST.get('subtest')
        reference = request.POST.get('reference')
        unit = request.POST.get('unit')
        print(choices)
        test = Test()

        subtest = Subtest()
        test.name = name
        subtest.test = Test.objects.get(name=choices)
        subtest.name = subtest
        subtest.unit = unit
        subtest.reference_value = reference
        subtest.save()
        test.save()
        
        # print(name)
        return redirect('home')
    return render(request,'main.html',{})   



# class ListSubsets(ListView):

#     context_object_name = 'tests' # This replace context['tests']
#     model = Test
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super(ListSubsets, self).get_context_data(**kwargs)
#         context['subtest'] = Subtest.objects.all()
#         # context['tests'] = Test.objects.all() # Without prefetch_related
#         return context

#     def post(self, request):
#         post_dict = request.POST.dict()
#         # test = Test.objects.get(id = post_dict['test_id'])
#         subtest = Subtest.objects.all()
#         for subtest in subtest:
#             try:
#                 if str(subtest.test_id) in post_dict:
#                     update = Subtest.objects.get(test = subtest.test_id)
#                     update.selected = True
#                     update.save()
#             except:
#                 print("Doesn't exist.")
#         return self.get(request, *args, **kwargs)


# tests = Test.objects.all()
# subtests = Subtest.objects.all()

def list_subtest(request):
    return{'subtest':Subtest.objects.all(),'test':Test.objects.all()}