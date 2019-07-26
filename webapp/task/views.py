from django.shortcuts import render, redirect
from .models import Employee
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .forms import EmployeeForm
# Create your views here.

def home_view(request):
    return render(request, "base.html")

def get_emp_details(request):

    data = Employee.objects.all()
    return render(request, 'emp_details.html', {'emp_data': data})

class AddEmployeeView(FormView):

    template_name = 'add_emp.html'
    form_class = EmployeeForm
    success_url = '/task/sucess/'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


def sucess(request):
    return render(request, 'sucess.html')

# def search(request):
#     # import pdb;pdb.set_trace()
#
#     data = Employee.objects.filter(name__contains = 'search_data')
#     print(data)
#
#     return render(request, 'search_emp.html', {'search_data': data})

# def search(request):
#
#     if request.method == 'GET': # If the form is submitted
#
#         search_data = request.GET.get('name')
#         print(search_data)
#         return render(request, 'search_emp.html', {'search_data': search_data})


class CustomerSearch(ListView):
    template_name = 'search_emp.html'
    model = Employee
    context_object_name = 'search_data'

    def get_queryset(self):
        data = Employee.objects.all()
        var_get_search = self.request.GET.get('name')
        # var_get_order_by = self.request.GET.get('order')

        if var_get_search is not None:
            data = data.filter(name=var_get_search)

        # if var_get_order_by is not None:
        #     data = data.order_by(var_get_order_by)

        return data









