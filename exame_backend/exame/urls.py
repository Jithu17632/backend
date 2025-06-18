from django.urls import path
from .views import SubmitExameResultView,GetAllResultsView,admin_login,signup_view,login_view,check_login,logout_view

urlpatterns = [
    path('submit/',SubmitExameResultView.as_view(),name='submit-exame'),
    path('results/',GetAllResultsView.as_view(),name='get-results'),
    path('admin-login/', admin_login),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('check-login/', check_login, name='check-login'),
    path('logout/',logout_view)
]