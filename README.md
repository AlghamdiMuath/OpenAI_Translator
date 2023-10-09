# Text Translation and Tokenization Pipeline: Enhanced Edition 🌐🔠

## Summary 📈

Leverage the robust capabilities of OpenAI's GPT-3.5 Turbo for advanced text translation from English to Arabic. This Python-based pipeline offers a comprehensive suite of features including text wrapping and tokenization, powered by TikToken.

---

## Table of Contents 📚

- [Summary](#summary)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Operation](#basic-operation)
  - [Configuration Options](#configuration-options)
- [Functionality Overview](#functionality-overview)
- [Contributions](#contributions)


---

## Prerequisites 🛠️

1. Python 3.x
2. OpenAI API Key
3. Pip package manager

---

## Installation 📦

1. Clone the repository to your local environment:
    ```bash
    git clone https://github.com/AlghamdiMuath/OpenAI_Translator.git
    ```
2. Change into the project directory:
    ```bash
    cd OpenAI_Translator
    ```
3. Install necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Populate the `.env` file with your OpenAI API Key:
    ```bash
    echo "OPENAI_API_KEY=your_key_here" > .env
    ```

---

## Usage 📖

### Basic Operation ⚙️

1. Place the text file to be translated at the specified `INPUT_FILE` location.
2. Execute the Python script:
    ```bash
    python main.py
    ```
3. Retrieve the translated Arabic text from the designated `OUTPUT_FILE` location.

### Configuration Options 🛠️

1. Adjust the `translation_template` for specialized translation criteria.
2. Modify `max_chunk_size` to handle large text files in segmented portions.

---

## Functionality Overview 📘

- `wrap_text_to_fixed_width()`: Text wrapping according to specified width.
- `tokenize_text_from_file()`: Tokenization of text files, supporting diverse language models.
- `partition_tokens_into_chunks()`: Token segmentation to control overflow.
- `convert_chunks_to_text()`: Conversion of token segments back into textual format.
- `get_translated_text()`: Utilizes OpenAI's GPT-3.5 Turbo for high-quality translation.
- `execute_translation()`: Coordinates the complete translation and tokenization process.

---

## Contributions 🤝

Contributions are welcome. Please feel free to fork this repository, submit pull requests, or report issues to improve the project.

