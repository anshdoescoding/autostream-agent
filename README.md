AutoStream Conversational AI Agent

>Project Overview
This project is a Conversational AI Agent built for AutoStream, a fictional SaaS platform that provides automated video editing tools for content creators.

The goal of this project is to simulate how real companies convert social media conversations into qualified leads using AI. Instead of acting like a simple chatbot, the agent understands user intent, answers product questions using stored knowledge, and captures lead details when a user shows interest in signing up.

This project was created as part of a Machine Learning Intern assignment and focuses on practical, real-world AI system design.

>What This Agent Can Do
Understand whether a user is just greeting, asking about the product, or ready to sign up
Answer pricing and feature questions using a local knowledge base (RAG)
Remember conversation context across multiple messages
Collect user details step-by-step when high intent is detected
Trigger a mock lead-capture API only after all required details are provided

>Tech Stack Used
Programming Language: Python 3.9+
Framework: LangChain (LangGraph-inspired architecture)
LLM: GPT-4o-mini (can be swapped if needed)
State Management: In-memory conversation state
Knowledge Storage: Local JSON file

>How to Run the Project Locally
Step 1: Clone the repository
git clone <https://github.com/anshdoescoding/autostream-agent>
cd autostream-agent
Step 2: Install required dependencies
pip install -r requirements.txt
Step 3: Start the agent
python main.py

>Architecture Explanation
The agent is built using a state-driven conversational workflow inspired by LangGraph concepts. Every user message first goes through an intent classification step, which decides whether the message is a greeting, a product inquiry, or a high-intent request.

When the user asks about pricing or features, the agent uses a Retrieval-Augmented Generation (RAG) approach. Instead of hardcoding answers, it retrieves relevant information from a local JSON knowledge base that contains pricing plans, features, and company policies. This ensures responses remain accurate and easy to update.

Once the user shows high intent (for example, wanting to try the Pro plan), the agent switches to a lead-collection flow. Conversation state is stored in memory, allowing the agent to collect the user’s name, email, and platform across multiple turns.

The lead-capture tool is executed only after all required details are collected, ensuring controlled and realistic backend behavior. This separation between reasoning and execution makes the agent reliable and easy to extend.

>WhatsApp Integration (Conceptual Explanation)
To integrate this agent with WhatsApp, the WhatsApp Business API can be used. Incoming user messages would be received through webhooks and forwarded to the backend service running the agent.

Each WhatsApp user can be tracked using their phone number as a session ID, allowing the agent to maintain conversation state across messages. The agent’s responses would then be sent back to WhatsApp through the API. This setup allows the same agent logic to be reused across platforms like WhatsApp, Instagram, or web chat.

>Demo Video
The demo video showcases:

The agent answering pricing questions
Detection of high-intent user behavior
Step-by-step collection of user details
Successful execution of the mock lead-capture tool

>Why This Project Works Well
Clear intent detection logic
Proper use of RAG instead of hardcoded responses
Clean state management across multiple turns
Safe and controlled tool execution
Real-world, production-style project structure

>Author
Ansh Kaushik