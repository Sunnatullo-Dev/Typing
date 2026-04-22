import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typing_site.settings')
django.setup()

from django.contrib.auth.models import User

# ✅ Xavfsiz: Parolni muhit o'zgaruvchisidan olish
username = os.environ.get("SEED_ADMIN_USERNAME", "admin")
password = os.environ.get("SEED_ADMIN_PASSWORD", "")
email    = os.environ.get("SEED_ADMIN_EMAIL", "admin@example.com")

if not password:
    import secrets
    password = secrets.token_urlsafe(16)
    print(f"[seed_admin] Auto-generated password: {password}")
    print("[seed_admin] SEED_ADMIN_PASSWORD env o'zgaruvchisini o'rnatish tavsiya qilinadi!")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' yaratildi.")
else:
    u = User.objects.get(username=username)
    u.set_password(password)
    u.is_superuser = True
    u.is_staff = True
    u.save()
    print(f"Superuser '{username}' yangilandi.")
