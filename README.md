Gemini-Powered Research Agent

This project is a powerful, autonomous AI research assistant built with Python, LangChain (using LangGraph), and Google's Gemini Pro model. It's designed to function as a ReAct-style agent, capable of using multiple tools to gather, synthesize, and save information.

🚀 Features

Multi-Tool Integration: The agent can dynamically choose which tool to use for a given task.

Live Web Search: Uses DuckDuckGo (search_tool) to get current events and real-time information.

Encyclopedic Knowledge: Uses Wikipedia (wiki_tool) for historical, biographical, and well-established facts.

File Saving: Can save its final, synthesized research to a text file (save_tool).

Agentic Logic with LangGraph: Built on a modern LangGraph state machine, allowing for complex, multi-step reasoning and a robust "thought-action-observation" loop.

Powered by Google Gemini: Uses the gemini-2.5-flash model for fast, high-quality reasoning and tool calling.

🛠️ Setup and Installation

Follow these steps to get the agent running on your local machine.

1. Clone the Repository

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name


2. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate


3. Install Dependencies

Install all the required Python packages from the requirements.txt file.

pip install -r requirements.txt


4. Set Up Your Environment Variables

This project requires a Google API key to use the Gemini model.

Rename the .env.example file (or create a new file) to .env.

Open the .env file and add your Google API key:

# Get your key from Google AI Studio: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
GOOGLE_API_KEY="YOUR_API_KEY_HERE"


🏃‍♂️ How to Run the Agent

With your virtual environment active and your .env file set up, simply run the main script:

python main.py


The script will greet you and ask for a research topic. The agent's thought process and tool usage will be printed to the console in real-time.

Example Prompts to Try:

Simple Web Search:

"What are the main features of Google's latest Gemini model, and when was it announced?"

Simple Wikipedia Search:

"Can you give me a detailed biography of Marie Curie, focusing on her scientific achievements?"

Multi-Tool Synthesis:

"Who is the current CEO of Microsoft? Also, please provide a brief history of the company's founding."

Full Workflow (including saving the file):

"Please research the pros and cons of nuclear energy, citing your sources. When you are finished, save the full summary to a file named 'nuclear_energy_report.txt'."