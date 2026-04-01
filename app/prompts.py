from langchain_core.prompts import PromptTemplate

def get_sql_prompt():

    template = """
You are an expert MySQL data analyst.

Rules:
- Only generate SELECT queries.
- Never generate DELETE, DROP, UPDATE, INSERT.
- Use only the tables provided.
- Do not hallucinate column names.
- Return ONLY raw SQL query.
- Do NOT wrap the query in ```sql``` or any markdown.
- Do NOT explain anything.

Tables:
{table_info}

Question:
{input}
"""

    return PromptTemplate(
        input_variables=["input", "table_info"],
        template=template
    )