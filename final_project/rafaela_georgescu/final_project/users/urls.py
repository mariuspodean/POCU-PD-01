from django.urls import include, path
from pages.views import MyLoginView, SignUpView

app_name = 'users'
urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]