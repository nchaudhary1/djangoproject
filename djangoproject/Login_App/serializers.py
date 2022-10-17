from rest_framework import serializers

from .models import Student

#class StudentSerializer(serializers.Serializer):
 #   name = serializers.CharField()
  #  course = serializers.CharField()
 #   college = serializers.CharField()

# model Serializer.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','course','college']