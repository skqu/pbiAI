from ollama import chat
import argparse
import json
import os


class Agent:

    def __init__(self):
        self.memory = []
        self.memory = load_memory()
        self.systemprompt = """
            You are an IT Architecture teaching assistant.

            Rules:
            - Be concise.
            - Maximum 100 words.
            - Use bullet points when appropriate.
            - Focus on software and IT architecture.
            """

    def ask(self, question: str, filename: str) -> str:
        architecture = get_arch()
        content = read_file(filename)
        userPrompt = {
                    "role": "user",
                    "content": f"""
                        Architecture:
                        {architecture}
                        Code:
                        {content}
                        Question:
                        {question}
                        """
                    }
        response = chat(
            model="gemma4:e2b",
            messages=[
                {
                    "role": "system",
                    "content": self.systemprompt
                },
                *self.memory,
                userPrompt
            ]
        )
        self.memory.append(
            {
                "role": "user", 
                "content": f"""
                Quistion: {question} 

                File: {filename}"""
            }
        )
        self.memory.append(
            {
                "role": "assistant",
                "content": response["message"]["content"]
            }
        )
        save_memory(self.memory)
        return response["message"]["content"]

# TOOLS

# Tool 0 Read a file -> Used for other tools
def read_file(path):
    with open(path, "r") as f:
        return f.read()


# Tool 1 Read a file -> Architecture documentation
def get_arch():
    return read_file("toolContext/architecture.md")

# Tool 2 Read requirement -> the requirement we set for the system
def load_memory():
    if not os.path.exists("memory/memory.json"):
        return []
    with open("memory/memory.json", "r") as f:
        return json.load(f)

def save_memory(memory):
    with open("memory/memory.json", "w") as f:
        json.dump(memory, f, indent=2)

def main():
    parser = argparse.ArgumentParser()
    agent = Agent()

    parser.add_argument(
        "-p",
        "--prompt",
        required=True,
        help="Prompt to send to agent"
        )

    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="File to include"
        )

    args = parser.parse_args()

    answer = agent.ask(
        args.prompt,
        args.file
        )

    print(answer)

if __name__ == "__main__":
    main()