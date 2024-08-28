import json
from openai import OpenAI

class MultiLLM:
    def __init__(self, actionsFW):
        self.actionsFW = actionsFW
        self.messages = [
            {"role": "system", "content": "You are a helpful support assistant for TV customer. Use the supplied tools to assist the user."}
        ]
        self.client = OpenAI()

    def query(self, user_query) -> str:
        self.messages.append({"role": "user", "content": user_query})
        tools = self._get_tools()

        while True:
            if tools:
                completion = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=self.messages,
                    tools = tools 
                )
            else:
                completion = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=self.messages
                )

            self.messages.append(completion.choices[0].message)
            finish_reason = completion.choices[0].finish_reason

            if finish_reason == "tool_calls":
                self._call_actions(completion.choices[0].message.tool_calls)
                tools = []
            elif finish_reason == "stop":
                return completion.choices[0].message.content
            else:
                return f"에러 응답({finish_reason})!!"
    
    def _get_tools(self):
        actions = self.actionsFW.get_actions(self.messages)
        return [self._as_tool(action) for action in actions]
    
    def _as_tool(self, action):
        return {
            "type": "function",
            "function": action
        }
    
    def _call_actions(self, tool_calls):
        for tool_call in tool_calls:
            print(f"[debug] calling tool for {tool_call}")
            ret = self.actionsFW.execute_action(tool_call.function.name, json.loads(tool_call.function.arguments))
            print(f"[debug] tool return {ret}")

            self.messages.append({
                "role": "tool",
                "content": json.dumps(ret, ensure_ascii=False),
                "tool_call_id": tool_call.id
            })
