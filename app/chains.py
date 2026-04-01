from langchain_experimental.sql import SQLDatabaseChain
from langchain_classic.memory import ConversationBufferMemory
from app.prompts import get_sql_prompt

def get_sql_chain(llm, db):

    memory = ConversationBufferMemory(return_messages=True)

    return SQLDatabaseChain.from_llm(
        llm=llm,
        db=db,
        prompt=get_sql_prompt(),
        memory=memory,
        verbose=True,
        return_intermediate_steps=False
    )