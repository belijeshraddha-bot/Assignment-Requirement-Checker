import streamlit as st


# -----------------------------------------
# Find requirements from the question
# -----------------------------------------
def extract_requirements(question):

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

    question = question.lower()

    requirements = []

    for keyword in keywords:
        if keyword in question and keyword not in requirements:
            requirements.append(keyword)

    return requirements


# -----------------------------------------
# Check requirements in the answer
# -----------------------------------------
def check_answer(requirements, answer):

    answer = answer.lower()

    results = {}

    for requirement in requirements:

        # Handle plural words
        if requirement.endswith("s"):
            simple_word = requirement[:-1]
        else:
            simple_word = requirement

        if requirement in answer or simple_word in answer:
            results[requirement] = True
        else:
            results[requirement] = False

    return results


# -----------------------------------------
# Streamlit page
# -----------------------------------------

st.set_page_config(
    page_title="Assignment Requirements Checker",
    page_icon="📝"
)

st.title("📝 Assignment Requirements Checker")

st.write(
    "Enter your assignment question and answer. "
    "The system will identify the requirements that are "
    "present and missing."
)

st.divider()


# -----------------------------------------
# Question
# -----------------------------------------

st.subheader("1️⃣ Assignment Question")

question = st.text_area(
    "Enter your assignment question:",
    height=150,
    placeholder="Example: Explain Artificial Intelligence including definition, applications, advantages, disadvantages and conclusion."
)


# -----------------------------------------
# Answer
# -----------------------------------------

st.subheader("2️⃣ Assignment Answer")

answer = st.text_area(
    "Enter your assignment answer:",
    height=250,
    placeholder="Enter or paste your assignment answer here..."
)


# -----------------------------------------
# Check button
# -----------------------------------------

if st.button("🔍 Check Assignment", use_container_width=True):

    if not question.strip():

        st.warning("⚠️ Please enter the assignment question.")

    elif not answer.strip():

        st.warning("⚠️ Please enter your assignment answer.")

    else:

        # Find requirements
        requirements = extract_requirements(question)

        if not requirements:

            st.info(
                "No predefined requirements were detected "
                "from the question."
            )

        else:

            # Check answer
            results = check_answer(
                requirements,
                answer
            )

            total = len(results)

            completed = sum(results.values())

            missing = total - completed

            percentage = (completed / total) * 100


            # -----------------------------------------
            # Results
            # -----------------------------------------

            st.divider()

            st.subheader("📊 Assignment Result")


            # Score
            st.metric(
                "Completion Score",
                f"{percentage:.0f}%"
            )


            col1, col2, col3 = st.columns(3)

            with col1:
                st.success(
                    f"✅ Present: {completed}"
                )

            with col2:
                st.error(
                    f"❌ Missing: {missing}"
                )

            with col3:
                st.info(
                    f"📋 Total: {total}"
                )


            st.divider()

            st.subheader("📋 Requirement Status")


            # Show each requirement
            for requirement, status in results.items():

                if status:

                    st.success(
                        f"✅ {requirement.title()} — Present"
                    )

                else:

                    st.error(
                        f"❌ {requirement.title()} — Missing"
                    )


            st.divider()


            # -----------------------------------------
            # Final message
            # -----------------------------------------

            if missing == 0:

                st.balloons()

                st.success(
                    "🎉 Excellent! All assignment requirements "
                    "are satisfied."
                )

            else:

                st.warning(
                    "⚠️ Your answer is missing some requirements. "
                    "Please add the missing sections."
                )