from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from mainapp.views import admin_u, user, manager #importing several views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('mainapp.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/admin/', admin_u.Admin_uSignUpView.as_view(), name='admin_signup'),
    path('accounts/signup/manager/', manager.ManagerSignUpView.as_view(), name='manager_signup'),
    path('accounts/signup/user/', user.UserSignUpView.as_view(), name='user_signup'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)