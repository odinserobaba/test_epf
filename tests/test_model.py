import os
import pytest
import logging
from unittest.mock import patch, MagicMock
from models import QueueLicense  # Replace 'your_module' with the actual module name

# Mocking the cat_print function
def cat_print(_):
    return "Mocked cat print"

# Fixture to create a QueueLicense instance
@pytest.fixture
def queue_license():
    return QueueLicense(name_tests='test_name')

# Test for create_folder_and_file method
def test_create_folder_and_file(queue_license):
    # Mock datetime to return a fixed date
    with patch('your_module.datetime') as mock_datetime:
        mock_datetime.now.return_value.strftime.return_value = "2023-10-01"
        result_file_path = queue_license.create_folder_and_file()

        # Check if the folder and file paths are created correctly
        assert os.path.exists(result_file_path)
        assert "out/2023-10-01" in result_file_path
        assert "test_name" in result_file_path

# Test for write_to_file method
def test_write_to_file(queue_license, tmp_path):
    # Use tmp_path to create a temporary file
    test_file_path = tmp_path / "test_file.md"

    # Write a test message to the file
    test_message = "Test message"
    queue_license.write_to_file(test_message, test_file_path)

    # Check if the message is written to the file
    with open(test_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        assert test_message in content

# Test for add_to_queue method
def test_add_to_queue(queue_license):
    # Mock function to add to the queue
    def mock_func(arg):
        return f"Processed {arg}"

    # Add a function and argument to the queue
    queue_license.add_to_queue(mock_func, "test_arg")

    # Check if the function and argument are added to the queue
    assert len(queue_license.queue) == 1
    assert queue_license.queue[0][0].__name__ == "mock_func"
    assert queue_license.queue[0][1] == "test_arg"

# Test for process_queue method
def test_process_queue(queue_license):
    # Mock function to add to the queue
    def mock_func(arg):
        return f"Processed {arg}"

    # Add a function and argument to the queue
    queue_license.add_to_queue(mock_func, "test_arg")

    # Process the queue
    with patch.object(queue_license, 'logger') as mock_logger:
        queue_license.process_queue()

        # Check if the function was executed and the queue is processed
        assert queue_license.setup['current_method_index'] == 1
        assert mock_logger.debug.called

# Test for process_queue method with stop_flag
def test_process_queue_with_stop_flag(queue_license):
    # Set stop_flag to True
    queue_license.stop_flag = True

    # Mock function to add to the queue
    def mock_func(arg):
        return f"Processed {arg}"

    # Add a function and argument to the queue
    queue_license.add_to_queue(mock_func, "test_arg")

    # Process the queue
    with patch.object(queue_license, 'logger') as mock_logger:
        queue_license.process_queue()

        # Check if the queue processing stops due to stop_flag
        assert queue_license.setup['current_method_index'] == 0
        assert mock_logger.debug.called
