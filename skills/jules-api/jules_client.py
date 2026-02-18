#!/usr/bin/env python3
import os
import sys
import json
import argparse
import requests

JULES_API_URL = "https://jules.googleapis.com/v1alpha"

def get_headers():
    api_key = os.environ.get("JULES_API_KEY")
    if not api_key:
        print("Error: JULES_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)
    return {
        "x-goog-api-key": api_key,
        "Content-Type": "application/json"
    }

def list_sources():
    url = f"{JULES_API_URL}/sources"
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()

def create_session(prompt, source, title=None, automation_mode="AUTO_CREATE_PR"):
    url = f"{JULES_API_URL}/sessions"
    data = {
        "prompt": prompt,
        "sourceContext": {
            "source": source,
            "githubRepoContext": {
                "startingBranch": "main"
            }
        },
        "automationMode": automation_mode,
        "title": title or "Jules Session"
    }
    response = requests.post(url, headers=get_headers(), json=data)
    response.raise_for_status()
    return response.json()

def get_session(session_id):
    url = f"{JULES_API_URL}/sessions/{session_id}"
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()

def list_activities(session_id):
    url = f"{JULES_API_URL}/sessions/{session_id}/activities"
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()

def send_message(session_id, prompt):
    url = f"{JULES_API_URL}/sessions/{session_id}:sendMessage"
    data = {"prompt": prompt}
    response = requests.post(url, headers=get_headers(), json=data)
    response.raise_for_status()
    return response.json()

def main():
    parser = argparse.ArgumentParser(description="Jules API Skill Client")
    subparsers = parser.add_subparsers(dest="command")

    # List sources
    subparsers.add_parser("list-sources")

    # Create session
    create_p = subparsers.add_parser("create-session")
    create_p.add_argument("--prompt", required=True)
    create_p.add_argument("--source", required=True)
    create_p.add_argument("--title")

    # Get session
    get_p = subparsers.add_parser("get-session")
    get_p.add_argument("--id", required=True)

    # List activities
    act_p = subparsers.add_parser("list-activities")
    act_p.add_argument("--id", required=True)

    # Send message
    msg_p = subparsers.add_parser("send-message")
    msg_p.add_argument("--id", required=True)
    msg_p.add_argument("--prompt", required=True)

    args = parser.parse_args()

    try:
        if args.command == "list-sources":
            print(json.dumps(list_sources(), indent=2))
        elif args.command == "create-session":
            print(json.dumps(create_session(args.prompt, args.source, args.title), indent=2))
        elif args.command == "get-session":
            print(json.dumps(get_session(args.id), indent=2))
        elif args.command == "list-activities":
            print(json.dumps(list_activities(args.id), indent=2))
        elif args.command == "send-message":
            print(json.dumps(send_message(args.id, args.prompt), indent=2))
        else:
            parser.print_help()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
