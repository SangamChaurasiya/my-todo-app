import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    print(new_todo)
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My ToDo App")
st.subheader("This is my ToDo App.")
st.write("This app is to increase your productivity.")

todos = functions.get_todos()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:  # Performing completion of the to do based on the key selected
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter new todo...", on_change=add_todo, key="new_todo")
