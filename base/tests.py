from django.test import TestCase
from .models import Task


class TestViews(TestCase):

    def test_get_login_page(self):
        response = self.client.get('/login/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login.html')

    def test_get_register_page(self):
        response = self.client.get('/register/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/register.html')
    
    def test_get_create_page(self):
        response = self.client.get('/task-create/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/login/?next=/task-create/')

    def test_delete_item(self):
        task = Task.objects.create(title='Test Todo Item')
        response = self.client.get(f'/task-delete/{task.id}')
        self.assertRedirects(response, '/login/?next=/task-delete/1')

    def test_edit_item(self):
        task = Task.objects.create(title='Test Todo Item')
        response = self.client.get(f'/task-update/{task.id}')
        self.assertRedirects(response, '/login/?next=/task-update/1')
