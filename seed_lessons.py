import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typing_site.settings')
django.setup()

from typingapp.models import Lesson

SAMPLE_LESSONS = [
  {
    "id": "1",
    "title": "Home Row Basics",
    "description": "Learn the home row keys: f, j, d, k",
    "content": "f j f j d k d k fj dk fj dk fjd kfjd kfjd k",
    "level": 1,
    "duration": 30,
  },
  {
    "id": "2",
    "title": "The Rest of the Home Row",
    "description": "Learn a, s, l, ; keys",
    "content": "a s l ; a s l ; as l; as l; asdf jkl; asdf jkl;",
    "level": 1,
    "duration": 30,
  },
  {
    "id": "3",
    "title": "Common Words",
    "description": "Practice common short words",
    "content": "the and for are but not you all any can had",
    "level": 2,
    "duration": 45,
  },
  {
    "id": "4",
    "title": "Sentence Practice",
    "description": "Type full sentences with punctuation",
    "content": "The quick brown fox jumps over the lazy dog.",
    "level": 3,
    "duration": 60,
  },
  {
    "id": "5",
    "title": "Top Row Intro",
    "description": "Learn the top row keys: e, i, r, u",
    "content": "e i r u e i r u er iu er iu rei uie rei uie",
    "level": 1,
    "duration": 30,
  },
  {
    "id": "6",
    "title": "Intermediate Phrases",
    "description": "Practice common English phrases",
    "content": "how are you doing today i am feeling great thanks",
    "level": 2,
    "duration": 45,
  },
  {
    "id": "7",
    "title": "Advanced Punctuation",
    "description": "Master commas, periods, and capitals",
    "content": "Hello, world. This is a test! Can you type this?",
    "level": 3,
    "duration": 60,
  },
]

for i, lesson_data in enumerate(SAMPLE_LESSONS):
    Lesson.objects.get_or_create(
        title=lesson_data['title'],
        defaults={
            'description': lesson_data['description'],
            'content': lesson_data['content'],
            'level': lesson_data['level'],
            'duration': lesson_data['duration'],
            'order': i
        }
    )

print("Lessons seeded successfully!")
