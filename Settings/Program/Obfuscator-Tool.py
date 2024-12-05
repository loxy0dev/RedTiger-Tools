# /Settings/Program/Obfuscator-tool.py

import requests
import random
import string

def generate_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36"
    ]
    return random.choice(user_agents)

# Function to obfuscate text
def obfuscate_text(text):
    obfuscated = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(text)))
    return obfuscated

# Function to perform a request with a random user agent
def make_request(url):
    headers = {
        'User -Agent': generate_user_agent()  # Fixed the header key
    }
    response = requests.get(url, headers=headers)
    return response.text

def main():
    print("Welcome to the Obfuscator and Anonymization Tool")
    
    while True:
        print("\nMenu:")
        print("1. Change User Agent")
        print("2. Obfuscate Text")
        print("3. Make HTTP Request with Random User Agent")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            print("Generated User Agent:", generate_user_agent())

        elif choice == '2':
            text = input("Enter text to obfuscate: ")
            obfuscated_text = obfuscate_text(text)
            print("Obfuscated Text:", obfuscated_text)

        elif choice == '3':
            url = input("Enter the URL to request: ")
            try:
                response = make_request(url)
                print("Response from the server:")
                print(response)
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == '4':
            print("Exiting the tool.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
