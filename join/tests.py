from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Task, Contact, Category

class BaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name="Test Category", color="#000000")
        self.task = Task.objects.create(title="Test Task", description="Test Description")
        self.contact = Contact.objects.create(firstname="Test", lastname="Contact")
        self.create_task_url = reverse('task-list')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

class TaskTests(BaseTest):
    def test_tasks_authenticated(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)

class TaskDetailTests(BaseTest):
    def test_taskDetail_authenticated(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
   
class ContactsTests(BaseTest):
    def test_contacts_authenticated(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)
        
class ContactsDetailTests(BaseTest):
    def test_contactDetail_authenticated(self):
        url = reverse('contact_detail', args=[self.contact.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) 
        
class CatgoriesTests(BaseTest):
    def test_categories_authenticated(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        
class TaskCreateTest(BaseTest):
    def test_create_task(self):
        task_data = {
                    "assigned_to": [self.contact.id],
                    "category_id": self.category.id,
                    "subtasks": [],
                    "title": "test",
                    "description": "test",
                    "created_at": "2024-04-08",
                    "date": "2024-04-11",
                    "prio": "low",
                    "stat": "todo"
                    }
        response = self.client.post(self.create_task_url, task_data, format='json')
        self.assertEqual(response.status_code, 201)
        
class TaskUpdateTest(BaseTest):
    def test_update_task(self):
        task_data = {
                    "title": "test",
                    "description": "test",
                    }
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.patch(url, task_data, format='json')
        self.assertEqual(response.status_code, 200)     
        
class TaskDeleteTest(BaseTest):
    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)         

class ContactCreateTest(BaseTest):
    def contact_create_task(self):
        contact_data = {
                        "firstname": "Postman",
                        "lastname": "Test",
                        "email": "postman@dev.com",
                        "phone": "4131321",
                        "color": "#fcd8d1",
                        }
        response = self.client.post(self.create_task_url, contact_data, format='json')
        self.assertEqual(response.status_code, 201)
        
class ContactDeleteTest(BaseTest):
    def test_delete_contact(self):
        url = reverse('contact_detail', args=[self.contact.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)   
        
class ContactUpdateTest(BaseTest):
    def test_update_contact(self):
        contact_data = {
                        "firstname": "Postman",
                        "lastname": "Test",
                        "email": "postman@dev.com",
                        "phone": "4131321",
                        "color": "#fcd8d1",
                        }
        url = reverse('contact_detail', args=[self.contact.id])
        response = self.client.put(url, contact_data, format='json')
        self.assertEqual(response.status_code, 200)     