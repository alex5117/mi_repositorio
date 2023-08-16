from django.shortcuts import render

# Create your views here.
from miApp.models import stock_limpieza, stock_comida,stock_veneno, stock_pago

def mostrar_stock_limpieza(request):
    sl1 = stock_limpieza(producto='lavandina', precio='190', envase='dos litros', stock='si')
    sl2 = stock_limpieza(producto='desodorante de piso', precio='160', envase='dos litros', stock='si')
    sl3 = stock_limpieza(producto='jabon', precio='260', envase='un cuarto', stock='si')
    sl4 = stock_limpieza(producto='desengrasante', precio='360', envase='un litro', stock='no')
    
    return render(request, 'miApp/stock_limpieza.html', {'stock_limpieza':[sl1,sl2,sl3,sl4]})

def mostrar_stock_comida(request):
    sc1 = stock_comida(producto='dogy', precio='560', bolsa='un kilo', stock='no')
    sc2 = stock_comida(producto='pedigri', precio='900', bolsa='un kilo', stock='si')
    sc3 = stock_comida(producto='cooperacion', precio='400', bolsa='un kilo', stock='si')
    sc4 = stock_comida(producto='whiskas', precio='960', bolsa='un kilo', stock='no')

    return render(request, 'miApp/stock_comida.html', {'stock_comida':[sc1,sc2,sc3,sc4]})

def mostrar_stock_veneno(request):
    sv1 = stock_veneno(producto='ratisida', precio='870', envase='cien gramos', stock='si')
    sv2 = stock_veneno(producto='veneno de cucarachas', precio='440', envase='un litro', stock='si')
    sv3 = stock_veneno(producto='veneno de hormigas', precio='240', envase='un litro', stock='no')

    return render(request, 'miApp/stock_veneno.html', {'stock_veneno':[sv1,sv2,sv3]})

def mostrar_stock_pago(request):
    mp1 = stock_pago(efectivo='12', uala='1', mercado_pago='2', banco_provincia='3')
    
    return render(request, 'miApp/stock_pago.html',{'stock_pago'[mp1]} )