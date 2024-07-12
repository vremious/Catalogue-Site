from django.test import TestCase

from django.test import TestCase
from main.models import *

from django.test import TestCase
from .models import TesterTime, Available, Type, Models, Filial
from django.urls import reverse


class MainPageTestCase(TestCase):
    def test_main_page_view(self):
        test = Filial.objects.create(
            filial='Test',
            slug='test'
        )
        response = self.client.get(reverse('category_detail', args=(test.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/category_detail.html')

        # Проверка формирования контекста
        self.assertTrue('testertime' in response.context)
        self.assertTrue('typed' in response.context)
        self.assertTrue('filial' in response.context)
        self.assertTrue('typed1' in response.context)
        self.assertTrue('type' in response.context)
        self.assertTrue('image' in response.context)
        self.assertTrue('city' in response.context)
        self.assertTrue('main_button' in response.context)
        self.assertTrue('city17' in response.context)

        # Другие необходимые проверки контекста

        # Проверка данных контекста
        # self.assertTrue(TesterTime.objects.all().exists())
        # self.assertTrue(Available.objects.all().exists())
        # self.assertTrue(Type.objects.all().exists())
        # self.assertTrue(Models.objects.values_list('image', 'id').exists())
        # self.assertTrue(Filial.objects.all().exists())

class PurposeTest(TestCase):
    def test_purpose_choices(self):
        purpose = Purpose.objects.create(purpose='На продажу')
        self.assertEqual(purpose.purpose, 'На продажу')
        purpose = Purpose.objects.create(purpose='Абонентское')
        self.assertEqual(purpose.purpose, 'Абонентское')
        purpose = Purpose.objects.create(purpose='Лидское пиво')
        self.assertEqual(purpose.purpose, 'Лидское пиво')


class CompanyModelTest(TestCase):
    def setUp(self):
        self.company1 = Company.objects.create(company='Company1')
        self.company2 = Company.objects.create(company='Company2')

    def test_company_creation(self):
        company1 = Company.objects.get(company='Company1')
        company2 = Company.objects.get(company='Company2')

        self.assertEqual(company1.company, 'Company1')
        self.assertEqual(company2.company, 'Company2')

    def test_unique_company(self):
        with self.assertRaises(Exception):
            Company.objects.create(company='Company1')

    def test_verbose_name(self):
        company = Company.objects.get(company='Company1')
        self.assertEqual(company._meta.get_field('company').verbose_name, 'Производитель')


class TypeTestCase(TestCase):
    def setUp(self):
        purpose = Purpose.objects.create(purpose='На продажу')
        Type.objects.create(type="Тестирование", purpose=purpose)

    def test_type_slug(self):
        test_type = Type.objects.get(type="Тестирование")
        self.assertEqual(test_type.slug, 'testirovanie')
    #
    # def test_type_verbose_name(self):
    #     test_type = Type.objects.get(type="Test Type")
    #     self.assertEqual(str(test_type._meta.verbose_name), "Тип оборудования")
    #
    # def test_type_str(self):
    #     test_type = Type.objects.get(type="Test Type")
    #     self.assertEqual(str(test_type), "Test Type")

