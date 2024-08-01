import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo and todo not in [t.strip() for t in todos]:
        todo += "\n"
        todos.append(todo)
        functions.write_todos(todos)
        st.toast(f"Todo '{todo.strip()}' added!", icon="✅")
    elif todo in [t.strip() for t in todos]:
        st.toast(f"Todo '{todo.strip()}' already exist!", icon="⚠️")
    else:
        st.error("Todo cannot be empty!")
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter todo", label_visibility="hidden", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
