# AI-Driven Data Extraction Workflow

This project is a fully functional automation blueprint for the [Make.com](https://make.com) platform, designed to intelligently and automatically extract structured financial data from unstructured text (e.g., emails, messages, or notes) using OpenAI's artificial intelligence tools.

## 🔴 The Problem We Solve
In many companies, finance, administrative, and accounting departments lose hundreds of hours every month manually reading and entering data from documents and messages.
The process of **manual data entry**:
- Is **extremely time-consuming** and repetitive.
- Leads to **human errors**, typos in amounts, and categorization mistakes.
- Hinders business scaling as revenue and document volume grow.

## 🟢 The Solution: AI-Powered Automation
This Blueprint creates a reliable pipeline where:
1. **Data Reception:** A Webhook or another integration seamlessly catches incoming, unstructured text data.
2. **AI-Driven Parsing:** The query is formatted and sent to **OpenAI models (GPT / o1)** using specially crafted Prompt Engineering. The AI effectively recognizes key data points, such as dates, amounts, contractors, cost descriptions, or financial categories, intending to generate a clean, strict format (e.g., JSON).
3. **Structured Storage:** The ready-to-use information is sent automatically and effortlessly into the appropriate databases or structures (in this example: Core Banking systems or a designated Google Sheet).

## 📈 Business Benefits
- **Cost and Time Reduction (ROI):** Reduces data administration time by 90%+. The team can focus on strategic verification, controlling, and analysis instead.
- **Error Resistance (Consistency):** Replaces error-prone manual entry with standardized JSON extraction by LLMs, which is far more consistent and reliable.
- **Instant Access to Information:** Continuous, real-time financial tracking, without waiting for batch manual accounting by an employee.
- **Security and Configuration Anonymity:** The template in this repository has sanitized sensitive inputs (such as emails, system connections), allowing for free sharing of the processes while protecting private data.

## ⚙️ How to Run the Project (Using the Template)
Keep private data such as your email address, OpenAI / Google connection IDs, or Google Sheets IDs in a special `.json` file to avoid exposing them in a GitHub repository!

1. Create a file named `variables.json` on your local drive (it is included in `.gitignore`, so it won't accidentally be pushed to the web):
```json
{
  "YOUR_EMAIL": "your_email_address@example.com",
  "YOUR_SPREADSHEET_ID": "your-spreadsheet-id",
  "OPENAI_CONNECTION_ID": 1111111,
  "GOOGLE_CONNECTION_ID": 2222222
}
```

2. Run the Python script from your terminal:
```bash
python3 apply_variables.py
```

The script will read the `AI_Financial_Extraction.blueprint.json` file, inject your secure text variables into it, and create a ready-to-import file named `AI_Financial_Extraction_Ready.json`.

3. Import this final generated file directly into the Make.com platform interface. You're done!
