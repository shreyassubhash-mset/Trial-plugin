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

def chunk_code(pushed_code, chunk_size):
    chunked_code = [pushed_code[i:i + chunk_size] for i in range(0, len(pushed_code), chunk_size)]
    return chunked_code

def review_code(chunked_code):
    model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")

    for chunk in chunked_code:
        prompt = f"Chunk of code: \n{chunk} \n\nYou are a senior software engineer with a sarcastic character who wants the others to learn and enjoy it as well instead of sharing what this code does please share a single paragraph summary containing the best practices and point any optimizations or concern in the commited code then give a small example and after that always add a programming quote in the end for the above code. "

        # Call GPT4All to generate code review feedback
        output = model.generate(prompt)

        # Print the review result
        print(output)

if __name__ == "__main__":
    # Get the pushed code changes
    pushed_code = get_pushed_code()

    if pushed_code is not None:
        # Chunk the code
        chunked_code = chunk_code(pushed_code, 100)

        # Perform code review
        review_result = review_code(chunked_code)

        # Print the review result
        print(pushed_code)