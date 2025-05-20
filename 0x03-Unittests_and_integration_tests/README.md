# 0x03. Unittests and Integration Tests

This directory contains unit tests and integration tests for Python modules.

## Files:

- `test_utils.py`: Contains unit tests for the utils module
  - TestAccessNestedMap: Tests for the access_nested_map function
  - TestGetJson: Tests for the get_json function
  - TestMemoize: Tests for the memoize decorator

- `test_client.py`: Contains unit tests and integration tests for the GithubOrgClient class
  - TestGithubOrgClient: Unit tests for individual methods
  - TestIntegrationGithubOrgClient: Integration tests using fixtures

## Test Types:

### Unit Tests
Unit tests focus on testing individual functions or methods in isolation. They use mocking to simulate dependencies and test specific behaviors.

### Integration Tests
Integration tests verify that different parts of the system work together correctly. They test the interaction between components and ensure the system functions as a whole.

## Running Tests:
To run the tests, use:
```bash
python -m unittest path/to/test_file.py
```

## Requirements:
- Python 3.7
- unittest
- parameterized
- requests (for HTTP calls) 