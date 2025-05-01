from django.test import TestCase
from django.contrib.auth.models import User,Group,Permission
# Create your tests here.



user = User.objects.get(username='admin123')
groups = Group.objects.all()
print("groups", groups)
print(user.groups)