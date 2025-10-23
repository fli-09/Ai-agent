from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


@tool
def search_tool(query: str) -> str:
    """
    Search the web for current, real-time information using DuckDuckGo.
    
    Use this tool when you need:
    - Recent news or events
    - Current statistics or data
    - Up-to-date information
    - Real-time facts
    
    Args:
        query: The search query string to look up on the web
        
    Returns:
        str: Search results from DuckDuckGo
    """
    try:
        search = DuckDuckGoSearchRun()
        results = search.run(query)
        return f"Search results for '{query}':\n{results}"
    except Exception as e:
        return f"Error performing search: {str(e)}"


@tool
def wiki_tool(query: str) -> str:
    """
    Search Wikipedia for encyclopedic information and well-established facts.
    
    Use this tool when you need:
    - Historical information
    - Scientific concepts and definitions
    - Biographical information
    - Well-documented facts
    - Academic or encyclopedic knowledge
    
    Args:
        query: The topic to search on Wikipedia
        
    Returns:
        str: Wikipedia article summary
    """
    try:
        api_wrapper = WikipediaAPIWrapper(
            top_k_results=1, 
            doc_content_chars_max=3000
        )
        wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
        results = wiki.run(query)
        return f"Wikipedia information on '{query}':\n{results}"
    except Exception as e:
        return f"Error querying Wikipedia: {str(e)}"


@tool
def save_tool(content: str, filename: str = "research_output.txt") -> str:
    """
    Save research content to a text file.
    
    Use this tool when you need to:
    - Save the final research paper
    - Store findings for later reference
    - Create a document from your research
    
    Args:
        content: The research content to save
        filename: The name of the file to save to (default: research_output.txt)
        
    Returns:
        str: Success or error message
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✓ Research successfully saved to '{filename}'"
    except Exception as e:
        return f"✗ Error saving file: {str(e)}"