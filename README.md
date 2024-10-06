# Chat Analyzer for WhatsApp and Telegram

This project is a streamlined chat analyzer designed to work with both WhatsApp and Telegram data. It automatically detects the type of analysis based on the file format you upload:

- WhatsApp Chat Analysis for `.txt` files
- Telegram Chat Analysis for `.json` files
  
---

## Key Features
- **Automatic File Type Detection:** No need to manually specify the platform. Upload your chat file, and the app will automatically determine whether it's WhatsApp or Telegram.
- **Streamlit-based Interface:** Enjoy a user-friendly web interface built with Streamlit, making it easy to upload and analyze your chat files in just a few clicks.
- **Comprehensive Insights:** Provides in-depth analysis of chat patterns, activity trends, most active participants, and more.
- **Cross-Platform:** Supports both WhatsApp and Telegram, offering a versatile solution for analyzing your chat data from both platforms.

---

## How it Works
1. **Upload your chat file:**
- **WhatsApp:** Export chat in `.txt` format
- **Telegram:** Export data in `.json` format
2. The app automatically detects the file type and starts the appropriate analysis.
3. **Get detailed insights about your chat, including:**
- Message frequency
- Participant activity
- Time-based analysis (most active times)
- Word/emoji usage patterns
- And more!

---

## Technology Stack
- **Streamlit:** For the user interface
- **Python**: Core logic and file processing
- **Pandas & Plotly:** For data manipulation and interactive visualizations
