import os
from openai import OpenAI

TASK_DESCRIPTIONS = [
    """
    The marketing team requires a full analysis of the Q3 campaign performance across all
    social media platforms, including detailed metrics on engagement rate, conversion rate,
    and cost per acquisition. This data must be compiled into a single, executive-level
    report with visualizations and presented to management by the end of the week.
    """,
    """
    We need to upgrade the database server from PostgreSQL 13 to PostgreSQL 16. This involves
    creating a staging environment, testing the application for compatibility with the new
    version, performing a dump and restore of the production data, and monitoring the
    system for 48 hours post-migration to ensure stability and performance.
    """
]

def summarize_task(description: str) -> str:
    if "OPENAI_API_KEY" not in os.environ:
        return "[ERROR] The OPENAI_API_KEY environment variable is not set."

    try:
        client = OpenAI()

        print(f"-> Summarizing: {description.strip()[:50]}...")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional task summarizer. Your ONLY job is to condense the user's input into a short, concise phrase (maximum 8 words)."
                },
                {
                    "role": "user",
                    "content": description
                }
            ],
            temperature=0.0
        )

        summary = response.choices[0].message.content.strip()
        return summary

    except Exception as e:
        return f"[API ERROR] Failed to summarize. Details: {e}"


def main():
    print("--- 📝 Starting Task Summarization ---")
    
    for i, description in enumerate(TASK_DESCRIPTIONS):
        summary = summarize_task(description)
        
        print(f"\n## Summary {i+1}")
        print(f"   Original (Snippet): {description.strip()[:65]}...")
        print(f"   **Summary Phrase: {summary}**")
        print("-" * 30)

    print("--- ✅ Summarization Complete ---")

if __name__ == "__main__":
    main()