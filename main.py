import os
from dotenv import load_dotenv
<<<<<<< HEAD

# Set tokenizers parallelism to avoid warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"

=======
>>>>>>> fcbfb7a442b48ed5410d11dfcd9c572d9f24db3b
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
        final_answer=result.get("answer","No answer generated")
<<<<<<< HEAD
        print("\n" + "="*80)
        print("ANSWER:")
        print("="*80)
        print(final_answer)
        print("\n" + "="*80)
        print("SOURCES:")
        print("="*80)
=======
        print("\nSOURCES")
>>>>>>> fcbfb7a442b48ed5410d11dfcd9c572d9f24db3b
        citations=result.get("citations",[])
        for c in citations[:10]:
            print(" . ",c)
        print("\n" +"-" *80)
        print("BUILT BY MOBOLAJI OPEYEMI BOLATITO OBINA .CRAG SYSTEM(CORRECTIVE RETRIEVAL -AUGMENTED-GENERATION)")
        print("-"*80 + "\n")
    except Exception as e:
        print(F"Something went wrong:{e}")
        print("Try again!\n")

