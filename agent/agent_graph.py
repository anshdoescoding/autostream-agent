from agent.intent_classifier import classify_intent, GREETING, HIGH_INTENT
from agent.rag_pipeline import RAGPipeline
from agent.tools import mock_lead_capture


class AgentState:
    def __init__(self):
        self.expecting = None  # name | email | platform
        self.name = None
        self.email = None
        self.platform = None


class AutoStreamAgent:
    def __init__(self, knowledge_base_path: str):
        self.state = AgentState()
        self.rag = RAGPipeline(knowledge_base_path)

    def handle_message(self, user_message: str) -> str:
        # 🔴 PRIORITY: lead collection
        if self.state.expecting == "name":
            self.state.name = user_message.strip()
            self.state.expecting = "email"
            return "Thanks! Could you please share your email address?"

        if self.state.expecting == "email":
            self.state.email = user_message.strip()
            self.state.expecting = "platform"
            return "Great! Which creator platform do you use? (YouTube, Instagram, etc.)"

        if self.state.expecting == "platform":
            self.state.platform = user_message.strip()
            self.state.expecting = None

            mock_lead_capture(
                self.state.name,
                self.state.email,
                self.state.platform,
            )
            return "🎉 You’re all set! Our team will contact you shortly."

        # 🔵 Normal intent flow
        intent = classify_intent(user_message)

        if intent == GREETING:
            return "Hello! 👋 How can I help you with AutoStream today?"

        if intent == HIGH_INTENT:
            self.state.expecting = "name"
            return "Great! I'd be happy to get you started. What’s your name?"

        # 🔵 RAG response (ALWAYS returns text)
        docs = self.rag.retrieve(user_message)
        response = "Here’s what I found:\n\n"
        for doc in docs:
            response += f"- {doc}\n"

        return response
