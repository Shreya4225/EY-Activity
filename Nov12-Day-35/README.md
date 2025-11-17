# 📬 AI Newsletter Assistant  
### *Automated Daily AI News Digest Powered by LLM Agents & LangGraph*

> Stay updated with the fast-moving AI world — completely hands-free 🚀

![banner](https://dummyimage.com/1200x250/3B82F6/ffffff&text=AI+Newsletter+Assistant)

---

## 📌 Overview

AI innovations are happening every hour — but people don’t have time to track everything.  
The **AI Newsletter Assistant** solves this by:

✔ Automatically fetching the latest AI news  
✔ Summarizing important updates using LLM  
✔ Generating a polished newsletter  
✔ Sending it to all subscribers — daily at 9 AM  

**Zero manual effort. Fully autonomous.**

---

## ✨ Key Features

| Feature | Status |
|--------|:------:|
| Daily automated AI newsletters | ✔ |
| Multi-agent workflow (Fetcher → Summarizer → Writer → Sender) | ✔ |
| Beautiful Streamlit dashboard | ✔ |
| Preview newsletters in-app | ✔ |
| Manual instant trigger | ✔ |
| Custom topic selection | ✔ |
| Email delivery via SMTP | ✔ |
| Logs + Cache storage | ✔ |

---

## 🧠 Tech Stack & Architecture

| Component | Technology |
|----------|------------|
| LLM | OpenRouter (Llama-3 model) |
| Agent Workflow | LangChain + LangGraph |
| UI | Streamlit |
| Automation | APScheduler |
| Emailing | Gmail SMTP |
| Data Storage | JSON |
| Logging | Rotating logs |

### 🧩 Architecture Diagram
```
User
│
▼
Streamlit Dashboard
│ (Manual Trigger or Scheduler)
▼
LangGraph Workflow
├── Fetcher Agent → Fetch AI News
├── Summarizer Agent → Compress info
├── Writer Agent → Create HTML newsletter
└── Email Agent → Send to all subscribers
│
▼
Subscriber Inbox 💌
```


---

## 🖥️ UI Screenshots  
> *(Add once you upload images — placeholders below)*

| Home Overview | Newsletter Preview |
|--------------|------------------|
| *(screenshot here)* | *(screenshot here)* |

---

## 📂 Project Structure
```
NewsAssistant/
│
├─ agents/
│   ├─ fetcher_agent.py
│   ├─ summarizer_agent.py
│   ├─ writer_agent.py
│   └─ email_agent.py
│
├─ langgraph_workflow/
│   ├─ graph_definition.py
│   └─ scheduler.py
│
├─ utils/
│   └─ logger.py
│
├─ config/
│   └─ settings.py
│
├─ data/
│   ├─ subscribers.json
│   └─ cache/
│       └─ newsletter.html
│
├─ app.py             # Streamlit Dashboard UI
├─ main.py            # CLI-based workflow execution
├─ requirements.txt
└─ README.md

```


---

## ⚙️ Setup Instructions

### 🔧 1️⃣ Install Dependencies
```
pip install -r requirements.txt
```
🔐 2️⃣ Add Your .env
```
OPENROUTER_API_KEY=your_key
NEWS_API_KEY=your_key
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```

▶️ 3️⃣ Run the Dashboard
```
streamlit run app.py
```

⏱️ 4️⃣ Start Scheduler (Daily Automation)
```
python -m langgraph_workflow.scheduler
```


---

## 💼 Business Value & Monetization Model

Ready-to-launch SaaS product with multiple income streams:

- 💰 Subscription revenue  
  - ₹199/month per subscriber for AI newsletter  
  - ₹499/month for multi-topic packs

- 🏢 B2B White-Labelling  
  - Automate daily newsletters for startups, schools, research teams  
  - ₹3,000 – ₹10,000 per company per month

- 🧩 Custom Topics as Add-on  
  - Finance, Crypto, Cybersecurity, Sports, Stock Market News, etc.

- 📊 Premium Analytics Dashboard  
  - Track engagement, readership, trending topics

- ⚙️ Automation = High ROI  
  - Low operational cost → high recurring revenue 🚀

---

## 🚀 Future Enhancements

- AI-generated thumbnails for news
- Authentication + multi-user SaaS portal
- Analytics and performance insights dashboard
- Web / mobile deployment
- Multi-language newsletter support

---

## 🤝 Contributing

Pull Requests are welcome!  
For major changes, please open an issue first to discuss improvements.

---

## ⭐ Show Your Support

If you like this project:

- ⭐ Star this repo
- 🍴 Fork it
- 📰 Try building your own newsletter niche!

---

## 📫 Contact

**Developer:** Shreya Jaygude  
**Email:** shreyajaygude425@gmail.com  
**LinkedIn / Portfolio:** 

---

## 🏁 Final Note

This system saves hours of manual effort every day,  
runs fully autonomously,  
and has real monetization potential.

