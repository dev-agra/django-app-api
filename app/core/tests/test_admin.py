"""Test for Django Admin"""

from django.test import TestCase, Client

from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):
    """Test for admin.py"""
    def setUp(self):
        # create user and client
        self.clent = Client()
        # create superuser
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123'
        )
        # allows to force auth
        self.client.force_login(self.admin_user)

        # create user
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name="dev_test"
        )

    def test_users_list(self):
        """Chk userslisted on page"""
        # url to get admin details
        url = reverse('admin:core_user_changelist')
        # http get request as we forced login it will be authenticated
        res = self.client.get(url)
        # chk if page containes name and email
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
