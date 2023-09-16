import React, { useState, useEffect } from "react";
import TodoForm from "./todo-form";
import Todo from "./todo";
import axios from 'axios';

export default function ListaDeTareas() {
  const [todos, setTodos] = useState([]);

  // Cargar tareas desde la API al iniciar el componente
  useEffect(() => {
    fetchTarea();
  }, []);

  const fetchTarea = async () => {
    try {
      const response = await axios.get('/api/tarea/');
      setTodos(response.data);
    } catch (error) {
      console.error('Error al obtener las tareas:', error);
    }
  };

  const onMarkComplete = async (id) => {
    try {
      await axios.put(`/api/Tarea/${id}/`, { completed: true });
      setTodos((prevTodos) =>
        prevTodos.map((todo) =>
          todo.id === id ? { ...todo, completed: true } : todo
        )
      );
    } catch (error) {
      console.error(`Error al marcar como completada la tarea con ID ${id}:`, error);
    }
  };

  const addTodo = async (newTodo) => {
    try {
      const response = await axios.post('/api/Tarea/', { tarea: newTodo, completed: false });
      setTodos([...todos, response.data]);
    } catch (error) {
      console.error('Error al agregar una tarea:', error);
    }
  };

  const onDeleteItem = async (id) => {
    try {
      await axios.delete(`/api/Tarea/${id}/`);
      setTodos((prevTodos) => prevTodos.filter((item) => item.id !== id));
    } catch (error) {
      console.error(`Error al eliminar la tarea con ID ${id}:`, error);
    }
  };

  const onEditTask = async (id, updatedTask) => {
    try {
      const response = await axios.put(`/api/Tareas/${id}/`, { tarea: updatedTask });
      setTodos((prevTodos) =>
        prevTodos.map((todo) =>
          todo.id === id ? { ...todo, tarea: response.data.tarea } : todo
        )
      );
    } catch (error) {
      console.error(`Error al editar la tarea con ID ${id}:`, error);
    }
  };

  return (
    <div className="container">
      <TodoForm addTodo={addTodo} />
      <Todo
        todos={todos}
        onMarkComplete={onMarkComplete}
        onDeleteItem={onDeleteItem}
        onEditTask={onEditTask}
      />
    </div>
  );
}
