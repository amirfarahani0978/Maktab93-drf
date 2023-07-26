from rest_framework import serializers

def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('amin mustnt be in admin')

"""
Write_only & read_only
"""
# class UserRegisterSerializers(serializers.Serializer):
#     first_name = serializers.CharField(required = True)
#     password = serializers.CharField(required = True , write_only = True)
#     password2 = serializers.CharField(required = True , write_only = True)
#     email = serializers.CharField(required = True , validators = [clean_email])


#     def validate_first_name(self,value):
#         if value == 'admin':
#             raise serializers.ValidationError('first_name cant be admin')
#         return value
    
#     def validate(self, data):
#         if data['password'] != data['password2']:
#             raise serializers.ValidationError('passwords must match')
#         return data



""""
use the modelserializer:

and overwrite the create object for model:

"""
from django.contrib.auth.models import User
class UserRegisterSerializers(serializers.ModelSerializer):
    # first_name = serializers.CharField(required = True)
    # password = serializers.CharField(required = True , write_only = True)
    password2 = serializers.CharField(write_only = True , required = True)
    # email = serializers.CharField(required = True , validators = [clean_email])
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password' , 'password2']
        #fields = ('username' , 'email' , 'password' , 'password2')
        extra_kwargs = {
            'password':{
                'write_only' :True
            },
            'email':{
                'validators':[clean_email]
            }
        }
    def create(self , validatad_data):
        del validatad_data['password2']
        return User.objects.create_user(**validatad_data)

    def validate_username(self,value):
        if value == 'admin':
            raise serializers.ValidationError('first_name cant be admin')
        return value
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords must match')
        return data