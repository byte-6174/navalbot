from langchain.document_loaders import PagedPDFSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import Prompt
from langchain import OpenAI, LLMChain
import os

index_name = 'navalmanack_faiss_index'
def pdf_to_embeddings(pdf_file):
    """reads pdf, and generates embedding index. 
       Gets rid of front and back matter of the book.
    Args:
        pdf_file (str): provide the pdf file name
    """
    # save the index once
    loader = PagedPDFSplitter(pdf_file)
    pages = loader.load_and_split()

    # get rid of front/back matter of the book
    pages = pages[17:-14]

    # calculate embedding index
    faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())

    # Save the index to disk
    faiss_index.save_local(index_name)

def load_embeddings(faiss_name):
    # Load the cached embeddings
    return FAISS.load_local(faiss_name, OpenAIEmbeddings())

def main():

    if not os.path.exists(index_name):
        print('Downloading pdf to learn about Naval...')
        # if the index is not generated, download the pdf and generate the index
        import requests
        navalmanck_url = 'https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf'
        pdf_name = 'navalmanack.pdf'
        response = requests.get(navalmanck_url)
        # Save the PDF
        if response.status_code == 200:
            with open(pdf_name, "wb") as f:
                f.write(response.content)
        else:
            print(response.status_code)

        # Generate embeddings from extracred pdf and save them
        print('saving embeddings...')
        pdf_to_embeddings(pdf_name)

    # Load the embeddings
    print('Loading embeddings...')
    faiss_index = load_embeddings(index_name)

    # Load the prompt master that primes the bot in believing it is naval.
    # Change as you see fit.
    with open("master.txt", "r") as f:
        promptTemplate = f.read()

    prompt = Prompt(template=promptTemplate, input_variables=["history", "context", "question"])

    llmChain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0.25))

    def onMessage(question, history):
        docs = faiss_index.similarity_search(question)
        contexts = []
        for i, doc in enumerate(docs):
            contexts.append(f"Context {i}:\n{doc.page_content}")
            answer = llmChain.predict(question=question, context="\n\n".join(contexts), history=history)
        return answer

    history = []
    while True:
        question = input("Ask a question to NavalBot> ")
        if not question:
            print('ask a real question!')
        else:
            answer = onMessage(question, history)
            print(f"NavalBot: {answer}")
            history.append(f"Human: {question}")
            history.append(f"NavalBot: {answer}")

if __name__ == "__main__":
    main()