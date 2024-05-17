import streamlit as st
from tasks.task_3.pdf_processing import DocumentProcessor
from tasks.task_4.embedding_client import EmbeddingClient
from tasks.task_5.chroma_collection_creator import ChromaCollectionCreator
from tasks.task_7.task_7 import QuizGenerator
class TaskList:
    def __init__(self, model_name:str, location:str, project_id:str) -> None:
        self.project_id = project_id
        self.location = location
        self.model = model_name
        #self.embedding_client = EmbeddingCleint(self.model, self.project_id, self.location) 
        self.embedding_client = None
        self.dp = DocumentProcessor()
        self.embed_config = {
                "model_name": self.model,
                "project": self.project_id,
                "location": self.location
        }
        self.embed_client = None # Initialize from Task 4
        self.chroma_creator = None

    def task_1(self):
        """"""
        return ""

    def task_2(self):
        """"""
        breakpoint()
        self.dp.ingest_documents()
        return ""

    def task_3(self):
        """"""
        return ""
    def task_4(self):
        """"""
        breakpoint()
        self.embedding_client = EmbeddingCleint(self.model, self.project_id, self.location) # NOTE: could add this into the default constructor and will later on but I want to test it first
        vectors = self.embedding_client.embed_query("Hello World!")
        if vectors:
            print(vectors)
            print("Successfully used the embedding client!")

        return ""
    def task_5(self):
        """"""
        self.embed_client = EmbeddingClient(**embed_config) # Initialize from Task 4
        self.chroma_creator = ChromaCollectionCreator(processor, embed_client)
        with st.form("Load Data to Chroma"):
            st.write("Select PDFs for Ingestion, then click Submit")
        submitted = st.form_submit_button("Submit")
        if submitted:
            chroma_creator.create_chroma_collection()

        return ""
    def task_6(self):
        """"""
        #### Task Six #####
        # NOTE: Review the task_6.py file again 
        breakpoint()
        st.header("Quizzify") 
        screen = st.empty() # Screen 1, ingest documents
        with screen.container():
            st.header("Quizzify")
            ####### YOUR CODE HERE #######
            # 1) Initalize DocumentProcessor and Ingest Documents from Task 3
            # 2) Initalize the EmbeddingClient from Task 4 with embed config
            # 3) Initialize the ChromaCollectionCreator from Task 5
            ####### YOUR CODE HERE #######

            with st.form("Load Data to Chroma"):
                st.subheader("Quiz Builder")
                st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")

                ####### YOUR CODE HERE #######
                # 4) Use streamlit widgets to capture the user's input
                # 4) for the quiz topic and the desired number of questions
                ####### YOUR CODE HERE #######

                document = None

                submitted = st.form_submit_button("Generate a Quiz!")
                if submitted:
                    ####### YOUR CODE HERE #######
                    # 5) Use the create_chroma_collection() method to create a Chroma collection from the processed documents
                    ####### YOUR CODE HERE #######

                    # Uncomment the following lines to test the query_chroma_collection() method
                    # document = chroma_creator.query_chroma_collection(topic_input)

        if document:
            screen.empty() # Screen 2
            with st.container():
                st.header("Query Chroma for Topic, top Document: ")
                st.write(document)

        return ""
    def task_7(self):
        """"""
        return ""

if __name__ == '__main__':
    model_name = "textembedding-gecko@003"
    project = "YOUR PROJECT ID HERE"
    location = "us-central1"
    TK = TaskList(model_name, location, project_id)
    # Task One
    TK.task_1()
    # Task Two
    TK.task_2()
    # Task Three
    TK.task_3()
    # Task Four: Required to fill out a couple fields for a constructor
    TK.task_4()
    # Task Five
    TK.task_5() 
    # Task Six
    TK.task_6()
    ##### Task Seven ######
