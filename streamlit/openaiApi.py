import json
import requests


class OpenAIAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def request_summarization(self, message):
        """
        Generates a summary using OpenAI API.

        Args:
            message (str): The message to summarize.

        Returns:
            str: The generated summary.
        """

        prompt = (f"summarize database using points in markdown language:\n\n{message}\n\n")
        # Set the API endpoint and headers
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        # Define the request payload
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"{prompt}"}]
        }

        # Convert the payload to JSON
        data = json.dumps(payload)

        # Send the POST request to OpenAI API
        response = requests.post(url, headers=headers, data=data)

        # Extract the response content
        response_data = response.json()

        # Access the generated completion
        completion = response_data["choices"][0]["message"]["content"]

        return completion

    def request_search(self, message):
        """
        Generates a search result using OpenAI API.

        Args:
            message (str): The message for the search query.

        Returns:
            str: The generated search result.
        """

        # Set the API endpoint and headers
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        # Define the request payload
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"{message}"}]
        }

        # Convert the payload to JSON
        data = json.dumps(payload)

        # Send the POST request to OpenAI API
        response = requests.post(url, headers=headers, data=data)

        # Extract the response content
        response_data = response.json()

        # Access the generated completion
        completion = response_data["choices"][0]["message"]["content"]

        return completion

    def request_organization(self, message):
        """
        Generates an organization output using OpenAI API.

        Args:
            message (str): The message for organizing the database.

        Returns:
            str: The generated organization output.
        """

        prompt = (f"Organize the database, classify similar entries into labelled groups, give the output in markdown language:\n\n{message}\n\n")
        # Set the API endpoint and headers
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        # Define the request payload
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"{prompt}"}]
        }

        # Convert the payload to JSON
        data = json.dumps(payload)

        # Send the POST request to OpenAI API
        response = requests.post(url, headers=headers, data=data)

        # Extract the response content
        response_data = response.json()

        # Access the generated completion
        completion = response_data["choices"][0]["message"]["content"]

        return completion
