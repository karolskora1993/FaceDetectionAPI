from django.test import TestCase
from .models import Face
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

TEST_FILE_PATH = './testData/test_img.png'

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
        image = SimpleUploadedFile(name='test_image.jpg', content=open(TEST_FILE_PATH, 'rb').read(),
                                            content_type='image/jpeg')
        self.data = {'name': image}
        self.response = self.client.post(
            reverse('create'),
            self.data,
            format="json")

    def test_api_can_create_a_face(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_api_can_get_a_face(self):
        """Test the api can get a given bucketlist."""
        face = Face.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': face.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, face)
