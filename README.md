# OpenAI_Translator
# OpenAI_Translator
# README for Text Translation and Tokenization Pipeline 🌐🔠

## Overview 📑

This Python script provides a pipeline for text translation and tokenization. Specifically, it focuses on translating English text to Arabic, while also implementing text wrapping and tokenization features. It integrates OpenAI's GPT-3 and TikToken for generating the translations and handling tokens.

---

## Table of Contents 📖

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Contribution](#contribution)

---

## Installation 🛠️

1. Clone the GitHub repository:
    ```
    git clone https://github.com/AlghamdiMuath/OpenAI_Translator.git
    ```
2. Navigate into the directory:
    ```
    cd OpenAI_Translator
    ```
3. Install required Python packages:
    ```
    pip install -r requirements.txt
    ```
4. Add your OpenAI API Key to the PATH as `OPENAI_API_KEY=your_key_here`.

---

## Usage 🚀

1. Place the text file to be translated into the `file_path` directory.
2. Run the main script:
    ```
    python main.py
    ```
3. The translated text will be saved into the `output path` file.

---

## Code Structure 🏗️

- `wrap_text()`: Wraps text to a specified width.
- `tokenize_file()`: Tokenizes a text file using TikToken.
- `split_tokens_into_chunks()`: Splits tokens into smaller chunks.
- `convert_token_Chunks_into_text()`: Converts token chunks back to text.
- `get_completion()`: Retrieves translation from OpenAI GPT-3.
- `runner()`: The main function that handles the translation pipeline.

---

## Contribution 👥

Feel free to contribute to this project by forking the repository and making pull requests, or by opening issues with suggestions and bug reports!
