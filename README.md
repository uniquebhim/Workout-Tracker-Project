# **Workout Tracker Project**

This command-line application allows users to track their workouts and save the data to a Google Sheet. The application uses the **[Nutritionix API](https://www.nutritionix.com/business/api)** to obtain information about exercises, and the **[Sheety API](https://sheety.co/)** to write the data to a Google Sheet.

## **Getting Started**

To use this application, you'll need to sign up for an account with **[Nutritionix](https://www.nutritionix.com/business/api)** and **[Sheety](https://sheety.co/)** to obtain your API keys. You'll also need to set up a Google Sheet with the following columns: **`date`**, **`time`**, **`exercise`**, **`duration`**, and **`calories`**.

Once you have your API keys and Google Sheet set up, create a new file called **`.env`** in the root directory of the project and add the following lines:

```
APP_ID=<your Nutritionix app ID>
API_KEY=<your Nutritionix API key>
SHEET_ENDPOINT=<your Sheety API endpoint>
TOKEN=<your Sheety API token>

```

Replace the placeholders with your actual values.

Next, install the required packages by running:

```
pip install -r requirements.txt

```

Finally, run the application by running:

```
python workout_tracker.py

```

## **Usage**

When you run the application, you'll be prompted to enter your gender, weight, height, and age. This information is used to calculate the calories burned during your workout.

You can then choose from the following options:

1. Add Workout: Enter the exercises you did and the duration, and the application will calculate the calories burned and save the data to the Google Sheet.
2. Get Details: Retrieve all the rows in the Google Sheet.
3. Delete Entry: Delete a row in the Google Sheet with the specified ID.
4. Exit: Quit the application.

## **Contributing**

If you'd like to contribute to this project, please fork the repository and create a pull request. We welcome bug reports, feature requests, and code improvements.

