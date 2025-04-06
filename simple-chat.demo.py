import asyncio
import json
import os

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)


def load_config():
    """Load configuration from the config.json file."""
    home_dir = os.getenv("HOME")
    config_path = os.path.join(home_dir, "config.json")
    with open(config_path, "r") as config_file:
        return json.load(config_file)


def initialize_kernel(config):
    """Initialize the kernel and add Azure OpenAI chat completion."""
    kernel = Kernel()
    chat_completion = AzureChatCompletion(
        deployment_name=config["deployment_name"],
        api_key=config["api_key"],
        base_url=config["base_url"],
    )
    kernel.add_service(chat_completion)
    return kernel, chat_completion


async def get_ai_response(chat_completion, history, kernel):
    """Get a response from the AI based on the chat history."""
    execution_settings = AzureChatPromptExecutionSettings()
    result = await chat_completion.get_chat_message_content(
        chat_history=history,
        settings=execution_settings,
        kernel=kernel,
    )
    return result


async def chat():
    """Simplified chat function for a single user input."""
    config = load_config()
    kernel, chat_completion = initialize_kernel(config)
    history = ChatHistory()

    # Collect user input
    user_input = input("User > ")

    # Add user input to the history
    history.add_user_message(user_input)

    # Get the response from the AI
    result = await get_ai_response(chat_completion, history, kernel)

    # Print the results
    print("Assistant > " + str(result))


if __name__ == "__main__":
    asyncio.run(chat())