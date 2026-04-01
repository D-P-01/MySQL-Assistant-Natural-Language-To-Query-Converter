<h1>🤖 AI SQL Assistant</h1>

<p>
An AI-powered SQL assistant that converts natural language questions into SQL queries and executes them on a database.
Built using LLMs, Streamlit UI, and modular backend architecture.
</p>

<hr>

<h2>🚀 Features</h2>

<ul>
  <li>Convert natural language → SQL queries</li>
  <li>Execute SQL on connected database</li>
  <li>Safety guardrails to prevent unsafe queries</li>
  <li>Streamlit-based interactive UI</li>
  <li>CLI version for testing</li>
  <li>Modular and scalable code structure</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre>
project/
│
├── app/
│   ├── llm.py              # LLM initialization
│   ├── database.py         # DB connection
│   ├── chains.py           # SQL chain logic
│   ├── guardrails.py       # Query safety checks
│
├── main.py                 # CLI version
├── streamlit_app.py        # Streamlit UI
├── .env                    # Environment variables (not pushed)
├── .gitignore
└── README.md
</pre>

<hr>

<h2>⚙️ Setup Instructions</h2>

<h3>1. Clone the repository</h3>

<pre>
git clone https://github.com/your-username/ai-sql-assistant.git
cd ai-sql-assistant
</pre>

<h3>2. Create virtual environment</h3>

<pre>
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
</pre>

<h3>3. Install dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>4. Setup environment variables</h3>

<p>Create a <code>.env</code> file in root directory:</p>

<pre>
OPENAI_API_KEY=your_api_key
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_db
</pre>

⚠️ Do NOT push <code>.env</code> to GitHub

<hr>

<h2>▶️ Running the Application</h2>

<h3>Run CLI version</h3>

<pre>
python main.py
</pre>

<h3>Run Streamlit UI</h3>

<pre>
streamlit run streamlit_app.py
</pre>

<hr>

<h2>🧠 Example Usage</h2>

<ul>
  <li>"Show all users"</li>
  <li>"Get total sales for last month"</li>
  <li>"Top 5 customers by revenue"</li>
</ul>

<hr>

<h2>🔒 Safety</h2>

<p>
The application uses guardrails to prevent execution of unsafe SQL queries such as:
</p>

<ul>
  <li>DROP</li>
  <li>DELETE</li>
  <li>TRUNCATE</li>
</ul>

<hr>

<h2>💡 Future Improvements</h2>

<ul>
  <li>FastAPI backend for production</li>
  <li>Authentication & authorization</li>
  <li>Query approval workflow</li>
  <li>Chat-based UI</li>
  <li>Support for multiple databases</li>
</ul>

<hr>

<h2>🙌 Author</h2>

<p>
Built for learning
</p>