# Video Question Answering System (RAG-based)

## 📌 Description
This project allows users to ask natural language questions about video content.
It accepts a single video file, a folder containing multiple videos, or a parquet file as input.
The video content is processed and queried using a Retrieval-Augmented Generation (RAG) pipeline,
and answers are generated using the LLaMA 3.2 language model.

The project was built to understand and experiment with how RAG systems work end-to-end,
especially in multimodal (video → text → answer) scenarios.

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

1. Clone the repository

git clone url

-----------------------------------------------------------------------------

2. Install ffmpeg
Step 1: Download FFmpeg

Go to ffmpeg.org

Click Download

Under Windows, choose a static build

Usually from “gyan.dev” or “BtbN builds”

Download the ZIP file

---------------------------------------------------------

Step 2: Extract the files

Right-click the ZIP → Extract All

Move the extracted folder to:

C:\ffmpeg

(You should see a bin folder inside it)

---------------------------------------------------------

Step 3: Add FFmpeg to PATH

Press Win + R → type sysdm.cpl → Enter

Go to Advanced → Environment Variables

Under System variables, find Path → Edit

Click New → add:

C:\ffmpeg\bin

Click OK everywhere

--------------------------------------------------------

Step 4: Verify installation

Open Command Prompt

Run:

ffmpeg -version

✅ If version info appears, FFmpeg is ready!

-----------------------------------------------------------------------------------------------------------------

3. Install llama3.2 with ollama

Visit https://ollama.com/

install ollama and run the setup file

open terminal and run -

ollama pull llama3.2

You are all set !!

4. Install requirements.txt

open terminal and run - 

pip install -r requirements.txt

5. Run the project

open the project directory in your terminal and run - 

python main.py

or use any code editor you like and run the main.py file.

Note - 
While pasting the file/folder location after running the project make sure that the location is not in inverted comma. if there is inverted comma just remove it manually.