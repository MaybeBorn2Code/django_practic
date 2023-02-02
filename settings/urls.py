
from django.contrib import admin
from django.urls import path


from apps.company.views import PenView, QuantityView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pen/',PenView.as_view()),
    path('quantity/', QuantityView.as_view())
]
