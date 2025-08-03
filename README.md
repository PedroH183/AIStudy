# AIStudy

A Python project for studying AI capabilities, specifically focusing on Google's Generative AI (Gemini) with function calling features.

## Project Structure

```
aistudy/
├── main.py              # Main entry point
├── function_calls.py    # Function calling implementation with Google Gemini
├── .env                 # Environment variables (API keys)
├── pyproject.toml       # Project configuration and dependencies
└── README.md           # This file
```

## Dependencies

- `google-genai>=1.27.0` - Google's Generative AI library
- `python-dotenv>=1.1.1` - Environment variable management

## Modules

### Function Calls Module

The [`function_calls.py`](function_calls.py) module demonstrates how to:

- Configure Google Gemini AI with custom function declarations
- Define function schemas for AI to understand and call
- Handle AI responses that include function calls
- Implement a product search function declaration for Elasticsearch integration

#### Key Components:

- **Function Declaration**: `elastic_product_search` - Defines a schema for product search functionality
- **AI Client Configuration**: Sets up Gemini 2.5 Flash model with function calling capabilities
- **Response Handling**: Processes AI responses to detect and extract function calls

#### Usage Example:

The module currently demonstrates searching for products with a Portuguese query "6 tem dipilona ?" and shows how the AI can interpret this as a product search request.

## Setup

1. Install dependencies using uv:
   ```bash
   uv sync
   ```

2. Set up your Google AI API key in the `.env` file:
   ```
   GENAI_API_KEY=your_api_key_here
   ```

3. Run the function calls example:
   ```bash
   python function_calls.py
   ```

## Future Modules

This project is designed to be expanded with additional AI study modules covering:
- More function calling patterns
- Different AI model integrations
- Advanced prompt engineering techniques
- Multi-modal AI capabilities

## Requirements

- Python 3.13+
- Google AI API key