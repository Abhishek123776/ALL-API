from rest_framework import serializers
from .models import Contact,Educationdetail,Familydetails,Partnerprefarencedetails


class ContactSerializer(serializers.Serializer):
    mobile_number=serializers.IntegerField()
    alternative_mobile_number=serializers.IntegerField()
    permanent_address=serializers.CharField(max_length=80)
    working_address=serializers.CharField(max_length=80)
    email=serializers.EmailField(max_length=50)

    def create(self, validated_data):
        mobile_number=validated_data['mobile_number']
        alternative_mobile_number=validated_data['alternative_mobile_number']
        permanent_address=validated_data['permanent_address']
        working_address=validated_data['working_address']
        email=validated_data['email']

        obj=Contact(mobile_number=mobile_number,alternative_mobile_number=alternative_mobile_number,permanent_address=permanent_address,working_address=working_address,email=email)
        obj.save()
        return obj
    
    def update(self, instance, validated_data):
        instance.mobile_number=validated_data.get['mobile_number']
        instance.alternative_mobile_number=validated_data.get['alternative_mobile_number']
        instance.permanent_address=validated_data.get['permanent_address']
        instance.working_address=validated_data.get['working_address']
        instance.email=validated_data.get['email']
        instance.save()
        return instance
    
class EducationdetailSerializer(serializers.Serializer):
    emp_id=serializers.IntegerField()
    qualification=serializers.CharField(max_length=40)
    occupations=serializers.CharField(max_length=40)
    annual_income=serializers.FloatField()

    def create(self, validated_data):
        emp_id=validated_data['emp_id']
        qualification=validated_data['qualification']
        occupations=validated_data['occupations']
        annual_income=validated_data['annual_income']

        obj=Educationdetail(emp_id=emp_id,qualification=qualification,occupations=occupations,annual_income=annual_income)
        obj.save()
        return obj
    
    def update(self, instance, validated_data):
        instance.emp_id=validated_data.get['emp_id']
        instance.qualification=validated_data.get['qualification']
        instance.occupations=validated_data.get['occupations']
        instance.annual_income=validated_data.get['annual_income']
        instance.save()
        return instance
    
class FamilydetailsSerializer(serializers.Serializer):
    father_name=serializers.CharField(max_length=40)
    mother_name=serializers.CharField(max_length=40)
    sister_name=serializers.CharField(max_length=40)
    about_family=serializers.CharField(max_length=80)

    def create(self, validated_data):
        father_name=validated_data['father_name']
        mother_name=validated_data['mother_name']
        sister_name=validated_data['sister_name']
        about_family=validated_data['about_family']

        obj=Familydetails(father_name=father_name,mother_name=mother_name,sister_name=sister_name,about_family=about_family)
        obj.save()
        return obj
    
    def update(self, instance, validated_data):
        instance.father_name=validated_data.get['father_name']
        instance.mother_name=validated_data.get['mother_name']
        instance.sister_name=validated_data.get['sister_name']
        instance.about_family=validated_data.get['about_family']
        instance.save()
        return instance
    
class PartnerprefarencedetailsSerializer(serializers.Serializer):
    looking_for=serializers.CharField(max_length=40)
    caste=serializers.CharField(max_length=40)
    qualification=serializers.CharField(max_length=40)
    occupations=serializers.CharField(max_length=40)

    def create(self, validated_data):
        looking_for=validated_data['looking_for']
        caste=validated_data['caste']
        qualification=validated_data['qualification']
        occupations=validated_data['occupations']

        obj=Partnerprefarencedetails(looking_for=looking_for,caste=caste,qualification=qualification,occupations=occupations)
        obj.save()
        return obj
    
    def update(self, instance, validated_data):
        instance.looking_for=validated_data.get['looking_for']
        instance.caste=validated_data.get['caste']
        instance.qualification=validated_data.get['qualification']
        instance.occupations=validated_data.get['occupations']
        instance.save()
        return instance