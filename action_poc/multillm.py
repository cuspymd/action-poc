from openai import OpenAI

class MultiLLM:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": "You are a helpful support assistant for TV customer. Use the supplied tools to assist the user."}
        ]
        self.client = OpenAI()

    def query(self, user_query) -> str:
        user_message = {"role": "user", "content": user_query}
        self.messages.append(user_message)

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.messages
        )

        self.messages.append(completion.choices[0].message)
        return completion.choices[0].message.content

