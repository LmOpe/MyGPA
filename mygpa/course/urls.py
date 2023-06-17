from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('auth/users/activate/<str:uid>/<str:token>', views.activateUsersView, name="activate"),
    path('auth/users/resend-activation-email/', views.resendActivationLinkView, name='resend-activate'),
]