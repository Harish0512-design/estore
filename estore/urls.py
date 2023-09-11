"""
URL configuration for estore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework_swagger.views import get_swagger_view

from estore import settings

schema_view = get_swagger_view(title='E-store API', url='product/')

urlpatterns = [
                  path('docs/', schema_view),
                  path('admin/', admin.site.urls),
                  path('product/', include('product.urls')),
                  path('api/accounts/', include('authemail.urls')),
              ] + static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
