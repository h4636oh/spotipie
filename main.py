from process_command import process_command
from process_input import process_input

while True:
    commandNaturalLanguage = input("Enter command: ")
    processedCommand = process_input(commandNaturalLanguage)
    print(processedCommand)
    if processedCommand == "exit":
        break
    process_command(processedCommand)