import streamlit as st
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(api_key="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")

# Streamlit app title
st.title("Techy bot")

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
        model="llama-3.1-8b-instant",
    )

    # Display the response in the Streamlit app
    st.write("Response:")
    st.write(chat_completion.choices[0].message.content)
