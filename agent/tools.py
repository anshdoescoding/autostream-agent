"""
Tools for AutoStream Agent

Includes mock API functions that simulate
backend actions like lead capture.
"""


def mock_lead_capture(name: str, email: str, platform: str):
    """
    Mock function to simulate lead capture.

    Args:
        name (str): User's name
        email (str): User's email
        platform (str): Creator platform (YouTube, Instagram, etc.)
    """
    print("===================================")
    print("Lead captured successfully!")
    print(f"Name     : {name}")
    print(f"Email    : {email}")
    print(f"Platform : {platform}")
    print("===================================")
