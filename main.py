from agent import run_agent


print("================================")
print("        AUREVIX AI")
print("  Autonomous Task Assistant")
print("================================")

while True:

    command = input("\nYou: ")

    if command.lower() == "exit":
        print("AUREVIX: Goodbye! 👋")
        break

    result = run_agent(command)

    print("AUREVIX:", result)