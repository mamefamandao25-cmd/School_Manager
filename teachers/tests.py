from django.test import TestCase

from students.models import Subject, Teacher


class TeacherSearchTests(TestCase):
    def setUp(self):
        math = Subject.objects.create(name='Mathématiques')
        computer_science = Subject.objects.create(name='Informatique')
        english = Subject.objects.create(name='Anglais')
        self.math_teacher = Teacher.objects.create(first_name='Mamadou Moustapha', last_name='Sarr', email='sarr@example.com')
        self.math_teacher.subjects.add(math)
        computer_teacher = Teacher.objects.create(first_name='Pape Ibrahima', last_name='Niang', email='niang@example.com')
        computer_teacher.subjects.add(computer_science)
        english_teacher = Teacher.objects.create(first_name='Cheikh Alssane', last_name='Ndoye', email='ndoye@example.com')
        english_teacher.subjects.add(english)

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
