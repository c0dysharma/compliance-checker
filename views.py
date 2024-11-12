import json
import os
import re
from dotenv import load_dotenv
from flask import request
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import UnstructuredURLLoader
from app import app
from helper.constants import LLM_PROMPT, STANDARD_COMPLIANCE

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.9, google_api_key=os.getenv('GEMINI_API_KEY'))
standard_text = None

# Custom parser
def extract_json(message):
    text = message.content
    # Define the regular expression pattern to match JSON blocks
    pattern = r"\`\`\`json(.*?)\`\`\`"

    # Find all non-overlapping matches of the pattern in the string
    matches = re.findall(pattern, text, re.DOTALL)

    # Return the list of matched JSON strings, stripping any leading or trailing whitespace
    try:
        return [json.loads(match.strip()) for match in matches]
    except Exception:
        print(f"Failed to parse: {message}")
        raise ValueError("Failed to parse data")

def invoke_llm(prompt):
    # Send the prompt to the LLM and return content
    response = llm.invoke(prompt)
    return extract_json(response)
    
    
def get_text_content_from_url(url):
    # Load the webpage content from the given URL and return it as a string
    loader = UnstructuredURLLoader(urls=[url])
    data = loader.load()
    return data[0].page_content

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/compliance', methods=['POST'])
def compliance_checker():
    url = request.get_json().get('url', None);
    if(not url):
        return {"success" : False, "error": "Please provide url"}
    
    global standard_text
    
    if(standard_text is None):
        standard_text = get_text_content_from_url(STANDARD_COMPLIANCE)
        
    to_be_tested_text = get_text_content_from_url(url)
    
    try:
        result = invoke_llm(LLM_PROMPT.format(standard=standard_text, text=to_be_tested_text))
    
        return {"success": True, "data": result}

    except Exception as e:
        return {"success": False, "error": e}
    
