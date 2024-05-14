import streamlit as st
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(api_key="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")

# Streamlit app title
st.title("Groq Chatbot")

# Input text from the user
prompt = st.text_input("Kya Jaana Hai:")

# If the user has entered a prompt
if prompt:
    # Generate chat completion using the Groq client
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    # Display the response in the Streamlit app
    st.write("Response:")
    st.write(chat_completion.choices[0].message.content)
