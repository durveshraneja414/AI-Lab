def evaluate_performance(punctuality, task_completion, peer_feedback, manager_feedback, innovation):
    score = 0

   
    if punctuality >= 8:
        score += 2
    elif punctuality >= 5:
        score += 1

    if task_completion >= 8:
        score += 3
    elif task_completion >= 5:
        score += 1

    if peer_feedback >= 8:
        score += 2
    elif peer_feedback >= 5:
        score += 1

    if manager_feedback >= 8:
        score += 4
    elif manager_feedback >= 5:
        score += 2

    if innovation >= 7:
        score += 2
    elif innovation >= 4:
        score += 1


    if score >= 10:
        return "Excellent"
    elif score >= 7:
        return "Good"
    elif score >= 4:
        return "Average"
    else:
        return "Needs Improvement"


def get_input(prompt):
    while True:
        try:
            value = int(input(prompt + " (1 to 10): "))
            if 1 <= value <= 10:
                return value
            else:
                print("  Please enter a number between 1 and 10.")
        except ValueError:
            print(" Invalid input. Please enter a number.")



print("==== Employee Performance Evaluation System ====")
punctuality = get_input("Enter Punctuality rating")
task_completion = get_input("Enter Task Completion rating")
peer_feedback = get_input("Enter Peer Feedback rating")
manager_feedback = get_input("Enter Manager Feedback rating")
innovation = get_input("Enter Innovation rating")


result = evaluate_performance(
    punctuality,
    task_completion,
    peer_feedback,
    manager_feedback,
    innovation
)

print("\n Employee Performance Rating:", result)
