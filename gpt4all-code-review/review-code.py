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
    
def chunk_string(input_string, chunk_size):
    # Chunk a string into chunks of a specified size.
    return [input_string[i:i + chunk_size] for i in range(0, len(input_string), chunk_size)]

def review_code_chunks(model, prompt_chunks):
    # Process code review for each chunk and concatenate outputs.
    review_outputs = []
    for prompt_chunk in prompt_chunks:
        output_chunk = model.generate(prompt_chunk)
        review_outputs.append(output_chunk)
    return '\n'.join(review_outputs)
 
# def review_code(commit_message):
#     model = GPT4All("orca-2-13b.Q4_0.gguf")
#     prompt = f"You are a senior software engineer with a sarcastic character who wants the others to learn and enjoy it as well instead of sharing what this code does please share a single paragraph summury containing the best practices and point any optimizations or concern in the commited code then give a small example and after that always add a programming quote in the end for the given code: \n {commit_message}. "

#     # Call GPT4All to generate code review feedback
#     output = model.generate(prompt)

#     return output

if __name__ == "__main__":
    # Get the pushed code changes
    pushed_code = get_pushed_code()

    if pushed_code is not None:
        # Chunk the pushed code
        chunk_size = 1000  # Set your desired chunk size
        pushed_code_chunks = chunk_string(pushed_code, chunk_size)

        # Initialize GPT4All model
        model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")

        # Perform code review for each chunk and combine outputs
        review_result = review_code_chunks(model, pushed_code_chunks)

        # Print the review result
        print(review_result)
