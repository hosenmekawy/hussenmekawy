from django.contrib import admin
from django.urls import path , include

import products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/' , include('products.urls'))
]
