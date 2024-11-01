import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_l = st.session_state['new todo'] + '\n'
    todos.append(todo_l)
    functions.write_todos(todos)
    st.session_state['new todo'] = ''


st.title('To-Do App', )
# st.subheader('This is my first app.')
# st.write('This app is to increase your productivity.')

st.text_input(label='',
              placeholder='Add new todo...',
              on_change=add_todo,
              key='new todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
