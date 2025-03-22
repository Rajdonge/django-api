from django.urls import path
from .views import LogoView, BannerView, CVView, SocialMediaView, ProjectView, EnquiryView

urlpatterns = [
    path('logo/', LogoView.as_view(), name='get-logo'),
    path('banner/', BannerView.as_view(), name='get-banner'),
    path('cv/', CVView.as_view(), name='get-cv'),
    path('social-media/', SocialMediaView.as_view(), name='social-media'),
    path('projects/', ProjectView.as_view(), name='projects-list'),
    path('enquiry/', EnquiryView.as_view(), name='enquiry-list'),
]