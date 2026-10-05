import re


def extract_requirements(question):
    """
    Extract important requirement words from the question.
    """

    keywords = [
        "definition",
        "introduction",
        "meaning",
        "applications",
        "application",
        "advantages",
        "disadvantages",
        "features",
        "types",
        "examples",
        "importance",
        "uses",
        "working",
        "process",
        "steps",
        "conclusion",
        "references"
    ]

    found_requirements = []

    question = question.lower()

    for keyword in keywords:
        if keyword in question:
            if keyword not in found_requirements:
                found_requirements.append(keyword)

    return found_requirements


def check_answer(requirements, answer):
    """
    Check whether each requirement is present in the answer.
    """

    answer = answer.lower()

    results = {}

    for requirement in requirements:

        # Convert plural words into a simple search form
        if requirement.endswith("s"):
            search_word = requirement[:-1]
        else:
            search_word = requirement

        if search_word in answer or requirement in answer:
            results[requirement] = True
        else:
            results[requirement] = False

    return results


def display_result(results):

    print("\n======================================")
    print("       ASSIGNMENT CHECKING RESULT")
    print("======================================")

    total = len(results)
    completed = 0

    print("\nRequirement Status:\n")

    for requirement, status in results.items():

        if status:
            print(f"✓ {requirement.title()} - Present")
            completed += 1
        else:
            print(f"✗ {requirement.title()} - Missing")

    missing = total - completed

    print("\n--------------------------------------")
    print(f"Total Requirements : {total}")
    print(f"Completed          : {completed}")
    print(f"Missing            : {missing}")

    if total > 0:
        percentage = (completed / total) * 100
        print(f"Completion         : {percentage:.2f}%")

    print("--------------------------------------")

    if missing == 0:
        print("🎉 All requirements are satisfied!")
    else:
        print("⚠️ Please add the missing requirements.")

    print("======================================")


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

print("======================================")
print("   ASSIGNMENT REQUIREMENTS CHECKER")
print("======================================")

print("\nEnter your assignment question:")
question = input("> ")

print("\nEnter your assignment answer:")
answer = input("> ")

# Extract requirements from question
requirements = extract_requirements(question)

# Check answer
results = check_answer(requirements, answer)

# Display result
display_result(results)