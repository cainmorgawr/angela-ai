def generate_content(client, messages):
    from call_function import available_functions

    # Create a chat completion request to the OpenRouter API
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        temperature=0,
    )


    return response

def main():
    print("Hello from angela-ai!")

    import os
    import json
    import argparse
    from dotenv import load_dotenv
    from openai import OpenAI
    from prompts import system_prompt

    # Load the OpenRouter API key from environment variables
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    # Check if the API key is set
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY is not set in the environment variables.")

    # Import the OpenAI client from the openai package
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    # Set up argument parsing for user input
    parser = argparse.ArgumentParser(description="Angela AI")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    # Create a list of messages for the chat completion request
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    # Generate content using the OpenRouter API
    response = generate_content(client, messages)

    # Check if the response usage is None and raise an error if it is
    if response.usage is None:
        raise RuntimeError("Response usage is None. Unable to retrieve token usage information.")
    else:
        if args.verbose:
            # Print the user prompt and number of tokens used in the request and response
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")

    # Generate the message content from the response
    message = response.choices[0].message
    if message.tool_calls is None or len(message.tool_calls) == 0:
        print(f"Response: {message.content}")
    else:
        # If there are tool calls, print the tool call information
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")


if __name__ == "__main__":
    main()
