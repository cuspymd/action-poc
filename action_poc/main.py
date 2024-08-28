from action_poc.multillm import MultiLLM
from action_poc.actions import ActionsFW
from action_poc.apps import VolumeApp

if __name__ == "__main__":
    actionsFW = ActionsFW()
    multiLLM = MultiLLM(actionsFW)

    actionsFW.scan_actions(VolumeApp())

    print("assistant: 무엇을 도와드릴까요?")

    while True:
        user_query = input("user: ")
        assistant_reply = multiLLM.query(user_query)
        print(f"assistant: {assistant_reply}")