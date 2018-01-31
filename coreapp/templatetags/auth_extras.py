from django import template
from django.contrib.auth.models import Group

# make tag library valid!
register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
	group =Group.objects.get(name=group_name)
	return group in user.groups.all()

