import unittest
from flask import Flask
from flask.testing import FlaskClient
from werkzeug.datastructures import FileStorage
from io import BytesIO
import os

# Assuming the Flask app is created in app.py
from app import create_app

class ComplaintEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_analyze_audio_complaint(self):
        audio_data = BytesIO(b"fake audio data")
        audio_file = FileStorage(stream=audio_data, filename="test_audio.mp3", content_type="audio/mpeg")

        response = self.client.post('/complaint/analyze_audio', data={'file': audio_file}, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        self.assertIn('category', response.json)
        self.assertIn('sub_category', response.json)
        self.assertIn('summary', response.json)
        self.assertIn('key_issues', response.json)

    def test_analyze_complaint_images(self):
        image_data = BytesIO(b"fake image data")
        image_file = FileStorage(stream=image_data, filename="test_image.png", content_type="image/png")

        response = self.client.post('/complaint/analyze_images', data={'images': [image_file]}, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        self.assertIn('category', response.json[0])
        self.assertIn('sub_category', response.json[0])
        self.assertIn('summary', response.json[0])
        self.assertIn('key_issues', response.json[0])

    def test_analyze_video_complaint(self):
        video_data = BytesIO(b"fake video data")
        video_file = FileStorage(stream=video_data, filename="test_video.mp4", content_type="video/mp4")

        response = self.client.post('/complaint/analyze_video', data={'file': video_file}, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        self.assertIn('category', response.json)
        self.assertIn('sub_category', response.json)
        self.assertIn('summary', response.json)
        self.assertIn('key_issues', response.json)

if __name__ == '__main__':
    unittest.main()