from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
