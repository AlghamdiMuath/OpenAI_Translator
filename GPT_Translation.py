# Import required libraries
import textwrap
import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv

# Load environment variables from a .env file
load_dotenv(find_dotenv())

# Function to wrap text to a given width
def wrap_text(text, width=120):
    wrapper = textwrap.TextWrapper(width=width)
    return wrapper.fill(text=text)

# Function to tokenize a given text file
def tokenize_file(file_path, model):
    with open(file_path, 'r', encoding="utf8") as file:
        text = file.read()
    encoding = tiktoken.get_encoding(model)
    tokens = encoding.encode(text)
    return tokens

# Function to split tokens into chunks of a specified size
def split_tokens_into_chunks(tokens, chunk_size):
    num_chunks = (len(tokens) + chunk_size - 1) // chunk_size
    chunks = [tokens[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)]
    return chunks

# Function to convert token chunks back into text
def convert_token_Chunks_into_text(token_chunks, model):
    encoding = tiktoken.get_encoding(model)
    text_chunks = []
    for chunk in token_chunks:
        text_chunks.append(encoding.decode(chunk))
    return text_chunks

# Function to get a translation using OpenAI's GPT-3.5-turbo
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]

# Function to generate Arabic text based on a template and English text
def runner(template, text):
    query = template + text
    arabic_text = get_completion(query)
    return arabic_text

# Define paths, chunk size, and model
file_path = 'Path_Of_Input_EnglishTextFile'
output_path = 'Path_For_Output_ArabicTextFile'
chunk_size = 1000
model = "cl100k_base"

# Tokenize the file and split into chunks
tokens = tokenize_file(file_path, model)
token_chunks = split_tokens_into_chunks(tokens, chunk_size)
text_chunks = convert_token_Chunks_into_text(token_chunks, model)
print(len(text_chunks), len(token_chunks))

# Translation template
template = '''You are a professional translator,
you excel in translating from English to Arabic
word for word maintaining the structure and the context.\
Your task is to translate the following English text to \
Arabic perfectly and without missing any words.\

English text: '''

# Translate and write to file
for text in text_chunks:
    arabic_text = runner(template, text)
    with open(output_path, 'a', encoding='utf-8') as file:
        file.write(arabic_text)
