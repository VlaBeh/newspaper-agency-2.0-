from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Topic

TOPIC_URL = reverse("catalog:topic-list")


class PrivateTopicListViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123",
        )
        self.client.force_login(self.user)

    def test_retrieve_topic_list(self):
        Topic.objects.create(name="Test Topic")
        Topic.objects.create(name="Test Topic2")

        response = self.client.get(TOPIC_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/topic_list.html")
