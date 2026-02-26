import os
import django
from django.urls import get_resolver

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_smart_buddy.settings')
django.setup()

def list_urls(lis, acc=None):
    if acc is None:
        acc = []
    if not lis:
        return
    for i in lis:
        if hasattr(i, 'url_patterns'):
            list_urls(i.url_patterns, acc + [str(i.pattern)])
        else:
            name = i.name if hasattr(i, 'name') else None
            if name:
                print(f"Name: {name} | Path: {''.join(acc)}{i.pattern}")

resolver = get_resolver()
list_urls(resolver.url_patterns)
