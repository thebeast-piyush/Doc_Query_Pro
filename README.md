# Doc_Query_Pro

## 📌 Overview
**Doc_Query_Pro** is an AI-powered PDF Q&A system that allows users to upload PDF documents and ask questions about the content. The app leverages OpenAI's embeddings and FAISS for efficient document retrieval and response generation.

## 🚀 Features
- 📂 **PDF Upload & Processing**: Extracts text from uploaded PDFs.
- 🔍 **AI-Powered Q&A**: Uses OpenAI embeddings and FAISS for document-based question answering.
- 🧠 **Efficient Search**: Retrieves relevant document sections based on user queries.
- ⚡ **Streamlit UI**: Simple and interactive interface for user-friendly experience.

## 🏗 Tech Stack
- **Programming Language:** Python
- **Frameworks:** Streamlit
- **NLP Models:** OpenAI API
- **Vector Store:** FAISS
- **PDF Processing:** PyPDF2

## 📂 Project Structure
```
Doc_Query_Pro/
│── Doc_pro.py  # Main application script
│── .env        # Environment variables (API Keys)
│── requirements.txt  # Dependencies
│── README.md   # Documentation
```

## 🔧 Installation & Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/thebeast-piyush/Doc_Query_Pro.git
   cd Doc_Query_Pro
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up the OpenAI API Key**
   - Create a `.env` file and add:
     ```sh
     OPENAI_API_KEY=your_openai_api_key
     ```
   - Or set it manually in your terminal:
     ```sh
     export OPENAI_API_KEY=your_openai_api_key  # macOS/Linux
     set OPENAI_API_KEY=your_openai_api_key  # Windows
     ```
4. **Run the application**
   ```sh
   streamlit run Doc_pro.py
   ```

## 📷 Screenshots
(Add screenshots of the interface here)

## 🤝 Contributing
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request.

## 📜 License
This project is licensed under the **MIT License**.

## 📬 Contact
- **Email:** piyushtrivedi461@gmail.com
- **GitHub:** [Doc_Query_Pro](https://github.com/thebeast-piyush/Doc_Query_Pro)
