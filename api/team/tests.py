from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from team import models


class MemberTests(APITestCase):

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.members = [
            {
                'firstname': 'Raj',
                'lastname': 'Kothari',
                'phone': '+918758886452',
                'email': 'raj.kothari@gmail.com',
                'role': 'admin'
            },
            {
                'firstname': 'Sarang',
                'lastname': 'Sharma',
                'phone': '+919879200381',
                'email': 'sarang.sharma@gmail.com',
                'role': 'regular'
            }
        ]

    def test_create_member(self):
        """Assert creating a new member is working"""
        url = reverse('member-list')
        body = self.members[0].copy()
        response = self.client.post(url, body, format='json')
        member = models.Member.objects.get()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Member.objects.count(), 1)
        self.assertEqual(member.firstname, body['firstname'])
        self.assertEqual(member.lastname, body['lastname'])
        self.assertEqual(member.phone, body['phone'])
        self.assertEqual(member.role, body['role'])

    def test_edit_member(self):
        """Assert editing a member is working"""
        member_obj = models.Member.objects.create(**self.members[0])
        body = {
            "role": "regular",
            "email": "raj.kothari@yahoo.com"
        }
        url = reverse('member-detail', kwargs={'pk': member_obj.pk})
        response = self.client.patch(url, body, format="json")
        updated_member_obj = models.Member.objects.get()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_member_obj.role, body['role'])
        self.assertEqual(updated_member_obj.email, body['email'])

    def test_read_member(self):
        """Assert reading a member is working"""
        member_obj = models.Member.objects.create(**self.members[0])
        url = reverse('member-detail', kwargs={'pk': member_obj.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_response = {'id': member_obj.pk}
        expected_response.update(self.members[0])
        self.assertDictEqual(response.data, expected_response)

    def test_deleting_member(self):
        """Assert deleting a member is working"""
        member_obj = models.Member.objects.create(**self.members[0])
        url = reverse('member-detail', kwargs={'pk': member_obj.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Member.objects.count(), 0)

    def test_list_members(self):
        """Assert listing members is possible"""
        member_objs = []
        for member in self.members:
            _member = models.Member.objects.create(**member)
            member_objs.append(_member)
        url = reverse('member-list')
        response = self.client.get(url)
        expected_response = self.members[:]
        expected_response[0]['id'] = member_objs[0].pk
        expected_response[1]['id'] = member_objs[1].pk

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertListEqual(response.data, expected_response)
