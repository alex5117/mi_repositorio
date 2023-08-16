from django.urls import path

from miApp import views
urlpatterns = [
    path('stock_limpieza/',views.mostrar_stock_limpieza),
    path('stock_comida/',views.mostrar_stock_comida),
    path('stock_veneno/',views.mostrar_stock_veneno),
    path('stock_pago/',views.mostrar_stock_pago)
]