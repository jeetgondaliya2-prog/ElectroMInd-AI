import time
import streamlit as st
from rag import ask_question

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="ElectroMind AI", 
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Custom CSS (design + animations)
# -----------------------------
st.markdown("""
<style>

/* ---------- Global background ---------- */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    background-size: 400% 400%;
    animation: gradientShift 18s ease infinite;
}

@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ---------- Title ---------- */
h1 {
    color: #ffffff !important;
    text-align: center;
    animation: fadeInDown 1s ease-out;
    text-shadow: 0 0 18px rgba(0, 200, 255, 0.5);
}

.stApp > header, .stApp [data-testid="stHeader"] {
    background: transparent;
}

div[data-testid="stSubheader"], .st-emotion-cache-1v0mbdj, .stMarkdown h3 {
    color: #d0f0ff !important;
    text-align: center;
    animation: fadeInDown 1.2s ease-out;
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-25px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ---------- Intro markdown card ---------- */
.intro-card {
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    padding: 20px 25px;
    backdrop-filter: blur(6px);
    color: #eaf6ff;
    animation: fadeIn 1.4s ease-in;
    margin-bottom: 10px;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}

/* ---------- Text input ---------- */
.stTextInput input {
    background-color: rgba(255,255,255,0.08) !important;
    color: #ffffff !important;
    border: 1px solid rgba(0, 200, 255, 0.4) !important;
    border-radius: 12px !important;
    padding: 12px !important;
    transition: all 0.3s ease-in-out;
}

.stTextInput input:focus {
    border: 1px solid #00d4ff !important;
    box-shadow: 0 0 12px rgba(0, 212, 255, 0.6) !important;
}

.stTextInput input::placeholder {
    color: #9fd8ee !important;
}

/* ---------- Button ---------- */
div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    font-weight: 600;
    font-size: 16px;
    border: none;
    border-radius: 14px;
    padding: 0.7em 1.6em;
    transition: all 0.35s ease-in-out;
    box-shadow: 0 4px 15px rgba(0, 114, 255, 0.4);
}

div.stButton > button:hover {
    transform: translateY(-3px) scale(1.04);
    box-shadow: 0 8px 25px rgba(0, 198, 255, 0.7);
    background: linear-gradient(90deg, #0072ff, #00c6ff);
    cursor: pointer;
}

div.stButton > button:active {
    transform: translateY(0px) scale(0.98);
    box-shadow: 0 3px 10px rgba(0, 114, 255, 0.5);
}

/* ---------- Answer box ---------- */
.answer-box {
    background: rgba(255, 255, 255, 0.08);
    border-left: 5px solid #00d4ff;
    border-radius: 12px;
    padding: 20px 25px;
    color: #f0feff;
    animation: slideFadeIn 0.8s ease-out;
    line-height: 1.6;
    font-size: 16px;
}

@keyframes slideFadeIn {
    from { opacity: 0; transform: translateX(-15px); }
    to   { opacity: 1; transform: translateX(0); }
}

/* ---------- Source chips ---------- */
.source-chip {
    display: inline-block;
    background: rgba(0, 212, 255, 0.12);
    border: 1px solid rgba(0, 212, 255, 0.4);
    color: #d5f6ff;
    padding: 8px 14px;
    border-radius: 999px;
    margin: 5px 6px 5px 0;
    font-size: 14px;
    transition: all 0.25s ease-in-out;
    animation: fadeIn 1s ease-in;
}

.source-chip:hover {
    background: rgba(0, 212, 255, 0.3);
    transform: translateY(-2px);
}

/* ---------- Divider ---------- */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,212,255,0.6), transparent);
    margin: 25px 0;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.title("🤖 ElectroMind AI")
st.subheader("AI Troubleshooting Assistant for Software & Electronics")

st.markdown("""
<div class="intro-card">
Ask questions related to:<br><br>
💻 <b>Software Engineering</b> (Python, Git, Networking, OS, etc.)<br>
🔌 <b>Electronics & Embedded Systems</b> (Arduino, Sensors, Circuits, IoT, etc.)<br><br>
Your answers are generated using your own knowledge base (RAG).
</div>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------
# Question Input
# -----------------------------
question = st.text_input(
    "Enter your question:",
    placeholder="Example: Arduino is not detected"
)

# -----------------------------
# Ask Button
# -----------------------------
if st.button("🚀 Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        # -----------------------------
        # NEW FEATURE: Live "what the AI is doing" status trace
        # -----------------------------
        with st.status("🧠 AI is working on your question...", expanded=True) as status:

            st.write("🔍 Searching the knowledge base for relevant documents...")
            time.sleep(0.6)

            answer, docs = ask_question(question)

            st.write(f"📖 Retrieved **{len(docs)}** relevant document chunk(s) from the knowledge base.")
            time.sleep(0.4)

            st.write("🧩 Feeding retrieved context + your question into the LLM...")
            time.sleep(0.5)

            st.write("✍️ Generating a grounded answer based on the retrieved context...")
            time.sleep(0.4)

            status.update(
                label="✅ Answer generated successfully!",
                state="complete",
                expanded=False
            )

        # -----------------------------
        # Answer
        # -----------------------------
        st.success("Answer Generated")

        st.markdown("## 📌 Answer")

        st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)

        # -----------------------------
        # Sources
        # -----------------------------
        st.markdown("---")
        st.markdown("## 📚 Sources")

        sources = []

        for doc in docs:

            source = doc.metadata.get("source", "Unknown")

            filename = source.split("\\")[-1].split("/")[-1]

            if filename not in sources:
                sources.append(filename)

        chips_html = "".join(
            f'<span class="source-chip">📄 {file}</span>' for file in sources
        )
        st.markdown(chips_html, unsafe_allow_html=True)
