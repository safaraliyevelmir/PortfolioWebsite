from django import template

register = template.Library()

@register.simple_tag(name="profile_picture")
def profile_picture(person):
    if person:
        return person.profile_picture.url
    else:
        return "https://www.gravatar.com/avatar/404?d=mp"