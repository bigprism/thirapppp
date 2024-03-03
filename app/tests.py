from django.test import TestCase

from .models import Task

from django.urls import reverse

from .forms import TaskForm

import json


class TaskModelTest(TestCase):

    def test_create_task(self):
        task = Task.objects.create(description='Test task')
        self.assertEqual(task.description, 'Test task')
        self.assertFalse(task.status)



class TaskViewTest(TestCase):

    def test_task_list_view(self):
        task1 = Task.objects.create(description='Test task 1')
        task2 = Task.objects.create(description='Test task 2')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, task1.description)
        self.assertContains(response, task2.description)



class TaskFormTest(TestCase):

    def test_valid_form(self):
        form = TaskForm(data={'description': 'Test task'})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = TaskForm(data={'description': ''})
        self.assertFalse(form.is_valid())





class TaskAPITest(TestCase):

    def test_task_list_api(self):
        task1 = Task.objects.create(description='Test task 1')
        task2 = Task.objects.create(description='Test task 2')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['description'], task1.description)
        self.assertEqual(data[1]['description'], task2.description)