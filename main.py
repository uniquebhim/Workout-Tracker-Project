import requests
from datetime import datetime


class WorkoutTracker:
    def __init__(self):
        # Get user inputs for gender, weight, height, and age
        self.gender = "male" if input("Enter your gender (M/F):").lower() == 'm' else "female"
        self.weight_kg = int(input("Enter your weight (in kg) :"))
        self.height_cm = int(input("Enter your height (in cm) :"))
        self.age = int(input("Enter your age :"))

        # Set up environment variables
        self.APP_ID = "api_id"
        self.API_KEY = "api_key"
        self.exercise_endpoint = "url"
        self.sheet_endpoint = "sheet_url"
        self.TOKEN = "token"
        self.headers = {"Authorization": f"Bearer {self.TOKEN}"}

        # Set a flag to determine if the user wants to end the program
        self.want_end = True

        # Call the entry_point() method to start the program
        self.entry_point()

    def entry_point(self):
        while self.want_end:
            # Show the user options for what they can do
            option = int(input(
                "\n1. Add Workout\n2. Get details\n3. Delete Entry\n4. EXIT\n\t\t\tEnter your Choice:"))

            if option == 1:
                self.add_workout()
            elif option == 2:
                self.get_rows()
            elif option == 3:
                self.delete_row()
            elif option == 4:
                self.end()
            else:
                print("Invalid option chosen")

    def end(self):
        # Set the flag to end the program
        self.want_end = False

    def add_workout(self):
        # Ask the user to input the exercises they did
        exercise_text = input("Tell me which exercises you did: ")

        # Set headers and parameters for the Nutritionix API
        headers = {
            "x-app-id": self.APP_ID,
            "x-app-key": self.API_KEY,
        }
        parameters = {
            "query": exercise_text,
            "gender": self.gender,
            "weight_kg": self.weight_kg,
            "height_cm": self.height_cm,
            "age": self.age
        }

        # Make a POST request to the Nutritionix API with the exercise information
        response = requests.post(url=self.exercise_endpoint,
                                 json=parameters, headers=headers)
        result = response.json()
        print(result)

        # Get the current date and time for the workout entry
        today_date = datetime.now().strftime("%d/%m/%Y")
        now_time = datetime.now().strftime("%X")

        # Loop through each exercise in the response and add it to the Google Sheet
        for exercise in result["exercises"]:
            sheet_inputs = {
                "workout": {
                    "date": today_date,
                    "time": now_time,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }

        # Make a POST request to the Google Sheets API to add the workout entry
        sheet_response = requests.post(
            url=self.sheet_endpoint, json=sheet_inputs, headers=self.headers)
        print(sheet_response.text)

    def get_rows(self):
        """
        Sends a GET request to retrieve all the rows in the Google Sheet.
        """
        get_sheet_response = requests.get(
            url=self.sheet_endpoint, headers=self.headers)
        print(get_sheet_response.text)


    def delete_row(self):
        """
        Deletes a row in the Google Sheet with the specified ID.
        """
        object_id = int(input("Enter the ID number:"))
        delete_endpoint = f"{self.sheet_endpoint}/{object_id}"
        delete_response = requests.delete(
            url=delete_endpoint, headers=self.headers)
        print(delete_response.text)



if __name__ == "__main__":
    workout = WorkoutTracker()


