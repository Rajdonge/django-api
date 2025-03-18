from rest_framework import serializers
from .models import Banner, CV, Project, SocialMedia, Enquiry

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['banner']

class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = ['cv']


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['facebook', 'github', 'linkedin']

class ProjectSerializer(serializers.ModelSerializer):
    project_image = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'
    
    def get_project_image(self, obj):
        if obj.project_image:
            return self.context['request'].build_absolute_uri(obj.project_image.url)
        return None

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ['visitor_name', 'visitor_email', 'visitor_message']
        
