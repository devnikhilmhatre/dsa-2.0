from typing import TypedDict
from langgraph.graph import StateGraph


class Memory(TypedDict):
    message: str
    val: bool


def greeting_node(state: Memory) -> Memory:
    """add greeting message to node"""
    state.update({"message": f"Hi, {state['message']}"})
    return state


def greeting_node2(state: Memory) -> Memory:
    """add greeting message to node"""
    state.update({"message": f"Hello, {state['message']}"})
    return state


def check_val_node(state: Memory) -> str:
    """check if the value is true"""
    if state["val"]:
        return "true"
    else:
        return "false"


graph = StateGraph(Memory)

graph.add_node("greeting", greeting_node)
graph.add_node("greeting2", greeting_node2)
graph.add_node("check_val", lambda state: state)

graph.add_conditional_edges(
    "check_val",
    check_val_node,
    {
        "true": "greeting",
        "false": "greeting2",
    },
)

graph.set_entry_point("check_val")
graph.set_finish_point("greeting2")
graph.set_finish_point("greeting")

app = graph.compile()

response = app.invoke({"message": "John", "val": False})
print(response)
