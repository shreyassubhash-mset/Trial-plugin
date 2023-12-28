from gpt4all import GPT4All
import subprocess

def get_pushed_code():
    try:
        # Use git show to get the changes introduced in the last pushed commit
        code_changes = subprocess.check_output(['git', 'show']).decode('utf-8')
        return code_changes
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving code changes: {e}")
        return None
 
def review_code(commit_message):
    model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")
    prompt = f"You are a senior software engineer with a sarcastic character who wants the others to learn and enjoy it as well instead of sharing what this code does please share a single paragraph summury containing the best practices and point any optimizations or concern in the commited code then give a small example and after that always add a programming quote in the end for the given code:\
    {commit_message}. "

    # Call GPT4All to generate code review feedback
    output = model.generate(prompt)

    return output

if __name__ == "__main__":
    # Get the pushed code changes
    pushed_code = get_pushed_code()

    if pushed_code is not None:
        
        # Perform code review
        review_result = review_code(pushed_code)

        print(pushed_code)

        # Print the review result
        print(review_result)
