# tasks/tests.py
from django.test import TestCase
# from django.urls import reverse
from accounts.models import Account
from .models import Task


class TaskViewsTestCase(TestCase):

    def setUp(self):
        # ایجاد یک کاربر از مدل Account
        self.account_user = Account.objects.create_user(
            username='testuser',
            password='password'
            )
        self.client.login(
            username='testuser',
            password='password'
            )

        # ایجاد تسک برای کاربر Account
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Task Description',
            user=self.account_user  # ارجاع به مدل Account
        )
