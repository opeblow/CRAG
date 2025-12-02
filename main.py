import os
from dotenv import load_dotenv
load_dotenv()
from app.agent import app
from app.models import AgentState

print("\nCRAG IS ALIVE")
print("Built by MOBOLAJI OPEYEMI BOLATITO,Corrective RAG with local PDFs + Brave Search fallback\n")
print("Type 'quit','exit',or 'bye' to stop\n")

while True:
    question=input("Ask me anything:")
    if question.lower() in {"quit","exit","bye",""}:
        print("\nSee you later")
        break
    if not question:
        continue
    print("\nThinking....",end="\n\n")

    try:
        result=app.invoke({"question":question})
        print("ANSWER")
        print(result["answer"])
        print("\nSOURCES")
        for c in result.get("citations",[])[:10]:
            print(" . ",c)
        print("\n" + "-" * 80 + "\n")
    except Exception as e:
        print(f"Something went wrong:{e}")
        print("Try again!\n")
