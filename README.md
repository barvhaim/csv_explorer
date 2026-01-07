# CSV Explorer

A Python application that enables natural language queries on CSV data using PandasAI and LiteLLM.

## Quick Start

1. **Install dependencies**
   ```bash
   uv sync
   ```

2. **Configure environment**

   Copy `.env.example` to `.env` and add your API credentials:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` with your OpenAI-compatible API details:
   ```
   OPENAI_API_KEY=your_api_key_here
   OPENAI_BASE_URL=http://your-endpoint:4000/v1
   OPENAI_MODEL_NAME=your-model-name
   ```

3. **Add your CSV data**

   Place CSV files in the `input/` directory

4. **Run the application**
   ```bash
   python main.py
   ```

## Usage

The application allows you to ask natural language questions about your CSV data:

```python
import pandasai as pai

# Load your CSV
df = pai.read_csv("input/your_data.csv")

# Ask questions in natural language
response = pai.chat("What is the average salary by department?", df)
print(response)
```

## Example

The included `input/employees.csv` contains sample employee data. The default query asks: "Who gets paid the most?"

## Requirements

- Python >= 3.11
- UV package manager
- Access to an OpenAI-compatible LLM endpoint
