"""
LangChain Installation Diagnostic Script
Run this to see what's available in your installation
"""

print("="*60)
print("LANGCHAIN DIAGNOSTIC TOOL")
print("="*60)

# Check if langchain is installed
try:
    import langchain
    print(f"\n✓ langchain installed: version {langchain.__version__}")
except ImportError as e:
    print(f"\n✗ langchain not installed: {e}")
    exit()

# Check langchain.agents module
print("\n" + "-"*60)
print("Available in langchain.agents:")
print("-"*60)
try:
    import langchain.agents
    agents_attrs = dir(langchain.agents)
    
    # Filter out private attributes
    public_attrs = [attr for attr in agents_attrs if not attr.startswith('_')]
    
    for attr in sorted(public_attrs):
        print(f"  - {attr}")
    
    # Check specifically for what we need
    print("\n" + "-"*60)
    print("Checking for required components:")
    print("-"*60)
    
    required = [
        'AgentExecutor',
        'create_tool_calling_agent',
        'create_react_agent',
        'create_openai_tools_agent',
        'create_openai_functions_agent'
    ]
    
    for item in required:
        if item in agents_attrs:
            print(f"  ✓ {item} - FOUND")
        else:
            print(f"  ✗ {item} - NOT FOUND")
            
except Exception as e:
    print(f"Error accessing langchain.agents: {e}")

# Check other important modules
print("\n" + "-"*60)
print("Checking other LangChain packages:")
print("-"*60)

packages = [
    'langchain_core',
    'langchain_community', 
    'langchain_google_genai',
    'langgraph'
]

for package in packages:
    try:
        mod = __import__(package)
        version = getattr(mod, '__version__', 'unknown')
        print(f"  ✓ {package}: version {version}")
    except ImportError:
        print(f"  ✗ {package}: NOT INSTALLED")

# Recommendation
print("\n" + "="*60)
print("RECOMMENDATIONS:")
print("="*60)

try:
    import langchain.agents
    if 'AgentExecutor' not in dir(langchain.agents):
        print("""
Your langchain installation is outdated or incomplete.

RUN THESE COMMANDS:
1. pip uninstall langchain langchain-core langchain-community -y
2. pip install langchain langchain-core langchain-community
3. pip install langgraph langchain-google-genai

OR use the LangGraph version of the code (recommended).
        """)
    else:
        print("\n✓ Your installation looks good!")
        print("  You can use the standard LangChain agent code.")
except:
    print("\nCritical error with langchain.agents module.")
    print("Reinstall LangChain packages.")

print("="*60)