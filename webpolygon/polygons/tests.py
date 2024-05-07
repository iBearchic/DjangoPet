from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Polygon

class PolygonAPITests(APITestCase):
    def setUp(self):
        # Создание тестового полигона
        self.test_polygon = Polygon.objects.create(name="Test Polygon", polygon="POLYGON((0 0, 1 1, 1 0, 0 0))")
        self.list_url = reverse('polygon-list') # проверка наличия правильного URL
    
    def test_create_polygon(self):
        data = {"name": "New Polygon", "polygon": "POLYGON((0 0, 1 1, 1 0, 0 0))"}
        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Polygon.objects.count(), 2)
    
    def test_get_polygon_list(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) # проверяем, что в ответе только оидн полигон из setUp
    
    def test_delete_polygon(self):
        delete_url = reverse('polygon-detail', kwargs={'pk': self.test_polygon.pk})
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Polygon.objects.count(), 0)
