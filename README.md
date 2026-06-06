# AI Library Management System

## Project Overview
This project implements an AI-powered library management system, designed to modernize traditional library services with advanced features such as semantic search, multilingual support, personalized recommendations, and a chatbot. The system leverages machine learning models for book indexing and retrieval, and integrates with external APIs for enhanced functionalities.

## Features
-   **Semantic Book Search**: Utilizes `SentenceTransformers` and FAISS for efficient and intelligent book search based on title and description embeddings.
-   **Multilingual Support**: Supports searching and interacting with the system in multiple languages (English, Amharic, French, Arabic) through `deep-translator` and `langdetect`.
-   **Recommendation Engine**: Provides personalized book recommendations.
-   **AI Chatbot**: An intelligent assistant capable of answering questions about books and providing recommendations, powered by OpenAI's `gpt-4o-mini`.
-   **Authentication**: Basic user authentication with JWT token creation (implemented but not fully integrated into Streamlit app yet).
-   **Book Management**: Functions to borrow and return books, integrated with an SQLite database.
-   **Predictive Analytics**: Functions to predict book popularity and potential late returns.
-   **Utilities**: QR code generation for book IDs, voice-to-text input, and email notifications.
-   **Data Enrichment**: Functions to classify book difficulty and generate relevant tags.
-   **Streamlit Dashboard**: A user-friendly web interface for searching, filtering, and interacting with the library system.
-   **Modular Codebase**: Organized into `auth.py`, `engine.py`, `utils.py`, and `streamlit_app.py` for better maintainability and scalability.

## Modular Structure
The project is divided into several Python files:
-   `auth.py`: Handles user authentication, including user data management, password hashing, and JWT token creation.
-   `engine.py`: Contains the core AI search logic, including the `AIEngine` class for building and querying the FAISS index.
-   `utils.py`: A collection of utility functions for various features such as multilingual translation, AI chatbot interaction, data enrichment, QR code generation, and email services.
-   `streamlit_app.py`: The main Streamlit application that integrates all the functionalities from `auth.py`, `engine.py`, and `utils.py` to provide the user interface.
-   `requirements.txt`: Lists all Python package dependencies.
-   `google_books_dataset.csv`: The dataset used for populating the book catalog.
-   `library.db`: The SQLite database storing book, user, and borrow record information.
-   `books_index.faiss`: The FAISS index file containing book embeddings for fast semantic search.

## Setup Instructions
To get the project up and running, follow these steps:

### 1. Clone the Repository (if applicable) or Download Files
Ensure you have all the project files (`.py` files, `.csv`, `.faiss`, `.db`) in your working directory.

### 2. Install Dependencies
Install all required Python packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Data and Index Initialization
-   The `google_books_dataset.csv` should be in the same directory as your scripts.
-   The SQLite database (`library.db`) and FAISS index (`books_index.faiss`) are generated when the initial setup cells in the notebook are run. If you're running locally, ensure these files are created or present.

### 4. Configuration (Important Placeholders)
Before running the Streamlit app, you *must* address the following placeholders:

-   **`ngrok` Authentication Token**: If you plan to deploy the Streamlit app publicly via `ngrok` in a Colab environment, replace `"YOUR_NGROK_AUTH_TOKEN"` in the `ngrok` setup cell with your actual authentication token.

-   **OpenAI API Key**: For the full AI assistant features, update `api_key="YOUR_API_KEY"` in `utils.py` with your actual OpenAI API key.

-   **Email Credentials**: If you intend to use the `send_email` function, update the `username` and `password` placeholders in the `send_email` function within `utils.py` with your email login credentials.

### 5. Running the Streamlit Application
Once dependencies are installed and configurations are updated, run the Streamlit application from your terminal:

```bash
streamlit run streamlit_app.py
```
If running in Google Colab, you will typically use `ngrok` to expose the Streamlit app to a public URL.

## Usage
-   **Sidebar Filters**: Use the sidebar to filter books by category, author, or title.
-   **Multilingual Search**: Enter a search query in your preferred language, and the AI engine will translate and search for relevant books, then translate results back.
-   **AI Assistant**: Interact with the chatbot by asking questions about books or general library inquiries. Ensure your OpenAI API key is configured for optimal performance.

## Future Enhancements
-   Full integration of user authentication (`auth.py`) into the Streamlit UI.
-   Implementing the `borrow_book` and `return_book` functionalities within the Streamlit interface.
-   Developing a more robust predictive model for popularity and late returns.
-   Expanding the multilingual support to cover more languages and fine-tuning translation quality.
-   Integrating other AI models (e.g., Gemini) for the chatbot.
-   Adding admin functionalities for managing books and users.
