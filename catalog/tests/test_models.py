from django.test import TestCase
from django.contrib.auth import get_user_model
from catalog.models import Topic, Newspaper, Redactor


class ModelsTest(TestCase):
    def test_topic_creation(self):
        topic = Topic.objects.create(name="Politics")
        self.assertEqual(str(topic), topic.name)

    def test_redactor_creation(self):
        redactor = get_user_model().objects.create_user(
            username="editor1",
            password="testpass12",
            first_name="editor1",
            last_name="editor1",
            years_of_experience=5
        )
        expected_str = f"{redactor.username}: ({redactor.first_name} {redactor.last_name})"
        self.assertEqual(str(redactor), expected_str)

    def test_newspaper_creation(self):
        topic = Topic.objects.create(name="Politics")
        newspaper = Newspaper.objects.create(
                title="Politics is...",
                content="Content of the newspaper",
                published_date="2024-01-01",
                topics=topic
            )
        self.assertEqual(str(newspaper), newspaper.title)
        self.assertEqual(newspaper.topics, topic)
