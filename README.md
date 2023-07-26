# Django rest framework
### After install django for use django rest framework you should do it :
- ```python
  pip install djangorestframework
  ```
- Add 'rest_framework' to installed app in settings.py
  ```python
  INSTALLED_APPS = [
    ...
    'rest_framework',
  ]
  ```
### Now you can use Api code in django
## In this exercise we have two apps which are:
```python
  INSTALLED_APPS = [
      ...
      'accounts',
      'product'
    ]
```
## At the first time you should know about request and response and serializeing
- Request : 🔗[Link](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/)
- response : 🔗[Link](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/)
- serializer : 🔗[Link](https://www.django-rest-framework.org/api-guide/serializers/)

### In views.py of product app we wrote api code for (crud) of the product model
- createProduct (function base view)
- listProduct (function base view)
- UpdateProduct (class base view)
- DelelteProduct (class base view)
### In serializers.py we used ModelSerializer because we wanted explain about :
- class Meta in serilizers
- model
- fields
- extra_kwargs
- read_only fields
- ...
### We can write three type of validation in serializers.py for each class:
- Field level :  🔗[Link](https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation)
- objecet level : 🔗[Link](https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation)
- validator : 🔗[Link](https://www.django-rest-framework.org/api-guide/serializers/#validators)
