from langchain_community.llms import Ollama

llm = Ollama(model="tinyllama")

response = llm.invoke("Why does a Kubernetes pod go into CrashLoopBackOff?")
print(response)