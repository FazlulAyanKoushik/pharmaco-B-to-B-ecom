from rest_framework import status

from catalogio.rest.tests import urlhelpers as catalogio_urlhelpers

from common.base_orm import BaseOrmCallApi
from common.base_test import BaseAPITestCase

from core.rest.tests import urlhelpers as core_urlhelpers, payloads as core_payloads

from . import payloads, urlhelpers


class PrivateCustomersOrderListApiTests(BaseAPITestCase):
    """Test organization private (ordered) customer list api"""

    def setUp(self):
        super(PrivateCustomersOrderListApiTests, self).setUp()

        self.base_orm = BaseOrmCallApi()

        # Create base product
        self.base_product = self.base_orm.baseproduct(payloads.base_product_payload())

        # Get base product uid
        self.base_product_uid = self.base_product.uid

        # Get organization
        self.organization = self.client.get(urlhelpers.organization_list_url())

        # Get user uid
        self.user = self.client.get(urlhelpers.organization_user_list_url())
        self.user_uid = self.user.data["results"][0]["user"]["uid"]

        # create product payload
        self.payload = {
            "base_product": self.base_product_uid,
            "organization": self.organization,
            "stock": 10,
            "selling_price": "100",
            "merchant": self.user_uid,
        }

        # Create product
        self.post_response = self.client.post(
            urlhelpers.product_list_url(), self.payload
        )

        # Get product list
        self.get_product = self.client.get(catalogio_urlhelpers.product_list_url())

        # Get product slug
        self.product_slug = self.get_product.data["results"][0]["slug"]

        # Create customer
        self.customer = self.client.post(
            core_urlhelpers.user_registration_list_url(),
            payloads.create_customer_payload(),
        )

        # Logged in customer
        self.customer_login = self.client.post(
            core_urlhelpers.user_token_login_url(), payloads.customer_login_payload()
        )

        # Assert that the response is correct
        self.assertEqual(self.customer_login.status_code, status.HTTP_201_CREATED)

        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + self.customer_login.data["access"],
            HTTP_X_DOMAIN="bill-corp",
        )

        # Create upazila, district, and division for customer address
        self.division = self.base_orm.division("Dhaka")
        self.district = self.base_orm.district("Gazipur", self.division.name)
        self.upazila = self.base_orm.upazila("Dhamrai", self.district.name)

        # Create customer address
        self.address = self.client.post(
            urlhelpers.create_customer_address_url(),
            payloads.customer_address_payload(
                self.upazila.uid, self.district.uid, self.division.uid
            ),
        )

        # Assert that the response is correct
        self.assertEqual(self.address.status_code, status.HTTP_201_CREATED)

        # Get address slug for orders
        self.get_address = self.client.get(urlhelpers.create_customer_address_url())
        self.address_uid = self.get_address.data[0]["uid"]

        # create delivery charge
        self.delivery_charge_payload = {
            "charge": "60.00",
            "district": self.district,
            "admin": self.base_product.superadmin,
        }
        self.delivery_charge = self.base_orm.delivery_charge(
            self.delivery_charge_payload
        )

        # Payment method
        self.payment_method = self.base_orm.payment_method()
        self.payment_uid = self.payment_method.uid

        # Add product on cart
        self.product = self.client.post(
            urlhelpers.cart_products_list_url(),
            payloads.add_product_payload(self.product_slug),
        )

        # Assert that the response is correct
        self.assertEqual(self.product.status_code, status.HTTP_201_CREATED)

        # Place order from customer side
        self.create_order_list = self.client.post(
            urlhelpers.create_order_list_url(),
            payloads.customer_order_payload(self.address_uid, self.payment_uid),
        )

        # Assert that the response is correct
        self.assertEqual(self.create_order_list.status_code, status.HTTP_201_CREATED)

        # Get customer order list
        self.get_order_list = self.client.get(urlhelpers.create_order_list_url())

        self.customer_order_uid = self.get_order_list.data["results"][0]["uid"]

        # Logged in organization user
        self.user_login = self.client.post(
            core_urlhelpers.user_token_login_url(), core_payloads.login_info_payload()
        )

        # Provide organization user credentials for access restricted api
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + self.user_login.data["access"],
            HTTP_X_DOMAIN="bill-corp",
        )

        # Get organization private customers who orders
        self.get_customer = self.client.get(urlhelpers.organization_customer_list_url())

        # Get organization private customers uid
        self.get_order_uid = self.get_customer.data["results"][0]["uid"]

    def test_ordered_customer_list(self):
        # Test private organization customer list api

        response = self.get_customer

        # Assert that the response is correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_ordered_customer_detail(self):
        # Test private organization customer detail api

        response = self.client.get(
            urlhelpers.organization_customer_detail_url(self.get_order_uid)
        )

        # Assert that the response is correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_delivery_charge_detail(self):
        # Test for customer delivery charge detail

        response = self.client.get(
            urlhelpers.customer_delivery_charge_detail(self.address_uid)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["charge"], self.delivery_charge_payload["charge"]
        )
