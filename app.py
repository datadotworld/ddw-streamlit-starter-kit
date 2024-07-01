import requests
import streamlit as st


# Function to send a question to the API and get the response
def ask_question(orgid: str, projectid: str, question: str):
    endpoint = st.secrets["ddw"]["api_endpoint"]
    url = endpoint + f"/v0/aice/{orgid}/{projectid}/answerTool"
    payload = {"question": question}

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + st.secrets["ddw"]["token"],
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        err_msg = f"Failed to get response from API: {response.status_code}"
        return {"error": err_msg}


# Streamlit App
def main():
    st.title("Question Answering with data.world's AI Context Engine")

    st.write("Ask a question about structured data and get an answer.")

    orgid = st.text_input("Enter your organization ID:")
    projectid = st.text_input("Enter your project ID:")
    question = st.text_input("Enter your question:")

    if st.button("Get Answer"):
        if question:
            with st.spinner("Asking the API..."):
                result = ask_question(orgid, projectid, question)
                st.write("## Answer")
                if "answer" in result:
                    st.write(result["answer"])
                else:
                    st.write(result.get("error", "No answer returned"))
        else:
            st.warning("Please enter a question")


if __name__ == "__main__":
    main()
