import datetime
from unittest import mock

import pytz
from django.test import TestCase

from authentication.models import CustomUser
from .models import Teacher

TEST_DATE = datetime.datetime(2021, 10, 10, 12, 00, tzinfo=pytz.utc)
TEST_DATE_END = TEST_DATE + datetime.timedelta(days=15)


class TestTeacherrModel(TestCase):
    """Class for CustomUser Model test"""

    def setUp(self):
        """ Create a user object to be used by the tests """
        time_mock = datetime.datetime(2021, 10, 10, 12, 00, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now') as mock_time:
            mock_time.return_value = time_mock
            self.user = CustomUser(id=111, email='email@mail.com', password='1234', first_name='fname',
                                   middle_name='mname',
                                   last_name='lname')
            self.user.save()
            self.user_free = CustomUser(id=222, email='2email@mail.com', password='1234', first_name='2fname',
                                        middle_name='2mname',
                                        last_name='2lname')
            self.user_free.save()

            self.teacher1 = Teacher(id=101, name="teacher1", surname="s1", patronymic="p1")
            self.teacher1.save()

            self.teacher2 = Teacher(id=102, name="teacher2", surname="s2", patronymic="p2")
            self.teacher2.save()

    def test_get_by_id_positive(self):
        """Positive test of the CustomUser.get_by_id() method"""
        teacher = Teacher.get_by_id(101)
        self.assertEqual(teacher.id, 101)
        self.assertEqual(teacher.name, 'teacher1')
        self.assertEqual(teacher.surname, "s1")
        self.assertEqual(teacher.patronymic, "p1")

    def test_get_by_id_negative(self):
        """Negative test of the CustomUser.get_by_id() method"""
        teacher = Teacher.get_by_id(999)
        self.assertIsNone(teacher)

    def test_delete_by_id_positive(self):
        """ Test of the CustomUser.delete_by_id() method """
        self.assertTrue(Teacher.delete_by_id(101))
        self.assertRaises(Teacher.DoesNotExist, Teacher.objects.get, pk=101)

    def test_delete_by_id_negative(self):
        """ Test of the CustomUser.delete_by_id() method """
        self.assertFalse(Teacher.delete_by_id(999))

    def test_get_all(self):
        """ Positive Test of the CustomUser.create method TEST_DATE_END"""
        teachers = list(Teacher.get_all())
        teachers.sort(key=lambda teacher: teacher.id)
        self.assertListEqual(teachers, [self.teacher1, self.teacher2])

    def test_update(self):
        teacher = Teacher.objects.get(id=101)
        teacher.update(name="testName", surname="testSurname", patronymic="testPatronymic")

        teacher = Teacher.objects.get(id=101)
        self.assertIsInstance(teacher, Teacher)
        self.assertEqual(teacher.name, "testName")
        self.assertEqual(teacher.surname, "testSurname")
        self.assertEqual(teacher.patronymic, "testPatronymic")

    def test_update_only_name(self):
        teacher = Teacher.objects.get(id=101)
        teacher.update(name="testName")

        teacher = Teacher.objects.get(id=101)
        self.assertIsInstance(teacher, Teacher)
        self.assertEqual(teacher.name, "testName")
        self.assertEqual(teacher.surname, "s1")
        self.assertEqual(teacher.patronymic, "p1")

    def test_update_not_valid_name(self):
        teacher = Teacher.objects.get(id=101)
        teacher.update(name="testName" * 5)

        teacher = Teacher.objects.get(id=101)
        self.assertIsInstance(teacher, Teacher)
        self.assertEqual(teacher.name, "teacher1")
        self.assertEqual(teacher.surname, "s1")
        self.assertEqual(teacher.patronymic, "p1")

    def test_create(self):
        teacher = Teacher.create(name="testName", surname="s1", patronymic="p1")
        teacher = Teacher.objects.get(id=teacher.id)
        self.assertIsInstance(teacher, Teacher)
        self.assertEqual(teacher.name, "testName")
        self.assertEqual(teacher.surname, "s1")
        self.assertEqual(teacher.patronymic, "p1")

    def test_createnot_valid_surname(self):
        teacher = Teacher.create(name="testName", surname="s1" * 20, patronymic="p1")
        self.assertIsNone(teacher)