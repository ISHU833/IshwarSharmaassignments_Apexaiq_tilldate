import requests
import json
from json_file import APIClient

class TestApi:

    def test_fetchAndStoreData(self):
        # fetch data
        obj = APIClient()
        data = obj.fetch_and_save_data()

        with open(r"D:\apexa_webscrspping\REST_API_DAY4\ayta.json", "r") as file:
            saved_data = json.load(file)

        # check if the data correctly fetched and save or not
        assert data == saved_data , "data is not save correctly"

        # Ensure 'posts' key exists
        assert 'posts' in data, "'posts' key is missing from the response"

        # Validate each post
        for post in data['posts']:
            # Check for required fields
            assert 'id' in post, f"'id' is missing in post: {post}"
            assert 'title' in post, f"'title' is missing in post: {post}"
            assert 'body' in post, f"'body' is missing in post: {post}"
            assert 'tags' in post, f"'tags' is missing in post: {post}"

            # Check that ID is an integer and not null
            assert post['id'] is not None, "ID should not be null"
            assert isinstance(post['id'], int), "ID should be an integer"

            # title should not be empty
            assert post['title'], "title should not be empty"

            # body should be an string
            assert isinstance(post['body'], str), "body should be an string"

            # tags should be a list
            assert isinstance(post['tags'], list), "tags should be a list"