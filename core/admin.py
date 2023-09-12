from django.contrib import admin
from core.models import Person, WorkExperience, EducationExperience, Skill, Contact

admin.site.site_header = "My Portfolio"
admin.site.site_title = "My Portfolio Admin Portal"
admin.site.index_title = "Welcome to My Portfolio Admin Portal"


admin.site.register(Person)
admin.site.register(WorkExperience)
admin.site.register(EducationExperience)
admin.site.register(Skill)
admin.site.register(Contact)
