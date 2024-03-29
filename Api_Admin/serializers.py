from rest_framework import serializers
from django.contrib.auth.models import User
from Api_Admin.models import Contact, Category, Product
from phonenumber_field.serializerfields import PhoneNumberField

# Add Contact information Serializer
class AddContactSerializer(serializers.ModelSerializer):
    mobile = PhoneNumberField(region="IN")
    class Meta:
        model = Contact
        fields = ['user', 'address','mobile']

    def create(self, validated_data):
        user = self.validated_data['user'] 
        address = self.validated_data['user'] 
        mobile = self.validated_data['user'] 
        if Contact.objects.filter(user=user).exists():
            raise serializers.ValidationError('User with contact information is already exist')
        elif Contact.objects.filter(address=address).exists():
            raise serializers.ValidationError('User with this contact already exist')
        else:
            contact = Contact.objects.create(**validated_data)
            return contact

# List Contact Information Serializer
class ListContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','user','address','mobile']

    def to_representation(self, instance):
        rep = super(ListContactSerializer,self).to_representation(instance)
        rep['user'] = instance.user.username
        return rep

# Add Category Serializer
class AddCatergorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

    def create(self, validated_data):
        category_name = self.validated_data['category_name']
        category = Category.objects.create(**validated_data)
        return category

# Add Product serializer
class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category','product_name','description','price','stock','available','picture','offer']

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product

# Edit Product Serializer
class EditProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'description','price','stock','available', 'picture','offer']

# Delete Prodcut Serializer
class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'