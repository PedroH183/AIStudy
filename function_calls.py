from google import genai
from google.genai import types

import os
from dotenv import load_dotenv


load_dotenv()


elastic_product_search = {
    "name": "search_elastic_product",
    "description": """
        Get the current products available in a document from elastic search
        Only call this function if the user asks for a specific product.
    """,
    "parameters": {
        "type": "object",
        "properties": {
            "product_name": {
                "type": "string",
                "description": "The name of the product to search for",
            },
        },
        "required": ["product_name"],
    },
}

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))
tools  = types.Tool(function_declarations=[elastic_product_search])
config = types.GenerateContentConfig(tools=[tools])

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="6 tem dipilona ? ",
    config=config,
)

if response.function_calls:

    function_call_name = response.function_calls[0].name
    function_call_parameters = response.function_calls[0].args

    print(f"Function to call: {function_call_name}")
    print(f"Object Complete : {function_call_parameters}")

    #  In a real app, you would call your function here:
    #  result = get_current_temperature(**function_call.args)

else:
    print("No function call found in the response.")
    print(response.text)