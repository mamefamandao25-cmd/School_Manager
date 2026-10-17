from django.test import TestCase


class AccueilPageTests(TestCase):
    def test_homepage_displays_welcome_content(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accueil/accueil.html')
        self.assertContains(response, 'Bienvenue sur mon site !')
