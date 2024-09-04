# 🐍 Python Code: Welcome to the GloProg Family! 🎉

# Importing necessary libraries
import time

# Function to display a welcome message
def welcome_message():
    print("🌟 Welcome to the GloProg GitHub Learning Session! 🌟")
    time.sleep(1)  # Adding a delay for effect
    print("🚀 Let's dive into Python programming and have some fun! 🚀")

# Function to print a list of tasks
def print_tasks(tasks):
    print("\n🔍 **Today's Tasks:**\n")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

# Main execution
if __name__ == "__main__":
    welcome_message()  # Display the welcome message

    # List of tasks for the day
    tasks = [
        "Learn Python basics",
        "Practice Git commands",
        "Explore Markdown",
        "Create a sample project"
    ]

    print_tasks(tasks)  # Print the list of tasks

    # Final message
    print("\n🎯 Keep up the great work and happy coding! 🎯"
