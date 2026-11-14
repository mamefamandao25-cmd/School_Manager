from django.test import TestCase

from students.models import Teacher


class TeacherSearchTests(TestCase):
    def setUp(self):
        Teacher.objects.create(first_name='Mamadou Moustapha', last_name='Sarr', subject='Mathématiques')
        Teacher.objects.create(first_name='Pape Ibrahima', last_name='Niang', subject='Informatique')
        Teacher.objects.create(first_name='Cheikh Alssane', last_name='Ndoye', subject='Anglais')

    def test_search_by_last_name_filters_results(self):
        response = self.client.get('/teachers/?q=sarr')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mamadou Moustapha')
        self.assertNotContains(response, 'Pape Ibrahima')

    def test_search_by_subject_filters_results(self):
        response = self.client.get('/teachers/?q=anglais')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cheikh Alssane')
        self.assertNotContains(response, 'Mamadou Moustapha')
