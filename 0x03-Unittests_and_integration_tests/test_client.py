#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, mock_get_json):
        """Test GithubOrgClient.org method"""
        mock_get_json.return_value = expected
        client = GithubOrgClient(org)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url property"""
        with patch('client.GithubOrgClient.org',
                  new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url,
                           "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos method"""
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload
        
        with patch('client.GithubOrgClient._public_repos_url',
                  new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/google/repos"
            client = GithubOrgClient('google')
            self.assertEqual(client.public_repos, ["repo1", "repo2"])
            mock_get_json.assert_called_once()
            mock_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license method"""
        client = GithubOrgClient('google')
        self.assertEqual(client.has_license(repo, license_key), expected)

@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        
        def side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return Mock(json=lambda: cls.org_payload)
            elif url == "https://api.github.com/orgs/google/repos":
                return Mock(json=lambda: cls.repos_payload)
            return None
        
        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down test fixtures"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method with integration"""
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license filter"""
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(license="apache-2.0"),
                        self.apache2_repos) 