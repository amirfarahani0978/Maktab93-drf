from rest_framework import serializers
from .models import Product , Comment

# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     price = serializers.IntegerField(write_only = True)
#     price_confirm = serializers.IntegerField(write_only = True)
#     def validate_name(self, value):
#         """
#         Check that the blog post is about Django.
#         """
#         if value =="kala9":
#             raise serializers.ValidationError("Please use the other name")
#         return value
#     def validate(self, data):
#         if data['price'] != data['price_confirm']:
#             raise serializers.ValidationError("price did'nt equal price_confirm")
#         return data


# class CommentSerializer(serializers.ModelSerializer):
#     # product_id = serializers.SlugRelatedField(read_only = True,slug_field='price')
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         extra_kwargs ={
#             'product_id':{
#                 'write_only':True
#             }
#         }

"""
That codes are above,used in the first of class about drf , please search about
****
relationField
****
"""

class ProductSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'price_confirm':{
                'write_only':True
            }
        }
    def get_comment(self , obj):
        data = obj.products.all()
        return CommentSerializer(instance= data , many = True).data
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs ={
            'product_id':{
                'write_only':True
            }
        }


