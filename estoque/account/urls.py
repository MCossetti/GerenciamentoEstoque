from django.urls import path, include
from django.contrib.auth import views as v

urlpatterns = [
    path('login/', v.LoginView.as_view(), name='login'),
    path('logout/', v.LogoutView.as_view(next_page='login'), name='logout'),
    path('password_change/', v.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', v.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', v.PasswordResetView.as_view(success_url='/account/login/'), name='password_reset'),
    path('reset/<uidb64>/<token>', v.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', v.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path('', include('django.contrib.auth.urls')),
]