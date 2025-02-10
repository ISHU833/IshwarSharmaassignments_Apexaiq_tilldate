import requests
import json
from json_file2 import Wheather

class Test_API:

    def test_current_state(self):
        obj = Wheather()
        data = obj.get_current_and_forecast_weather()

        with open(r"D:\apexa_webscrspping\REST_API_DAY4\first.json", "r")as file:
            saved_data = json.loads(file.read())

        # check if the data correctly fetched and save or not
        assert data == saved_data, "Data is not saved corectly"

        # check if any parameter is not null 
        def check_no_null(data):
            if isinstance(data, dict):
                for key in data:
                    assert data[key] is not None, f"Null value found for key:{key}"
            elif isinstance(data, list):
                for item in data:
                    assert item is not None, "Null value is found in list"
        check_no_null(data)