from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

# class CategoryListView(APIView):
#     def get(self, request):
#         categorys = Category.objects.all()
#         serializer = CategorySerializer(categorys, many=True)
#         return Response(serializer.data)


# class CategoryDetailView(APIView):
#     def get(self, request, pk):
#         try:
#             category = Category.objects.get(pk=pk)
#         except category.DoesNotExist:
#             return Response({'error': 'category not found'}, status=404)

#         serializer = CategorySerializer(Category)
#         return Response(serializer.data)


# class CreateProductView(APIView):
#     def post(self , request):
#         ser_data = ProductSerializer(data = request.data)
#         if ser_data.is_valid():
#             ser_data.save()
#             return Response(ser_data.data , status = status.HTTP_201_CREATED)
#         return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


# class CreateCategoryView(APIView):
#     def post(self, request):
#         ser_data = CategorySerializer(data=request.data)
#         if ser_data.is_valid():
#             Category.objects.create(name = ser_data.validated_data['name'])
#             return Response(ser_data.data, status=status.HTTP_201_CREATED)
#         return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)




"""
Hint:
    This code is about to Exercise at class but you can see the The codes are above 
    and in that code used to create or read data for Category model.
"""

from .models import Product , Comment
from .serializers import ProductSerializer , CommentSerializer
from django.views import View
from django.http import JsonResponse

from django.shortcuts import render
@api_view(['GET'])
def listProduct(request):
    product = Product.objects.all()
    ser_data = ProductSerializer(instance= product , many= True)
    return Response(ser_data.data)

@api_view(["POST"])
def createProduct(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    confirm_price = request.POST.get('confirm_price')
    if name and price and confirm_price:
        product = Product.objects.create(name=name, price=price , price_confirm = confirm_price)
        return JsonResponse({'message': 'Product created successfully!'})
    else:
        return JsonResponse({'error': 'Invalid data provided.'}, status=400)

class UpdateProduct(APIView):
    def put(self ,request , pk):
        product = Product.objects.get(id = pk)
        ser_data = ProductSerializer(instance= product , data = request.data , partial = True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data)
        return Response(ser_data.errors)

class DelelteProduct(APIView):
    def delete(self , request , pk):
        product = Product.objects.get(id = pk)
        product.delete()
        return Response('deleted')
    

class ListCommentView(APIView):
    def get(self , request):
        comment = Comment.objects.all()
        ser_data = CommentSerializer(instance = comment , many =True)
        return Response(ser_data.data)    


class CreateCommentView(APIView):
    def post(self , request):
        ser_data = CommentSerializer(data = request.data)
        if ser_data.is_valid():
            Comment.objects.create(
                title = ser_data.validated_data['title'],
                text = ser_data.validated_data['text'],
                product_id = ser_data.validated_data['product_id']
            )
            return Response(ser_data.data)
        return Response(ser_data.errors)
    
class HomeView(View):
    def get(self , request):
        return render(request , 'home.html')