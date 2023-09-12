from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Person, Skill, WorkExperience, EducationExperience
from .forms import ContactForm

def index(request):
    person = Person.objects.first()
    context = {
        "person": person,
        "active_home": "active",
    }
    return render(request, "index.html", context=context)


def resume(request):
    skills = Skill.objects.all()
    work_experiences = WorkExperience.objects.all()
    education_experiences = EducationExperience.objects.all()
    person = Person.objects.first()

    context = {
        "skills": skills,
        "work_experiences": work_experiences,
        "education_experiences": education_experiences,
        "person": person,
        "active_resume": "active",
    }
    return render(request, "resume.html", context=context)


def about(request):
    person = Person.objects.first()
    context = {
        "person": person,
        "active_about": "active",
    }
    return render(request, "about.html", context=context)


def contact(request):
    person = Person.objects.first()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Your message has been sent successfully.")
        return redirect("contact")
    
    context = {
        "person": person,
        "active_contact": "active",
        "form": form,
    }
    return render(request, "contact.html", context=context)


def blog(request):
    return render(request, "blog.html")


def blog_single(request):
    return render(request, "blog-single.html")


def portfolio(request):
    return render(request, "portfolio.html")


def portfolio_single(request):
    return render(request, "portfolio-single.html")
