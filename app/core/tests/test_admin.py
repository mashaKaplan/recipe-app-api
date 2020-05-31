# from django.test import TestCase, Client
# from django.contrib.auth import get_user_model
# from django.urls import reverse
#
#
# class AdminSideTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.admin_user = get_user_model().objects.create_superuser(
#             email='test@tes.com',
#             password='12345'
#         )
#         self.client.force_login(self.admin_user)
#         self.user = get_user_model().objects.create_user(
#             email='test@tes.com',
#             password='12345',
#             name='User name'
#         )
#
#     def test_users_listed(self):
#         url = reverse('admin:core_user_changeList')
#         res = self.client.get(url)
#
#         self.assertContains(res, self.user.name)
#         self.assertContains(res, self.user.email)
#
#     def test_user_change_page(self):
#         url = reverse('admin:core_user_change', args=self.user.id)
#         res = self.client.get(url)
#         self.assertEqual(res.status_code, 200)
