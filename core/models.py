from django.db import models

KNOWLEDGE_LEVELS = (
    (3, "Expert"),
    (1, "Good"),
    (0, "Not bad"),
)


class Person(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to="profile_pictures")
    about_me = models.TextField()
    cv = models.FileField(upload_to="cv")
    github_profile = models.URLField()
    linkedin_profile = models.URLField()
    phone_number = models.CharField(max_length=128)
    open_to_work = models.BooleanField(default=False)
    is_freelancer = models.BooleanField(default=False)

    @property
    def open_to_work_text(self):
        return "Yes" if self.open_to_work else "No"
    
    @property
    def is_freelancer_text(self):
        return "Yes" if self.is_freelancer else "No"
    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return f"{self.name} {self.surname}"


class WorkExperience(models.Model):
    company = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    description = models.TextField()

    start_date = models.CharField(max_length=128)
    end_date = models.CharField(max_length=128)


    def __str__(self):
        return f"{self.company} - {self.position}"


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.TextField()

    send_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class EducationExperience(models.Model):
    university = models.CharField(max_length=128)
    degree = models.CharField(max_length=128)
    description = models.TextField()

    start_date = models.CharField(max_length=128)
    end_date = models.CharField(max_length=128)


    def __str__(self):
        return f"{self.university} - {self.degree}"


class Skill(models.Model):
    name = models.CharField(max_length=128)
    level = models.IntegerField(choices=KNOWLEDGE_LEVELS)

    def __str__(self):
        return f"{self.name} - {self.level}"
