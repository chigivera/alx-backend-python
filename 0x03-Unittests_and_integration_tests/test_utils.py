#!/usr/bin/env python3
"""
Unit tests for the utils module
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function"""
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with valid inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """Test access_nested_map with invalid inputs"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Test cases for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json with mocked requests.get"""
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = test_payload
            
            result = get_json(test_url)
            
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """Test cases for memoize decorator"""

    def test_memoize(self):
        """Test memoize decorator"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            test_class = TestClass()
            
            # Call a_property twice
            result1 = test_class.a_property
            result2 = test_class.a_property
            
            # Check results
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            
            # Verify a_method was called only once
            mock_method.assert_called_once() 