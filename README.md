# TravelMateAI
TravelMateAI is an AI-powered travel assistant built with Python that leverages the Groq API and function calling capabilities to deliver intelligent travel assistance through natural language conversations. The application interprets user queries and dynamically invokes Python functions to provide travel-related information such as weather updates, flight details, hotel recommendations, and popular tourist attractions.
Designed as a learning project, TravelMateAI demonstrates the practical implementation of AI-powered function calling, API integration, and conversational interfaces.
---

## Features
-  Weather information for supported destinations
-  Flight information lookup
-  Hotel recommendations
-  Tourist attraction suggestions
-  AI-powered function calling using the Groq API
-  Natural language interaction
-  Modular and easily extendable architecture
---

## Tech Stack
- Python
- Groq API
- OpenAI Python SDK
- python-dotenv
- JSON
---

## Project Structure
```text
TravelMateAI/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```
---

## installation

### 1. Clone the Repository

```bash
git clone https://github.com/siyaabhi/TravelMateAI.git
cd TravelMateAI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root and add your Groq API key.

```env
GROQ_API_KEY=your_api_key_here
```

> **Note:** Never commit your API keys to a public repository.

### 6. Run the Application

```bash
python main.py
```

---

## Example Queries

Try asking questions like:

- *What's the weather in Goa?*
- *Find flights to Bangalore.*
- *Recommend hotels in Mumbai.*
- *Suggest tourist attractions in Delhi.*
- *What are the best places to visit in Jaipur?*

---

## How It Works

1. The user submits a travel-related query.
2. The Groq AI model analyzes the request.
3. The model determines whether a predefined function should be invoked.
4. The corresponding Python function executes and retrieves structured data.
5. The AI generates a natural language response using the returned information.

This project showcases the power of **AI Function Calling**, enabling language models to interact with external tools and services intelligently.
---

## Future Enhancements

- Live weather API integration
- Real-time flight search
- Hotel booking support
- Restaurant recommendations
- Interactive Streamlit web interface
- Database integration
- User authentication
- Trip itinerary generation
- Voice-based travel assistant
- Interactive maps and navigation
---

##  Contributing

Contributions, feature requests, and suggestions are welcome.
If you'd like to contribute:
1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request
---

## License

This project is developed for educational and learning purposes. Feel free to explore, modify, and build upon it for non-commercial use.
---

## Author

**Justin P Saju**

GitHub: https://github.com/justinsaju1

---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!
