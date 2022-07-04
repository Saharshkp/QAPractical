from application import app
from flask import url_for
from flask_testing import TestCase
import requests_mock


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_level1(self):
        response = self.client.post(url_for('level'), json={"Pokemon": "Charizard", "rarity": "Common"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'85', response.data)

class TestResponse(TestBase):
    def test_level2(self):
        response = self.client.post(url_for('level'), json={"Pokemon": "Rayquaza", "rarity": "Legendary"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'200', response.data)

class TestResponse(TestBase):
    def test_level1(self):
        response = self.client.post(url_for('level'), json={"Pokemon": "Gengar", "rarity": "Rare"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'150', response.data)