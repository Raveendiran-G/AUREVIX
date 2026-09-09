from tools import create_file


def run_agent(command):

    command = command.lower()

    if "create a file" in command:

        print("🧠 AUREVIX understood the task.")

        # Example:
        filename = "hello.py"

        content = """print("Hello World")"""

        result = create_file(filename, content)

        return result

    else:
        return "❌ AUREVIX doesn't know how to perform this task yet."