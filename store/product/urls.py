from django.urls import path
from .views import listProduct , createProduct , UpdateProduct , DelelteProduct ,ListCommentView , CreateCommentView , HomeView 
app_name = 'product'
urlpatterns = [
    path('' , HomeView.as_view() , name = 'home'),
    path('list_product/' , listProduct , name='list-product'),
    path('create_product/' , createProduct , name='create-product'),
    path('update_product/<int:pk>/' , UpdateProduct.as_view() , name='update-product'),
    path('delete_product/<str:pk>/' , DelelteProduct.as_view() , name='delete-prooduct'),
    path('list_comment/' , ListCommentView.as_view(), name='list-comment'),
    path('create_comment/' , CreateCommentView.as_view() , name='create-comment')
]