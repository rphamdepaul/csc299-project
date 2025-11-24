import os
import pytest
from finalversion.ai_agent import summarize_text, ai_agent_edit

def test_summarize_text_no_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    result = summarize_text("Test input")
    assert result.startswith("[ERROR]")

def test_ai_agent_edit_no_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    result = ai_agent_edit("Test input", "Edit instruction")
    assert result.startswith("[ERROR]")

# Optionally, add a test for API error handling (simulate failure)
def test_summarize_text_api_error(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")
    def fake_client():
        class Fake:
            class chat:
                class completions:
                    @staticmethod
                    def create(**kwargs):
                        raise Exception("Simulated API failure")
        return Fake()
    monkeypatch.setattr("finalversion.ai_agent.OpenAI", fake_client)
    result = summarize_text("Test input")
    assert result.startswith("[API ERROR]")

def test_ai_agent_edit_api_error(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")
    def fake_client():
        class Fake:
            class chat:
                class completions:
                    @staticmethod
                    def create(**kwargs):
                        raise Exception("Simulated API failure")
        return Fake()
    monkeypatch.setattr("finalversion.ai_agent.OpenAI", fake_client)
    result = ai_agent_edit("Test input", "Edit instruction")
    assert result.startswith("[API ERROR]")
