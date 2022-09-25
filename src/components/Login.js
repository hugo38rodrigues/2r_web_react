import React from "react";
import axios from "axios";
import { useState } from "react";
import md5 from "md5";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [mdp, setMdp] = useState("");
  const [email, setemail] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const handlesubmit = (event) => {
    event.preventDefault();
    axios
      .post("http://localhost:5000/connexion", {
        email: email,
        mdp: md5(mdp),
      })
      .then((response) => {
        if (response.status === 200) {
          navigate("/Acceuil");
          window.location.reload();
        } else {
          setError("error");
          setemail("");
          setMdp("");
        }
      })

      .catch((error) => console.log("Error: ", error));
  };

  return (
    <div className="login">
      <form onSubmit={handlesubmit}>
        <h2>Connexion</h2>
        <br /> <br />
        <label>adresse mail</label>
        <br />
        <input
          type="email"
          name="email"
          value={email}
          onChange={(e) => setemail(e.target.value)}
        />
        <br />
        <br />
        <label>Mot de passe</label>
        <br />
        <input
          type="password"
          value={mdp}
          name="mdp"
          onChange={(e) => setMdp(e.target.value)}
        />
        <br />
        <br />
        <button type="submit">Connexion</button>
        {error ? <p>Vérifier votre mot de passe ou email !</p> : ""}
      </form>
    </div>
  );
};

export default Login;
