from langchain_core.prompts import PromptTemplate

prompt = """
You are an expert in compliance and regulatory standards. Your task is to analyze the content of a webpage to check if it complies with a given policy. 

**Policy**:
{standard}

**Webpage Content**:
I will provide you with the content extracted from the webpage at `https://mercury.com/`:

{text}

**Instructions**:
- Identify any content that does not comply with the policy points above.
- For each non-compliant issue, include the following:
  - The exact text from the webpage
  - The policy rule it violates

**Response Format**:
Please return a list of non-compliant findings in the following JSON format:

{{
  "non_compliant_issues": [
    {{
      "text": "Text that violates the policy",
      "policy_violation": "Explanation of the specific policy rule it violates"
    }},
    ...
  ]
}}
"""

LLM_PROMPT = PromptTemplate.from_template(prompt)

STANDARD_COMPLIANCE = "https://stripe.com/docs/treasury/marketing-treasury"
