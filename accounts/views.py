from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Logo, Banner, CV, SocialMedia, Project, Enquiry
from . serializers import SocialMediaSerializer, ProjectSerializer, EnquirySerializer


class LogoView(APIView):
    def get(self, request):
        try:
            latest_logo = Logo.objects.latest('created_at')
            logo_url = request.build_absolute_uri(latest_logo.logo_image.url)

            return Response({'logo_url': logo_url}, status=status.HTTP_200_OK)
        
        except Logo.DoesNotExist:
            return Response({'error': 'No logo found'}, status=status.HTTP_404_NOT_FOUND)
        
class BannerView(APIView):
    def get(self, request):
        try:
            latest_banner = Banner.objects.latest('created_at')
            banner_url = request.build_absolute_uri(latest_banner.banner.url)
            return Response({'banner_url': banner_url}, status=status.HTTP_200_OK)
        
        except Banner.DoesNotExist:
            return Response({'error': 'No Banner found'}, status=status.HTTP_404_NOT_FOUND)
        
class CVView(APIView):
    def get(self, request):
        try:
            latest_cv = CV.objects.latest('created_at')
            cv_url = request.build_absolute_uri(latest_cv.cv.url)
            return Response({'cv_url': cv_url}, status=status.HTTP_200_OK)
        
        except CV.DoesNotExist:
            return Response({'error': 'No CV found'}, status=status.HTTP_404_NOT_FOUND)
        
class SocialMediaView(APIView):
    def get(self, request):
        # Get the latest social media entry
        social_media = SocialMedia.objects.last()
        if social_media:
            serializer = SocialMediaSerializer(social_media)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "No social media links found."}, status=status.HTTP_404_NOT_FOUND)

class ProjectView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    
class EnquiryView(APIView):
    def post(self, request):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        enquiries = Enquiry.objects.all()
        serializer = EnquirySerializer(enquiries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)