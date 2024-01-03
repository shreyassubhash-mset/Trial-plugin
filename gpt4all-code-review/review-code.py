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

def review_code_chunks(model, prompt, input_chunks):
    output_chunks = []

    # Process the prompt
    output_prompt = model.generate(prompt)
    output_chunks.append(output_prompt)

    # Process the remaining input chunks
    for input_chunk in input_chunks:
        output_chunk = model.generate(input_chunk)
        output_chunks.append(output_chunk)

    return output_chunks

def process_input_in_chunks(input_data, chunk_size):
    # Split input_data into chunks
    chunks = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]
    return chunks

def generate_code_overview(output_chunks):
    # Combine the outputs into a single string
    combined_output = ''.join(output_chunks)

    # Process the combined output to generate a code overview paragraph
    overview_prompt = "Provide a code overview summarizing the main points and feedback: \n" + combined_output
    overview = model.generate(overview_prompt)

    return overview

if __name__ == "__main__":
    # Get the pushed code changes
    pushed_code = get_pushed_code()

    if pushed_code is not None:
        # Specify the chunk size
        chunk_size = 800  # You can adjust this based on your requirements

        # Split pushed_code into chunks
        code_chunks = process_input_in_chunks(pushed_code, chunk_size)

        # Specify the prompt
        prompt = "You are a senior software engineer with a sarcastic character who wants the others to learn and enjoy it as well instead of sharing what this code does please share a single paragraph summury containing the best practices and point any optimizations or concern in the commited code then give a small example and after that always add a programming quote in the end for the given code: \n"

        # Initialize GPT4All model
        model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")

        # Perform code review on each chunk
        review_results = review_code_chunks(model, prompt, code_chunks)

        # Generate code overview paragraph
        code_overview = generate_code_overview(review_results)

        # Print the code overview
        print(code_overview)

