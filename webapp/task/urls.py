from django.conf.urls import url,include
from .views import get_emp_details,AddEmployeeView,home_view,sucess,CustomerSearch



urlpatterns = [

    # url(r'^app/',index_view),   # function based views
    url(r'empdata/',get_emp_details, name = 'emp_details'),
    url(r'add_emp/', AddEmployeeView.as_view(), name="add_emp"),
    url(r'home/', home_view, name="home"),
    url(r'sucess/', sucess, name='sucess'),

    # url(r'search_emp/',search, name='search_emp'),

    url(r'search_emp/',CustomerSearch.as_view(), name='search_emp')


    # url(r'search/',AccountList.as_view())

]