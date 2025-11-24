import os
from openai import OpenAI


def summarize_text(text: str) -> str:
    if "OPENAI_API_KEY" not in os.environ:
        return "[ERROR] The OPENAI_API_KEY environment variable is not set."
    try:
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional task summarizer. Your ONLY job is to condense the user's input into a short, concise phrase (maximum 8 words)."},
                {"role": "user", "content": text}
            ],
            temperature=0.0
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        return f"[API ERROR] Failed to summarize. Details: {e}"

# New function for edit/fix requests
def ai_agent_edit(text: str, instruction: str) -> str:
    if "OPENAI_API_KEY" not in os.environ:
        return "[ERROR] The OPENAI_API_KEY environment variable is not set."
    try:
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert editor. Your job is to follow the user's instruction and edit the provided text accordingly. Only return the revised text, do not explain your changes."},
                {"role": "user", "content": f"Text: {text}\nInstruction: {instruction}"}
            ],
            temperature=0.2
        )
        edited = response.choices[0].message.content.strip()
        return edited
    except Exception as e:
        return f"[API ERROR] Failed to edit. Details: {e}"
