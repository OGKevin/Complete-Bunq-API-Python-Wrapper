import random
import unittest

from user import User
from .test_endpoint import EndpointTest


class UserTest(EndpointTest, unittest.TestCase):

    def setUp(self):
        super().setUp(User)
        self.random_id = random.randint(1, 10000)

    def test_get_base_endpoint(self):
        endpoint_should_be = "/user/%d" % self.random_id
        endpoint_to_check = self.test_class.get_base_endpoint(self.random_id)
        self.assert_endpoints(endpoint_should_be, endpoint_to_check)

    def test_get_all_users(self):
        endpoint_should_be = "/user"
        endpoint_to_check = self.test_class.get_all_users()
        self.assert_endpoints(endpoint_should_be, endpoint_to_check)

    def test_get_user_by_id(self):
        endpoint_should_be = "/user/%d" % self.random_id
        endpoint_to_check = self.test_class.get_base_endpoint(self.random_id)
        self.assert_endpoints(endpoint_should_be, endpoint_to_check)

    def test_get_user_person_by_id(self):
        endpoint_should_be = "/user-person/%d" % self.random_id
        endpoint_to_check = self.test_class.get_user_person_by_id(
            self.random_id)
        self.assert_endpoints(endpoint_should_be, endpoint_to_check)

    def test_get_user_company_by_id(self):
        endpoint_should_be = "/user-company/%d" % self.random_id
        endpoint_to_check = self.test_class.get_user_company_by_id(
            self.random_id)
        self.assert_endpoints(endpoint_should_be, endpoint_to_check)