import os
import anthropic

# Initialize the Anthropic client with Claude API
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY", "your-api-key-here")
)

def run_administrative_research(topic: str) -> str:
    """
    Automates administrative research and generates structured business summaries.
    Designed for workflow automation and operation optimization.
    """
    prompt = f"""
    You are an AI Operations Assistant. Please analyze the following topic and provide a structured operational breakdown:
    Topic: {topic}
    
    Format requirements:
    - Executive Summary (2-3 sentences)
    - 3 Key Actionable Insights
    - Recommended Process Workflow
    """
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=500,
        temperature=0.3,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.content[0].text

if __name__ == "__main__":
    sample_topic = "Automating Client Onboarding via CRM & Webhooks"
    print(f"--- Running Automated Research for: {sample_topic} ---")
    result = run_administrative_research(sample_topic)
    print(result)
