# chatbot_app/api.py

from ninja_extra import NinjaExtraAPI
from django.http import StreamingHttpResponse
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from django.conf import settings
from langchain.callbacks.base import BaseCallbackHandler
from queue import Queue
from threading import Thread

api = NinjaExtraAPI()

@api.get("/chat")
def chat(request, message: str):
    llm = ChatOpenAI(
        temperature=0.7,
        streaming=True,
        openai_api_key=settings.OPENAI_API_KEY
    )

    queue = Queue()

    class MyCallbackHandler(BaseCallbackHandler):
        def __init__(self, queue):
            self.queue = queue

        def on_llm_new_token(self, token: str, **kwargs):
            self.queue.put(token)

        def on_llm_end(self, response, **kwargs):
            self.queue.put('[END]')

    handler = MyCallbackHandler(queue)

    def event_stream():
        messages = [HumanMessage(content=message)]
        # Start the LLM call in a background thread
        def run_llm():
            llm(messages, callbacks=[handler])
        thread = Thread(target=run_llm)
        thread.start()
        while True:
            token = queue.get()
            if token == '[END]':
                yield f"data: [END]\n\n"
                break
            yield f"data: {token}\n\n"

    return StreamingHttpResponse(
        event_stream(),
        content_type='text/event-stream'
    )
