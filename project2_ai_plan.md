# Project 2: AI Features Implementation Plan for NexusLink System

## Overview
Enhance the existing NexusLink Employee & Admin Portal with **2 powerful AI-driven features** leveraging the company work policy (`policy.text`) and operational logs.

---

## 🤖 Feature 1: AI HR & Policy Assistant (Interactive Chatbot)
**Goal:** Provide employees and HR with an intelligent, 24/7 interactive assistant that answers policy questions based on `policy.text`.

### Key Capabilities:
- **Policy QA:** Instantly answers questions regarding working hours (9 AM - 5 PM), 15-min grace periods, lateness deductions, and emergency protocols.
- **Personalized Attendance Queries:** Employees can ask "Am I late today?" or "How many days was I late this week?".
- **UI Integration:** A sleek floating AI chat drawer/widget on both `index.html` and `dashboard.html`.

### Technical Stack:
- **Backend:** FastAPI endpoint `/api/ai/chat` utilizing an LLM / RAG pipeline reading `policy.text`.
- **Frontend:** Floating interactive glassmorphic chat widget in `script.js` & `style.css`.

---

## 📊 Feature 2: AI Attendance Analytics & Compliance Guard (Admin Insight Engine)
**Goal:** Automatically analyze attendance logs against `policy.text` rules to highlight compliance issues and notify HR.

### Key Capabilities:
- **Lateness & Penalty Detection:** Automatically flags check-ins after 9:15 AM (grace period) and identifies unexcused delays >60 mins (triggering half-day deduction recommendations).
- **Consecutive Violation Alerts:** Detects 3+ consecutive late days per employee and generates warning notifications for the Admin Console.
- **Smart Executive Summaries:** Provides HR with AI-generated daily/monthly attendance insights (e.g., *"Team punctuality improved by 12% this week"*).

### Technical Stack:
- **Backend:** FastAPI endpoint `/api/ai/analytics` that parses SQLite/CSV logs + policy rules.
- **Frontend:** AI Insights widget on the Admin Attendance Console in `dashboard.html`.

---

## 🚀 Execution Steps
1. **Setup AI Endpoint Engine (`main.py`):** Add `/api/ai/chat` and `/api/ai/analytics`.
2. **Policy Knowledge Base Integration:** Parse `policy.text` for contextual prompt grounding.
3. **Frontend UI Components:** Add floating AI Chatbot & Admin Insights card.
4. **Testing & Verification:** Verify AI responses against company policies and attendance logs.
