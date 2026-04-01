import streamlit as st
from app.llm import get_llm
from app.database import get_database
from app.chains import get_sql_chain
from app.guardrails import is_query_safe

# ---- Page Config ----
st.set_page_config(page_title="AI SQL Assistant", page_icon="🤖", layout="centered")

st.title("🤖 AI SQL Assistant")
st.markdown("Ask questions in natural language and get SQL + answers")

# ---- Initialize once (important for performance) ----
@st.cache_resource
def init():
    llm = get_llm()
    db = get_database()
    chain = get_sql_chain(llm, db)
    return chain

chain = init()

# ---- Session State for chat history ----
if "history" not in st.session_state:
    st.session_state.history = []

# ---- Input box ----
question = st.text_input("Ask your question:")

if st.button("Generate") and question:
    try:
        response = chain.invoke({"query": question})

        sql_query = response["intermediate_steps"][0]["sql_cmd"]

        if not is_query_safe(sql_query):
            st.error("❌ Unsafe query detected!")
        else:
            result = response["result"]

            # Save history
            st.session_state.history.append({
                "question": question,
                "sql": sql_query,
                "result": result
            })

    except Exception as e:
        st.error(f"Error: {e}")

# ---- Display history ----
for item in reversed(st.session_state.history):
    st.markdown("---")
    st.subheader("🧠 Question")
    st.write(item["question"])

    st.subheader("🛠 Generated SQL")
    st.code(item["sql"], language="sql")

    st.subheader("📊 Answer")
    st.write(item["result"])