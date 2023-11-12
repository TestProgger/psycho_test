from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/subject/', include('subject.api.urls')),
    path('api/pst/', include('psycho_test.api.urls'))
]
