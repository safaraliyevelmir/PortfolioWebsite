from django import template

register = template.Library()

@register.simple_tag(name="profile_picture")
def profile_picture(person):
    return person.profile_picture.url