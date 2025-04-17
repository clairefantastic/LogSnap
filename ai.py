import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(log_lines):
    content = "\n".join(log_lines[-100:])  # last 100 lines
    prompt = f"""
You are a helpful Linux system assistant. Summarize the following system logs in one concise sentence.

Logs:
{content}

Summary:
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=60
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ GPT summary failed: {e}"
