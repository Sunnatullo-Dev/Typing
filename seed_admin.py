import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typing_site.settings')
django.setup()

from django.contrib.auth.models import User

username = "user"
password = "user"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email="admin@example.com", password=password)
    print(f"Superuser '{username}' created with password '{password}'")
else:
    u = User.objects.get(username=username)
    u.set_password(password)
    u.is_superuser = True
    u.is_staff = True
    u.save()
    print(f"Superuser '{username}' password updated to '{password}'")
