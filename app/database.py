from langchain_community.utilities import SQLDatabase

def get_database():
    db_user = "root"
    db_password = "dhananjay"
    db_host = "localhost"
    db_name = "atliq_tshirts"

    return SQLDatabase.from_uri(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
        sample_rows_in_table_info=3
    )