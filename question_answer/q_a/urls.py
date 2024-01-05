from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import HomeView, PythonView ,PythonansView,QA_form

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    # path('python/', PythonView.as_view(), name='python'),
    # path('form',QA_form,name='form'),
    # path('python/<int:x_id>/',PythonansView.as_view(),name='pythonans'),
    path('Questions/',views.Question_list),
    path('Questions/<int:id>/',views.Question_detail),
]
urlpatterns=format_suffix_patterns(urlpatterns)
