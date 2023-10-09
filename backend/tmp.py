from langchain.text_splitter import CharacterTextSplitter
# from langchain import OpenAI
# from langchain.llms.openai import OpenAIChat
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
import os
from langchain.docstore.document import Document
from langchain.chains import ConversationalRetrievalChain
from langchain import FewShotPromptTemplate, PromptTemplate
import json, re

root_dir = "./"
exclude_dirs = ["venv", "__pycache__"]

# loader = DirectoryLoader("./", glob='**/*.py', show_progress=True, loader_cls=TextLoader).load_and_split()

# Load
# loader = GenericLoader.from_filesystem(
#     root_dir,
#     exclude=exclude_dirs,
#     glob="**/*",
#     suffixes=[".py"],
#     parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
# )
# documents = loader.load()
# len(documents)

# from langchain.text_splitter import RecursiveCharacterTextSplitter
# python_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON, 
#                                                                chunk_size=2000, 
#                                                                chunk_overlap=200)
# texts = python_splitter.split_documents(documents)
# len(texts)

tree_map = ""
docs = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    if any(exclude in dirpath for exclude in exclude_dirs):
        continue
    for file in filenames:
        if file.endswith(".py"):
            try:
                path = os.path.join(dirpath, file)
                tree_map += path + "\n"
                # loader = TextLoader(os.path.join(dirpath, file), encoding="utf-8")
                # docs.extend(loader.load_and_split())
                file_content = open(path, 'r').read()
                preset = f"# metadata = file:{file} directory:{dirpath}"
                docs.append(Document(page_content=preset + file_content, metadata={'source':path, 'directory':dirpath, 'filename':file}))
            except Exception as e:
                pass

# docs.extend(Document(page_content=tree_map, metadata={"source": "local"}))
# print(f"{len(docs)}")

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(docs)

# texts.append(text_splitter.split_text(tree_map))
print(f"{len(texts)}")

key = "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"
embeddings = OpenAIEmbeddings(openai_api_key=key, disallowed_special=())
vectorstore = Chroma.from_documents(texts, embeddings)

# print(docsearch.get())

gpt = ChatOpenAI(openai_api_key=key, model="gpt-3.5-turbo")

from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

qa = ConversationalRetrievalChain.from_llm(gpt, vectorstore.as_retriever(), memory=memory)
# qa = RetrievalQA.from_chain_type(
#     llm=gpt, 
#     chain_type="stuff", 
#     retriever=vectorstore.as_retriever()
# )

# query()
pre_query = open("prequery.txt", 'r').read()

print(qa(pre_query))

def query(q, prequery = False):
    q = pre_query +"\n" + q if prequery else q
    q = "User : " + q + "\nAssistant : "
    answer = qa({"question": q})['answer']
    # answer = qa.run(q)
    print("Answer: ", answer)
    return answer

def extract_json_from_text(text):
    # Use regular expression to find JSON objects
    matches = re.findall(r'\{.*?\}', text, re.DOTALL)
    return matches

import json

def extract_and_write_json(text):
    # Define a regular expression pattern to find JSON objects
    # json_pattern = r'{\s*"file":\s*"(.*?)",\s*"code":\s*"(.*?)"}'

    # Define regex pattern to extract "file" and "code"
    pattern = r'"file": "(.*?)",\s+"code": "(.*?)"'

    # Search for the pattern
    match = re.search(pattern, text)

    # Extract values
    file_name = match.group(1)
    code = match.group(2).replace("\\n", "\n")

    # # Find all JSON objects in the text
    # json_objects = re.findall(json_pattern, text, re.DOTALL)

    # if not json_objects:
    #     return "No JSON objects found in the text."

    results = []

    # for file_name, code in json_objects:
    # Create the directory if it doesn't exist
    directory = os.path.dirname(file_name)
    if directory:
        os.makedirs(directory, exist_ok=True)

    # Write code to the file
    with open(file_name, 'w') as f:
        f.write(code)
    
    results.append(f"Code has been written to {file_name}")

    return "\n".join(results)


# query("", False)
# query_cmd = query("Could you give me the code to add a date attribute to the car model ?")
# print(query_cmd)
# result = interpret_json_and_write_code(query_cmd)
# print(result)


# create our examples
examples = [
    # {
    #     "query": "Could you add a date attribute to the car model ?",
    #     "answer": "{'file':'./projectname/carapp/models.py','code':'from django.db import models\n\nclass Car(models.Model):\n    id = models.AutoField(primary_key=True)\n    color = models.CharField(max_length=50)\n    date = models.DateField()\n\n    def __str__(self):\n        return f\'Car {self.id} - {self.color}\"'}"
    # },
]

# create a example template
example_template = """
User: {query}
AI: {answer}
"""

# create a prompt example from above template
example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template
)

# now break our previous prompt into a prefix and suffix
# the prefix is our instructions
prefix = """The following are exerpts from conversations with an AI
assistant.
""" + pre_query
# and the suffix our user input and output indicator
suffix = """
User: {query}
AI: """

# now create the few shot prompt template
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["query"],
    example_separator="\n\n"
)


while True:
    question = input("Query : ")
    query_cmd = query(question)
    # print(query_cmd)
    try:
        result = extract_and_write_json(query_cmd)
        print(result)
    except Exception as e :
        print(e)
