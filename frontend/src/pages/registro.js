import React from 'react';
import ReactDOM from 'react-dom';
import { Formik, Field, Form } from 'formik';
import Link from 'next/link';
import "../../styles/registro.css";


const Registro = () => (
  <>
    <div>
      <h1>REGISTRATE</h1>
      <Formik
        initialValues={{
          firstName: '',
          lastName: '',
          email: '',
        }}
        onSubmit={async (values) => {
          await new Promise((r) => setTimeout(r, 500));
          alert(JSON.stringify(values, null, 2));
        }}
      >
      <Form className='form'>
        <label htmlFor="firstName">NOMBRE</label> <br/>
        <Field id="firstName" name="firstName" placeholder="Nombre" /><br/>
        <label htmlFor="lastName">APELLIDO</label><br/>
        <Field id="lastName" name="lastName" placeholder="Apellido" /><br/>
        <label htmlFor="contraseña">CONTRASEÑA</label><br/>
        <Field id="contraseña" name="contraseña" placeholder="Contraseña" type="number" maxlength="8" /><br/>
        <label htmlFor="email">Email</label><br/>
        <Field
          id="email"
          name="email"
          placeholder="jane@gmail.com"
          type="email"
        />
        <button id="enviar"className='boton' type="submit">ENVIAR</button>
      </Form>
      </Formik>
    </div>
    <div>
      <button className='boton'>
    <Link href="/inicio-sesion">Iniciar Sesión</Link>
      </button>
    </div>
  </>
);

//ReactDOM.render(<Registro />,document.getElementById('root'));
export default Registro;


