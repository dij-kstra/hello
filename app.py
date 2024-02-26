import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="Love Notes", page_icon="💖")

# Define the function to initialize session state
def init_session_state():
    return {
        "answers": "",
        "image": None
    }

# Define the main function
def main():
    # Initialize session state
    session_state = st.session_state.get("session_state", init_session_state())

    # Define the sidebar content
    sidebar_text = """
    ## Love Notes 💖 💖 
    Here's a thought from Sadhguru:
    "Love is not an instrument of convenience. It is a process of self-annihilation."
    """

    # Render the sidebar
    st.sidebar.markdown(sidebar_text)

    # Display a beautiful thought
    st.title("Love Notes 💖 💖")
    st.write("Welcome to Love Notes! Share your thoughts and feelings with each other.")

    # Text area for writing answers and notes
    answers = st.text_area("Write your thoughts here", session_state["answers"])
    session_state["answers"] = answers  # Update session state

    # Upload image
    st.subheader("Upload a photo to share")
    image = st.file_uploader("Choose a photo", type=["jpg", "jpeg", "png"])
    if image is not None:
        session_state["image"] = image  # Update session state

    # Display the shared answers and image
    st.write("Shared Thoughts:")
    st.write(session_state["answers"])
    if session_state["image"] is not None:
        st.image(session_state["image"], caption="Shared Photo")

    # Define the quiz questions
    questions = [
        "What is my favorite color?",
        "What is my go-to comfort food?",
        "Which movie can I watch over and over again without getting tired of it?",
        "What is my favorite season of the year?",
        "What is my favorite genre of music?",
        "What is my zodiac sign?",
        "What is my preferred type of dessert?",
        "What is the name of my childhood best friend?",
        "What is my favorite holiday?",
        "What is my dream vacation destination?",
        "What is my most cherished childhood memory and why does it hold such significance for me?",
        "Which life lesson or piece of advice from a family member or mentor has had the biggest impact on me, and how has it shaped my outlook on life?",
        "Describe a moment when I felt truly vulnerable or afraid, and how did I overcome it?",
        "What is my greatest fear, and how does it influence my actions or decisions?",
        "Share an experience where I felt deeply loved and supported by someone, and why did it leave a lasting impression on me?",
        "Reflecting on a difficult time in my life, what coping mechanism or support system did I find most helpful?",
        "Describe a personal goal or dream that I've shared with you, and why it means so much to me.",
        "What is my favorite way to unwind or de-stress when I'm feeling overwhelmed or anxious?",
        "Share a moment when I felt proud of myself or accomplished, and why did it mean so much to me?",
        "Describe a time when I experienced a setback or failure, and how did I handle it emotionally?"
    ]

    # Display the quiz questions and input fields for answers
    st.subheader("Love Notes Quiz")
    st.write("Answer the following questions to see how well you know each other.")
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(f"Question {i+1}: {question}")
        answers[question] = st.text_input("Your Answer:", key=question)

    # Display the answers as they are typed
    st.subheader("Your Answers:")
    for question, answer in answers.items():
        st.write(f"- **{question}:** {answer}")

# Run the app
if __name__ == "__main__":
    main()
