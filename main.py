import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import MessagesState, StateGraph, START
from langgraph.prebuilt import tools_condition, ToolNode
from tools import search_tool, wiki_tool, save_tool

# Load environment variables
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    print("Error: GOOGLE_API_KEY not found. Make sure it's set in your .env file.")
    exit()

# Initialize the language model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    google_api_key=google_api_key,
    temperature=0.2
)

# Define tools list
tools = [search_tool, wiki_tool, save_tool]

# Bind tools to the language model
llm_with_tools = llm.bind_tools(tools)

# System message to guide the assistant
sys_msg = SystemMessage(
    content="""You are a research assistant that helps generate comprehensive research papers.
    
Your task is to:
1. Use the search_tool to find current, real-time information on the web
2. Use the wiki_tool to get encyclopedic knowledge and well-established facts
3. Gather information from multiple sources
4. Synthesize the information into a comprehensive summary
5. Always cite your sources properly
6. Use the save_tool to save your final research if requested

Be thorough, accurate, and provide detailed responses with proper citations."""
)

# Define the assistant node
def assistant(state: MessagesState):
    """
    The assistant node that processes messages and decides whether to use tools.
    """
    return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# Build the ReAct graph
builder = StateGraph(MessagesState)

# Add nodes
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# Add edges
builder.add_edge(START, "assistant")

# Add conditional edge from assistant
# If assistant wants to use a tool -> goes to "tools"
# If assistant has final answer -> goes to END
builder.add_conditional_edges(
    "assistant",
    tools_condition,
)

# Add edge from tools back to assistant (creates the feedback loop)
builder.add_edge("tools", "assistant")

# Compile the graph
react_graph = builder.compile()

# Main execution
if __name__ == "__main__":
    print("="*60)
    print("RESEARCH ASSISTANT - ReAct Agent")
    print("="*60)
    
    query = input("\nWhat can I help you research? ")
    
    print("\n" + "="*60)
    print("AGENT WORKING...")
    print("="*60 + "\n")
    
    try:
        # Create the initial message
        messages = [HumanMessage(content=query)]
        
        # Invoke the graph
        result = react_graph.invoke({"messages": messages})
        
        # Display all messages in the conversation
        print("\n" + "="*60)
        print("CONVERSATION FLOW:")
        print("="*60 + "\n")
        
        for m in result['messages']:
            m.pretty_print()
            print()
        
        # Extract final answer
        final_message = result['messages'][-1]
        
        print("="*60)
        print("FINAL ANSWER:")
        print("="*60)
        print(final_message.content)
        print("="*60)
        
    except Exception as e:
        print(f"\n Error running agent: {e}")
        import traceback
        traceback.print_exc()
