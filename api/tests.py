from django.test import TestCase
from .models import Face
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import os

dir = os.path.dirname(__file__)
TEST_IMAGE_PATH = os.path.join(dir, '/testData/test_img.jpg')


class ModelTest(TestCase):

    def setUp(self):
        self.face = Face()

    def test_create_new_not_recognized_face(self):
        old_count = Face.objects.count()
        self.face.save()
        new_count = Face.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.data = {'image': None}
        self.response = self.client.post(
            reverse('create'),
            self.data,
            format="json")

    def test_api_can_create_a_face(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_api_can_get_a_face(self):
        face = Face.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': face.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, face)
