import json
import os

def load_usernames(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict):
                for key in data:
                    try:
                        return {entry["string_list_data"][0]["value"] for entry in data[key]}
                    except (KeyError, IndexError, TypeError):
                        continue
            elif isinstance(data, list):
                return {entry["string_list_data"][0]["value"] for entry in data}
            else:
                print(f"Unexpected data format in {filepath}")
                return set()
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return set()

following_path = r"E:\insta_check\connections\followers_and_following\following.json"
followers_path = r"E:\insta_check\connections\followers_and_following\followers_1.json"

following = load_usernames(following_path)
followers = load_usernames(followers_path)

# Find accounts you follow but don't follow you back
not_following_back = following - followers

print("People you follow but who don't follow you back:")
for user in sorted(not_following_back):
    print(user)
