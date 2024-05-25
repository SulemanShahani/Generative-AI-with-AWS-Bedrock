# Chat with PDF using AWS Bedrock 💬

This project allows you to interactively chat with PDF documents using AWS Bedrock for embeddings and language model responses. You can ask questions related to the content of PDF files, and the system will generate responses based on the provided context.

## Features

- **PDF Data Ingestion**: Load PDF documents and split them into manageable chunks for processing.
- **Vector Embedding**: Use AWS Bedrock to generate vector embeddings for the text content of PDF files.
- **Language Model Interaction**: Engage with language models provided by AWS Bedrock to generate responses to user queries.
- **Streamlit Interface**: Utilize Streamlit for building an interactive web application for chatting with PDFs.

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Ensure you have your AWS credentials set up or configure them as needed.
4. Run the Streamlit application by executing `streamlit run app.py` in your terminal.
5. Interact with the web interface to ask questions and receive responses based on the content of PDF files.

## File Structure

- `app.py`: Main Python script containing the Streamlit application logic.
- `requirements.txt`: File listing all Python dependencies required for the project.
- `data/`: Directory containing PDF files to be processed.
- `README.md`: This file, providing an overview of the project and instructions for usage.

## Additional Notes

- Ensure that your AWS credentials are properly configured to access the Bedrock runtime services.
- The PDF documents should be placed in the `data/` directory for ingestion.
- You can customize the language models and parameters used for generating responses by modifying the code in `app.py`.




