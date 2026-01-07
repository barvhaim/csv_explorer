import os
from dotenv import load_dotenv
import pandasai as pai
from pandasai_litellm.litellm import LiteLLM

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Initialize LiteLLM with your OpenAI-compatible configuration
    llm = LiteLLM(
        model=os.getenv("OPENAI_MODEL_NAME"),
        api_key=os.getenv("OPENAI_API_KEY"),
        api_base=os.getenv("OPENAI_BASE_URL")
    )

    # Configure PandasAI to use this LLM
    pai.config.set({
        "llm": llm
    })

    # Load data from CSV file
    csv_path = "input/employees.csv"
    employees_df = pai.read_csv(csv_path)

    # Query the data
    response = pai.chat("Who gets paid the most?", employees_df)
    print(f"\nResponse: {response}")


if __name__ == "__main__":
    main()
