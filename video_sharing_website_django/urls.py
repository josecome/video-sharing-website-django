"""video_sharing_website_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from videos import views as video_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', video_views.home, name="home"),
    path('login/', video_views.loginPage, name='login'),
    path('admin/', admin.site.urls),
    path('logout/', video_views.logout_view, name='logout'),
    path('register/', video_views.registrationPage, name='register'),
    path('videos/<int:id>', video_views.video_detail, name="videos"),
    path('studio/', video_views.studio, name="studio"),
    path('api/', include('api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
