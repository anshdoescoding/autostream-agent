"""
Main entry point for AutoStream Conversational Agent
"""

from agent.agent_graph import AutoStreamAgent


def main():
    print("===================================")
    print("🤖 AutoStream AI Agent")
    print("Type 'exit' to end the conversation")
    print("===================================\n")

    agent = AutoStreamAgent("data/knowledge_base.json")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("\nAgent: Thank you for chatting with AutoStream. 👋")
            break

        response = agent.handle_message(user_input)
        print(f"\nAgent: {response}\n")


if __name__ == "__main__":
    main()
