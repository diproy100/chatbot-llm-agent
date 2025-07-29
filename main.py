import warnings
warnings.filterwarnings('ignore')

from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, Tool, AgentType
from tools.calculator import calculate

# Set up LLM
llm = Ollama(model="llama3")

# Define the calculator tool
calculator_tool = Tool(
    name="Calculator",
    func=calculate,
    description="Useful for simple math calculations. Input should be a valid arithmetic expression (e.g., 2 + 2 * 3)."
)

# Initialize agent with tool
agent = initialize_agent(
    tools=[calculator_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

def main():
    print("Welcome to the Agentic Chatbot! Type 'quit' to exit.")
    while True:
        query = input("You: ")
        if query.lower() == "quit":
            break
        response = agent.run(query)
        print("Bot:", response)

if __name__ == "__main__":
    main()
