"""
RAG Pipeline for AutoStream Agent

Loads a local knowledge base and retrieves
relevant information based on user queries.
"""

import json
from typing import List


class RAGPipeline:
    def __init__(self, knowledge_base_path: str):
        """
        Initialize the RAG pipeline.

        Args:
            knowledge_base_path (str): Path to local knowledge base JSON file
        """
        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)

    def _load_knowledge_base(self, path: str) -> List[dict]:
        """Load knowledge base from JSON file."""
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def retrieve(self, query: str) -> List[str]:
        """
        Retrieve relevant knowledge snippets based on keyword matching.

        Args:
            query (str): User question

        Returns:
            List[str]: Relevant information snippets
        """
        query = query.lower()
        results = []

        for item in self.knowledge_base:
            content = item["content"].lower()
            if any(word in content for word in query.split()):
                results.append(item["content"])

        # Fallback: return all content if nothing matches
        if not results:
            results = [item["content"] for item in self.knowledge_base]

        return results
