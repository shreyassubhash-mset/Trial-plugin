import streamlit as st

#set up the app title
st.title('MentalMind')

#setup a session state message variable to hold 
if 'messages' not in st.session_state:
    st.session_state.messages = []

#Display all the historical data
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

#set up credentials dictionary
creds = {
    'apikey' : 'fbdad58c-56c0-4ea5-b18a-2b0a17024040',
    'url' : 'https://us-south.ml.cloud.ibm.com'
}

#create LLM using Langchain
llm = LangChainInterface(
    credentials = creds,
    model = 'your-finetuned-model',
    params = {
        'decoding_method' : 'sample',
        'max_new_tokens' : '200',
        'temperature' : 0.5
    },
    project_id = 'your-project-id'
)

#build a prompt input template to display the prompts
prompt = st.chat_input('Pass your prompt here')

#if the user hits enter then
if prompt:
    #display the prompt     
    st.chat_message('user').markdown(prompt)
    #Store the user prompt in state
    st.session_state.messages.append({'role':'user','content':prompt})
    #send the prompt to the LLM
    response = llm(prompt)
    #show the llm response
    st.chat_message('assistant').markdown(response)
    #store the LLM response in state
    st.session_state.messages.append({'role':'assistant', 'content':response})