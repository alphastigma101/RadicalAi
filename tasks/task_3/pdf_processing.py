# Necessary imports
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import os
import tempfile
import uuid

class DocumentProcessor:
    """
    This class encapsulates the functionality for processing uploaded PDF documents using Streamlit
    and Langchain's PyPDFLoader. It provides a method to render a file uploader widget, process the
    uploaded PDF files, extract their pages, and display the total number of pages extracted.
    """
    def __init__(self):
        self.pages = []  # List to keep track of pages from all documents
    
    def ingest_documents(self, filename:str): -> None
        """
            Renders a file uploader in a Streamlit app, processes uploaded PDF files,
            extracts their pages, and updates the self.pages list with the total number of pages.
            Param:
                filename: Type of file that is uploaded 
        """
        try:
            # Step 1: Render a file uploader widget. Replace 'None' with the Streamlit file uploader code.
            uploaded_files = st.file_uploader(filename, type=['.pdf'], accept_multiple_files=True)
        except:
            print("Can only upload .PDF files!")
        
        if uploaded_files is not None:
            breakpoint()
            for uploaded_file in uploaded_files:
                # Generate a unique identifier to append to the file's original name
                unique_id = uuid.uuid4().hex
                original_name, file_extension = os.path.splitext(uploaded_file.name)
                temp_file_name = f"{original_name}_{unique_id}{file_extension}"
                temp_file_path = os.path.join(tempfile.gettempdir(), temp_file_name)

                # Write the uploaded PDF to a temporary file
                with open(temp_file_path, 'wb') as f:
                    f.write(uploaded_file.getvalue())

                # Step 2: Process the temporary file
                #####################################
                # Use PyPDFLoader here to load the PDF and extract pages.
                # https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf#using-pypdf
                # You will need to figure out how to use PyPDFLoader to process the temporary file.
                
                # Step 3: Then, Add the extracted pages to the 'pages' list.
                #####################################
                loader = PyPDFLoader(temp_file_path)
                pages = loader.load_and_split() # returns a list
                for i in range(0, len(pages)):
                    self.pages.extend(pages[i]) # adds the pages to the DocumentProcessor

                # Clean up by deleting the temporary file.
                os.unlink(temp_file_path)
            
            # Display the total number of pages processed.
            st.write(f"Total pages processed: {len(self.pages)}")
        
