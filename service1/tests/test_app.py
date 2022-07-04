from flask import Flask, url_for
from flask_testing import TestCase
import application.routes
from application import app 
from unittest.mock import patch
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

#Testing the route index
class Testindex(TestBase):
    def test_get_index(self):
            response =self.client.get(url_for('index'))
            self.assert500(response)

class TestPok1(TestBase):
    def test_pok1(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5000/Pokemon', text='Charizard')
            m.get('http://service3:5000/rarity', text='Rare')
            m.post('http://service4:5000/level', text='60')
            
            response =self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'Charizard', response.data)
            self.assertIn(b'Rare', response.data)
            self.assertIn(b'60', response.data)
