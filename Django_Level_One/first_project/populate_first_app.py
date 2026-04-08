import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

## FAKE POP SCRIPT

import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fake = Faker()

topics = ["Search", "News", "Social", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(n = 5):
    for i in range(n):
        # get topic for entry
        topic = add_topic()

        # Create the fake data for that entry
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        # Create the new webpage entry
        webpage = Webpage.objects.get_or_create(topic=topic, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating scripts!")
    populate(20)
    print("Populating complete!")
