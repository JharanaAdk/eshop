from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('category', views.catview, name="category"),
    path('category/<str:slug>/', views.categoryproduct, name="categoryproduct"),
    path('product/<str:cat_slug>/<str:prod_slug>/', views.productview, name="productview"),


    # search function url
    path('product-list', views.productlistAjax),
    path('searchproduct', views.searchproduct, name="searchproduct")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

