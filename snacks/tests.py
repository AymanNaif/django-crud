from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Snack
from django.urls import reverse


class SnackTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='ayman',
            email='ayman_naif@hotmail.com',
            password='ayman123456'
        )

        self.post = Snack.objects.create(
            name='werr',
            purchaser=self.user,
            description='Do whatever'
        )

    def test_string_representation(self):
        post = Snack(name='name')
        self.assertEqual(str(post), post.name)

    def test_all_fields(self):

        self.assertEqual(str(self.post), 'werr')
        self.assertEqual(f'{self.post.purchaser}', 'ayman')
        self.assertEqual(self.post.description, 'Do whatever')

    def test_snack_list_view(self):
        response = self.client.get(reverse('snack-list'))
        self.assertEqual(response.status_code, 200)

    def test_snack_details_view(self):
        response = self.client.get(reverse('snack-detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_snack_update_view(self):
        response = self.client.post(reverse('snack-update', args='1'), {
            'name': 'werr',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'werr')

    def test_home_status(self):
        expected = 200
        url = reverse('snack-list')
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected, actual)

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = 'home.html'
        self.assertTemplateUsed(response, actual)

    def test_create_view(self):
        response = self.client.post(reverse('snack-create'), {
            'name': 'werr',
            'purchaser': self.user,
            'description': 'Do whatever',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'werr')
        self.assertContains(response, 'Do whatever')
        self.assertContains(response, 'ayman')

    def test_delete_view(self):
        response = self.client.get(reverse('snack-delete', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Are you sure that you wanna delete ?')

        post_response = self.client.post(reverse('snack-delete', args='1'))
        self.assertRedirects(post_response, reverse(
            'snack-list'), status_code=302)
