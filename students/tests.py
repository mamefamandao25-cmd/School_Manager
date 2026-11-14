from django.test import TestCase

from .models import Student


class StudentSearchTests(TestCase):
    def setUp(self):
        Student.objects.create(first_name='Mame Fama', last_name='Ndao', classe='L1', active=True)
        Student.objects.create(first_name='Moustapha', last_name='Ndiaye', classe='L2', active=False)
        Student.objects.create(first_name='Fatou Binetou', last_name='Ladiane', classe='L1', active=False)

    def test_search_by_last_name_filters_results(self):
        response = self.client.get('/students/?q=ndi')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Moustapha')
        self.assertNotContains(response, 'Mame Fama')
        self.assertNotContains(response, 'Fatou Binetou')

    def test_search_by_first_name_filters_results(self):
        response = self.client.get('/students/?q=fatou')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Fatou Binetou')
        self.assertNotContains(response, 'Mame Fama')
