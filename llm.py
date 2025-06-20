import openai
import os

# Set your OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure you set your API key as an environment variable

def get_response(prompt):
    # Use OpenAI's GPT-4 model to generate a response (updated API)
    response = openai.completions.create(  # Updated method name for OpenAI 1.0.0+
        model="gpt-4",  # Specify GPT-4 model (or "gpt-3.5-turbo" if you're using that)
        prompt=prompt,  # Pass the input prompt to the model
        max_tokens=150,  # Limit the response to a maximum number of tokens (words)
        temperature=0.7  # Controls the creativity of the response (0 = deterministic, 1 = creative)
    )
    return response['choices'][0]['text'].strip()  # Return the generated response

if __name__ == "__main__":
    # Example usage
    prompt = "What are the first steps to troubleshoot a robot arm not moving?"
    response = get_response(prompt)
    print(response)  # Print the model's response
