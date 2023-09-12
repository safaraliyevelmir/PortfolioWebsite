from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("resume/", views.resume, name="resume"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path("blog-single/", views.blog_single, name="blog-single"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("portfolio-single/", views.portfolio_single, name="portfolio-single"),
]
