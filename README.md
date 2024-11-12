Ollama, an application based on llama.cpp, now allows users to run any of the 45,000+ GGUF models from Hugging Face directly on their local machines, simplifying the process of interacting with large language models for AI enthusiasts and developers alike.

# LangChain-Ollama Integration Examples

This repository demonstrates how to integrate LangChain with Ollama to interact with Hugging Face GGUF models locally. The examples show how to create simple yet powerful applications using locally-hosted language models. Here is the [link](https://medium.com/@adrian.dsa/running-hugging-face-models-locally-with-ollama-and-langchain-aa1ecd9f0d72) to an article I wrote on this topic.

## Prerequisites

- Python 3.8+
- Ollama installed and running on your system
- A Hugging Face GGUF model downloaded via Ollama

## Requirements

- langchain-ollama
- langchain

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/langchain-ollama-examples
cd langchain-ollama-examples
```
2. Install required packages:
```bash
pip install -r requirements.txt
```
## Usage

1. First, ensure Ollama is running and you have downloaded your desired model:

```bash
ollama run hf.co/username/model-repository
```

2. Run the examples:

```bash
python main.py
python main_with_memory.py
```
