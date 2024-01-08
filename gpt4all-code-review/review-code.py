import gpt4all as GPT4All
import subprocess
import re
import os

def is_git_repo(directory):
    return os.path.exists(os.path.join(directory, '.git'))

def get_pushed_code():
    try:
        # Check if the current directory is a git repository
        if not is_git_repo(os.getcwd()):
            print("Error: Current directory is not a git repository.")
            return None

        # Use git show to get the changes introduced in the last pushed commit
        git_diff = subprocess.check_output(['git', 'diff', 'HEAD^', 'HEAD']).decode('utf-8')

        # Extract the added and modified code using regular expressions
        added_modified_code = re.findall(r'^\+.*', git_diff, re.MULTILINE)

        # Join the code lines into a single string
        return ''.join(added_modified_code)
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving code changes: {e}")
        return None
 
def review_code(commit_message):
    model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")
    prompt = f"{commit_message}: \n You are a senior software engineer with a sarcastic character who wants the others to learn and enjoy it as well instead of sharing what this code does please share a single paragraph summury containing the best practices and point any optimizations or concern in the commited code then give a small example and after that always add a programming quote in the end for the above code. "

    # Call GPT4All to generate code review feedback
    output = model.generate(prompt)

    return output

if __name__ == "__main__":
    # Get the pushed code changes
    pushed_code = get_pushed_code()

    if pushed_code is not None:
        
        # Perform code review
        review_result = review_code(pushed_code)
        
        # Print the review result
        print(pushed_code)