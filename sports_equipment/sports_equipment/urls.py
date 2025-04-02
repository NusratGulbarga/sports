from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipment/', include('equipment.urls')),  # Include the equipment app's URLs

    # Add a root URL that redirects to the equipment list view
    path('', lambda request: redirect('equipment_list')),  # Redirect root to equipment list
]
