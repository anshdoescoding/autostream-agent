"""
Intent Classifier for AutoStream Agent

Classifies user messages into:
1. GREETING
2. PRODUCT_INQUIRY
3. HIGH_INTENT
"""

import re

# Intent labels
GREETING = "greeting"
PRODUCT_INQUIRY = "product_inquiry"
HIGH_INTENT = "high_intent"


def classify_intent(user_message: str) -> str:
    """
    Classify user intent based on keywords and phrases.

    Args:
        user_message (str): User input message

    Returns:
        str: Detected intent
    """

    message = user_message.lower().strip()

    # Greeting intent
    if re.search(r"\b(hi|hello|hey|good morning|good evening)\b", message):
        return GREETING

    # High-intent lead signals
    if re.search(
        r"\b(sign up|subscribe|buy|purchase|try|get started|start using|"
        r"pro plan|i want to use|i want to try)\b",
        message,
    ):
        return HIGH_INTENT

    # Product / pricing inquiry
    if re.search(
        r"\b(price|pricing|cost|plan|features|what do you offer|"
        r"basic plan|pro plan)\b",
        message,
    ):
        return PRODUCT_INQUIRY

    # Default fallback
    return PRODUCT_INQUIRY
