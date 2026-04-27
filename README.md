# Video Question Answering System (RAG-based)

## 📌 Description
This project allows users to ask questions about video content.
It accepts a single video file, a folder containing multiple videos, or a parquet file as input.
The video content is processed and queried using a Retrieval-Augmented Generation (RAG) pipeline,
and answers are generated using the LLaMA 3.2 language model.

-----------------------------------------------------------------------------------------------------------------

## ✨ Main Features
- Accepts **single video files**, **folders with multiple videos**, or **parquet files** as input
- Automatically processes video data for question answering
- Uses **Retrieval-Augmented Generation (RAG)** for accurate and context-aware responses
- Answers user questions using the **LLaMA 3.2** language model
- Modular and extensible pipeline for future improvements

-----------------------------------------------------------------------------------------------------------------

## 🧠 How It Works 
1. Video input is processed and converted into text representations
2. Relevant information is retrieved based on the user’s query
3. Retrieved context is passed to the LLaMA 3.2 model
4. The model generates a final answer grounded in the video content

-----------------------------------------------------------------------------------------------------------------

## 🛠️ Tech Stack
- Python
- NumPy
- Pandas
- scikit-learn
- Requests
- FFmpeg
- OpenAI Whisper (Speech-to-Text)
- LLaMA 3.2 (LLM)

-----------------------------------------------------------------------------------------------------------------

## ⚙️ Installation

Step 1. Clone the repository

git clone <url>

-----------------------------------------------------------------------------------------------------------------

Step 2. Install llama3.2 with ollama

Visit https://ollama.com/

install ollama and run the setup file

open terminal and run -

ollama pull llama3.2

-----------------------------------------------------------------------------------------------------------------

Step 3. Install requirements.txt

open terminal and run - 

pip install -r requirements.txt

-----------------------------------------------------------------------------------------------------------------

Step 4. Run the project

open the project directory in your terminal and run - 

python main.py

or use any code editor you like and run the main.py file.

-----------------------------------------------------------------------------------------------------------------

Note - 
While pasting the file/folder location after running the project make sure that the location is not in inverted comma, if there is inverted comma just remove it manually.