from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="loginrequest"),
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.user_login, name="login"),
    path('profile/', views.user_profile, name="profile"),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('like/<int:id>/',views.liked_video,name='like-video'),
    path('logout/', views.user_logout, name="logout"),
    path('changepassword/', views.user_change_pass, name="changepass"),
    path('changepassword1/', views.user_change_pass1, name="changepass1"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
