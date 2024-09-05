from django.test import TestCase
from django.contrib.auth import get_user_model
from catalog.models import Topic, Newspaper, Redactor


class TopicModelTest(TestCase):
    def test_topic_creation(self):
        topic = Topic.objects.create(name="Politics")
        self.assertEqual(str(topic), topic.name)


class RedactorModelTest(TestCase):
    def test_redactor_creation(self):
        redactor = get_user_model().objects.create_user(
            username="editor1",
            password="testpass12",
            years_of_experience=5
        )
        self.assertEqual(str(redactor),
                         f"{redactor.username} ({redactor.years_of_experience} years of experience)")


class NewspaperModelTest(TestCase):
    def test_newspaper_creation(self):
        topic = Topic.objects.create(name="Politics")
        newspaper = Newspaper.objects.create(
            title="Politics is...",
            content="Content of the newspaper",
            published_date="2024-01-01"
        )
        newspaper.topics.add(topic)
        self.assertEqual(str(newspaper), newspaper.title)
        self.assertIn(topic, newspaper.topics.all())
