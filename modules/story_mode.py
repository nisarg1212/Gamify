"""Story Mode - Generate engaging narrative from a topic"""
import os
import json
import re
from dotenv import load_dotenv
from openai import OpenAI
from gamification.models import Story

# Load environment variables and configure OpenRouter
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

MODEL = "google/gemini-2.0-flash-exp:free"

def generate_story(topic: str) -> Story:
    """Generate an engaging story about a topic"""
    
    prompt = f"""You are a master storyteller. Create an engaging, educational story about: {topic}

Requirements:
- Captivating narrative (300-400 words)
- Include 5 key educational facts
- Have a clear beginning, middle, end

IMPORTANT: Return ONLY valid JSON in this exact format, nothing else:
{{"title": "Story Title", "content": "Full story text here...", "key_facts": ["fact 1", "fact 2", "fact 3", "fact 4", "fact 5"]}}"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Check if response is valid
        if not response or not response.choices:
            raise ValueError("Empty response from API")
        
        text = response.choices[0].message.content
        if not text:
            raise ValueError("Empty content in response")
        
        text = text.strip()
        
        # Remove markdown code blocks if present
        if text.startswith("```"):
            text = re.sub(r'^```json?\s*\n?', '', text)
            text = re.sub(r'\n?```\s*$', '', text)
        
        # Try to find JSON in the response
        json_match = re.search(r'\{[\s\S]*\}', text)
        if json_match:
            text = json_match.group()
        
        data = json.loads(text)
        
        # Validate required fields
        title = data.get("title", f"Learning About {topic}")
        content = data.get("content", "")
        key_facts = data.get("key_facts", [])
        
        if not content:
            raise ValueError("No content in generated story")
        
        if not key_facts or len(key_facts) < 3:
            key_facts = [
                f"{topic} is a fascinating subject",
                f"There are many aspects to {topic}",
                f"Understanding {topic} opens new perspectives",
                f"{topic} has real-world applications",
                f"Learning about {topic} is rewarding"
            ]
        
        return Story(
            topic=topic,
            title=title,
            content=content,
            key_facts=key_facts[:5],
            xp_reward=15
        )
    except json.JSONDecodeError as e:
        print(f"[STORY JSON ERROR] {e}")
        # Create a simple story if JSON parsing fails
        return Story(
            topic=topic,
            title=f"Discovering {topic}",
            content=f"""Let's explore the fascinating world of {topic}!

{topic} is a subject that has captivated people for generations. It encompasses many interesting aspects that are worth understanding.

When we study {topic}, we discover new perspectives and gain valuable knowledge. The concepts within {topic} connect to many areas of our lives.

By learning about {topic}, you open doors to deeper understanding. Whether you're a beginner or already familiar with the subject, there's always more to discover.

Take your time to explore {topic}. Ask questions, seek answers, and enjoy the journey of learning!""",
            key_facts=[
                f"{topic} is a rich and diverse subject",
                f"Many experts have studied {topic}",
                f"{topic} connects to real-world applications",
                f"Understanding {topic} requires exploration",
                f"Learning {topic} is a rewarding journey"
            ],
            xp_reward=10
        )
    except Exception as e:
        print(f"[STORY ERROR] {type(e).__name__}: {e}")
        return Story(
            topic=topic,
            title=f"The World of {topic}",
            content=f"""Welcome to learning about {topic}!

While we prepare a more detailed story for you, let's start with the basics. {topic} is an interesting subject with many dimensions to explore.

Think about what you already know about {topic}. What questions do you have? What would you like to learn more about?

As you continue through this learning adventure, you'll test your knowledge and deepen your understanding. Let's get started!""",
            key_facts=[
                f"{topic} is worth learning about",
                f"Questions help us understand {topic} better",
                f"Practice helps master {topic}",
                f"{topic} has many interesting aspects",
                f"Keep exploring {topic}!"
            ],
            xp_reward=5
        )
