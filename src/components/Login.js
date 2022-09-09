import React from "react";
import axios from "axios";
import { useState } from "react";
import md5 from "md5";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [mdp, setMdp] = useState("");
  const [pseudo, setPseudo] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const handlesubmit = (event) => {
    event.preventDefault();
    axios
      .post("http://127.0.0.1:5000/connexion", {
        pseudo: pseudo,
        mdp: md5(mdp),
      })
      .then((response) => {
        if (response.data === "ok") {
          navigate("/Acceuil");
          window.location.reload();
        } else {
          setError("error");
          setPseudo("");
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
        <label>Pseudo</label>
        <br />
        <input
          type="text"
          name="pseudo"
          value={pseudo}
          onChange={(e) => setPseudo(e.target.value)}
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
        {error ? <p>Vérifier votre mot de passe ou pseudo !</p> : ""}
      </form>
    </div>
  );
};

export default Login;
