import os
import argparse

def main():
    # Accessing the unique ID from the environment variable
    unique_id_env = os.getenv('UNIQUE_ID')
    print(f"Unique ID from environment variable: {unique_id_env}")

    # Accessing the unique ID from the command-line argument
    parser = argparse.ArgumentParser(description="Process unique identifier.")
    parser.add_argument('--unique-id', type=str, help='Unique identifier passed as argument')
    args = parser.parse_args()
    print(f"Unique ID from command-line argument: {args.unique_id}")

if __name__ == "__main__":
    main()
