import React, {useState} from 'react'

export default function UseStateHook() {

  const [nombre, setNombre] = useState('Enrique ')
  const handleClick = (e, newNombre) =>{
    setNombre(newNombre) 
    
  }  
  return (
    <div>
    <h1>Mi primer estado</h1>
    <strong>
        {nombre}
    </strong><br />
    <button onClick={handleClick}>Cambiar nombre</button> <br />
    <input type="text" placeholder='cambiat nombre' onKeyUp={e => handleClick(e, e.target.value)} />
    </div>
  )
}
