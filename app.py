from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain import PromptTemplate
from example import example
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env 

#Wrapper for the embeddings
import functools
class MyEmbeddings(HuggingFaceEmbeddings):

    def __call__(self, input):
        return super().__call__(input)



def get_db_chain():

    #create connection with db
    db_user = "root"
    db_password = " "
    db_host = "localhost"
    db_name = "petdata"

    db = SQLDatabase.from_uri(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
        sample_rows_in_table_info=3,
    )
    print(db.table_info)
    llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)
    
   
   
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
    
    return chain



