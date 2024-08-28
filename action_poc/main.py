from action_poc.multillm import MultiLLM

if __name__ == "__main__":
    multiLLM = MultiLLM()
    print("assistant: 무엇을 도와드릴까요?")

    while True:
        user_query = input("user: ")
        assistant_reply = multiLLM.query(user_query)
        print(f"assistant: {assistant_reply}")