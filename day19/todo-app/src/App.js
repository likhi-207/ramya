import logo from './logo.svg';
import './App.css';
import List from './Components/List';
import Form from './Components/Form'; 
import { useState } from 'react';
import Counter from './Components/Counter';
import TodoApp from './TodoApp';

function App(){

  return (
    <div>
      {/* <List list={players} />
      <Form handleChange={handleChange}  /> */}
      {/* <Counter /> */}
      <TodoApp />
    </div>
  );
}

export default App;
