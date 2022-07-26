from django.urls import path
from manual import views

urlpatterns = [
    #Отчеты
    path('report/', views.report, name='report'),
    # Справочник услуг и товаров
    path('product_manual/', views.mainProduct, name='main-product'),
    path('create_product/', views.createProduct, name='create-product'),
    path('product_manual/sort/bydate', views.sortProductDate, name='sort-product'),
    path('product_manual/sort/default', views.sortProductDefault, name='sort-product-default'),
    path('edit_product/<int:pk>/', views.editProduct, name='edit-product'),
    path('delete_product/<int:pk>/', views.deleteProduct, name='delete-product'),
    # Справочник цен
    path('price_manual/', views.mainPrice, name='main-price'),
    path('create_price/', views.createPrice, name='create-price'),
    path('edit_price/<int:pk>/', views.editPrice, name='edit-price'),
    path('delete_price/<int:pk>/', views.deletePrice, name='delete-price'),
    # Справочник объемов продаж
    path('sale_manual/', views.mainSale, name='main-sale'),
    path('create_sale/', views.createSale, name='create-sale'),
    path('edit_sale/<int:pk>/', views.editSale, name='edit-sale'),
    path('delete_sale/<int:pk>/', views.deleteSale, name='delete-sale'),
    # Создание справочника
    path('create_manual/', views.createManual, name='create-manual'),
]
