from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from products.controller import cart

urlpatterns = [
    path('', views.home, name="home"),
    path('category', views.catview, name="category"),
    path('category/<str:slug>/', views.categoryproduct, name="categoryproduct"),
    path('product/<str:cat_slug>/<str:prod_slug>/', views.productview, name="productview"),


    # search function url
    path('product-list', views.productlistAjax),
    path('searchproduct', views.searchproduct, name="searchproduct"),

    # cart function url
    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

