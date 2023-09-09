import React from "react";
import Link from "next/link";
import "../../styles/inicio-sesion.css";

export default function Inicio_sesion() {
    return(   
        <> 
            <form className="container">
                <h1>INICIAR SESIÓN</h1>
                <div className="mb-3">
                    <label for="exampleInputEmail1" className="form-label">Dirección de Email</label> <br/>
                    <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                    </input>    <br/>
                    <label for="exampleInputPassword1" className="form-label">Contraseña</label><br/>
                    <input type="password" className="form-control" id="exampleInputPassword1" maxLength={8}>
                    </input>
                </div>
                <button type="submit" className="enviar">ENVIAR</button>
            </form>
            <div>
                <button className="boton"><Link href="/registro">Registrate</Link></button>
            </div>
            <div>
                <button className="boton"><Link href="/lista-tarea">Lista tarea</Link></button>
            </div>
        </>
    )

}

/*<>
<h4>Sino sos usuario registrado:</h4>
<Link to="/registro">REGISTRATE</Link>
</>*/
