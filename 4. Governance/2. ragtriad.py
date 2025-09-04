from langchain_ibm import ChatWatsonx
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
import os 
from dotenv import load_dotenv

from ibm_watsonx_gov.entities.state import EvaluationState
from ibm_watsonx_gov.evaluators.agentic_evaluator import AgenticEvaluator
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import START, END, StateGraph
import uuid
import json 

from langchain_ibm import ChatWatsonx, WatsonxEmbeddings

from langchain_chroma import Chroma
from colorama import Fore 
import uuid

# RAG Triad: https://myscale.com/blog/ultimate-guide-to-evaluate-rag-system/

load_dotenv()

embeddings = WatsonxEmbeddings(
    model_id="sentence-transformers/all-minilm-l6-v2",
    project_id=os.getenv("WATSONX_PROJECT_ID"),
)

vector_store = Chroma(
    collection_name="credit_card",
    persist_directory="./credit_card",
    embedding_function=embeddings,
)

llm = ChatWatsonx(
    model_id="ibm/granite-3-2b-instruct",
    url=os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com"),
    apikey=os.getenv("WATSONX_APIKEY"),
    project_id=os.getenv("WATSONX_PROJECT_ID"),
    params={
        "decoding_method": "greedy",
        "temperature": 0,
        "min_new_tokens": 5,
        "max_new_tokens": 250,
        "stop_sequences": ["Human:", "Observation:"],
})

class AppState(EvaluationState):
    pass

evaluator = AgenticEvaluator()
@evaluator.evaluate_context_relevance()
def retrieval_node(state: AppState):
    similarity_threshold_retriever = vector_store.as_retriever(search_type="similarity_score_threshold",search_kwargs={"k": 3,"score_threshold": 0.1})
    context = similarity_threshold_retriever.invoke(state.input_text)
    return {
        "context": [doc.page_content for doc in context]
    }

@evaluator.evaluate_faithfulness()
@evaluator.evaluate_answer_relevance()
def generate_node(state: AppState):
    generate_prompt = ChatPromptTemplate.from_template(
        "Answer the following question based on the given context:\n"
        "Context: {context}\n"
        "Question: {input_text}\n"
        "Answer:"
    )

    formatted_prompt = generate_prompt.invoke(
        {"input_text": state.input_text, "context": "\n".join(state.context)})

    result = llm.invoke(formatted_prompt)
    return {
        "generated_text": result.content
    }

graph = StateGraph(AppState)

# Add nodes
graph.add_node("Retrieval \nNode", retrieval_node)
graph.add_node("Generation \nNode", generate_node)

# Add edges
graph.add_edge(START, "Retrieval \nNode")
graph.add_edge("Retrieval \nNode", "Generation \nNode")
graph.add_edge("Generation \nNode", END)

# Compile the graph
rag_app = graph.compile()

rag_app.get_graph().draw_mermaid_png(output_file_path="rag_graph.png")

config = {"configurable": {"thread_id": "abc123"}}
# Output assistant results
def stream_graph_updates(user_input: str):
    for event in rag_app.stream({"input_text":user_input, "interaction_id":str(uuid.uuid1())}, config):
        for value in event.values():
            for key, value in value.items(): 
                if key == 'context': 
                    print("Context: " + Fore.LIGHTCYAN_EX  + f" {value}) \n" + Fore.RESET)
                else: 
                    print("Agent: " + Fore.LIGHTMAGENTA_EX  + f" {value}) \n" + Fore.RESET)


while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    
    evaluator.start_run()
    stream_graph_updates(user_input)
    evaluator.end_run()