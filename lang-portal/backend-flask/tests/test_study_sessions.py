import pytest
from datetime import datetime

def test_create_study_session_success(test_client, app):
    # Given valid study session data
    data = {
        "group_id": 1,
        "study_activity_id": 1
    }
    
    # When creating a new study session
    response = test_client.post('/api/study-sessions', json=data)
    
    # Then verify the response
    assert response.status_code == 201, f"Response: {response.get_json()}"
    result = response.get_json()
    assert "id" in result
    assert isinstance(result["id"], int)
    assert result["group_id"] == data["group_id"]
    assert result["study_activity_id"] == data["study_activity_id"]
    assert "created_at" in result
    assert "message" in result
    assert result["message"] == "Session created"

def test_create_study_session_missing_fields(test_client):
    # Test cases for missing fields
    test_cases = [
        ({}, "No data provided"),
        ({"group_id": 1}, "Missing required fields: study_activity_id"),
        ({"study_activity_id": 1}, "Missing required fields: group_id"),
        (None, "No data provided")
    ]
    
    for data, expected_error in test_cases:
        headers = {'Content-Type': 'application/json'}
        if data is None:
            response = test_client.post('/api/study-sessions', data='', headers=headers)
        else:
            response = test_client.post('/api/study-sessions', json=data, headers=headers)
        result = response.get_json()
        assert response.status_code == 400, f"Response: {result}"
        assert "error" in result
        assert expected_error in result["error"]

def test_create_study_session_invalid_types(test_client):
    # Test cases for invalid field types
    test_cases = [
        {"group_id": "1", "study_activity_id": 1},  # String instead of int
        {"group_id": 1, "study_activity_id": "1"},  # String instead of int
        {"group_id": 1.5, "study_activity_id": 1},  # Float instead of int
        {"group_id": 1, "study_activity_id": 1.5},  # Float instead of int
    ]
    
    headers = {'Content-Type': 'application/json'}
    for data in test_cases:
        response = test_client.post('/api/study-sessions', json=data, headers=headers)
        result = response.get_json()
        assert response.status_code == 400, f"Response: {result}"
        assert "error" in result
        assert "must be integers" in result["error"]

def test_create_study_session_nonexistent_ids(test_client):
    # Test with non-existent group_id
    data = {
        "group_id": 99999,
        "study_activity_id": 1
    }
    response = test_client.post('/api/study-sessions', json=data)
    result = response.get_json()
    assert response.status_code == 404, f"Response: {result}"
    assert "error" in result
    assert "Group not found" in result["error"]

    # Test with non-existent activity_id
    data = {
        "group_id": 1,
        "study_activity_id": 99999
    }
    response = test_client.post('/api/study-sessions', json=data)
    result = response.get_json()
    assert response.status_code == 404, f"Response: {result}"
    assert "error" in result
    assert "Study activity not found" in result["error"] 