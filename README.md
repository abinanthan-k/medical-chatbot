# 🩺 Medical Diagnosis Chatbot

A conversational AI assistant that provides accurate and real-time answers to medical questions using a Retrieval-Augmented Generation (RAG) pipeline.

![Streamlit UI](https://github.com/user-attachments/assets/b0be61f2-79a7-49f2-bf60-b4c6aced7a84)
<!-- Replace with actual screenshot URL -->

## 🔍 Features

- 💬 **Conversational Interface**: Streamlit-powered chat UI with session-based history, user/AI avatars, and reset functionality.
- 📚 **Context-Aware Responses**: Uses vector search (Pinecone) to fetch relevant documents before generating responses with Gemini Pro.
- 🎨 **Custom Theming**: Custom icon, Google Fonts, and color customization support.
- 🚀 **Deployment-Ready**: Easily deployable to Streamlit Cloud or run locally.

## ⚙️ Tech Stack

- **Frontend**: Streamlit + Bootstrap Styling
- **Backend**: Python, LangChain, Gemini Pro (Google Generative AI)
- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Vector DB**: Pinecone
- **Environment**: dotenv for key management

## 📊 Performance Metrics

- ✅ **Retrieval Accuracy**: 90.00% on benchmarked medical queries
- ⏱️ **Average Latency**: 3.74 seconds per response

