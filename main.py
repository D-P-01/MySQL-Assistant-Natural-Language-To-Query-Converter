from app.llm import get_llm
from app.database import get_database
from app.chains import get_sql_chain
from app.guardrails import is_query_safe

def main():

    llm = get_llm()
    db = get_database()
    chain = get_sql_chain(llm, db)

    print("AI SQL Assistant Ready 🚀")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("Ask your question: ")

        if question.lower() == "exit":
            break

        try:
            response = chain.invoke({"query": question})

            # Extract generated SQL
            sql_query = response["intermediate_steps"][0]["sql_cmd"]

            if not is_query_safe(sql_query):
                print("❌ Unsafe query detected!")
                continue

            print("\nGenerated SQL:")
            print(sql_query)

            print("\nAnswer:")
            print(response["result"])
            print("\n" + "-"*50)

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()