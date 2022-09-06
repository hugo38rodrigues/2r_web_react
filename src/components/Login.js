import React from "react";
import axios from "axios";
import { useState } from "react";

const Login = () => {
  const [mdp, setMdp] = useState("");
  const [pseudo, setPseudo] = useState("");

  axios
    .post("/connexion", {
      MDP: mdp,
      Pseudo: pseudo,
    })
    .then(function (response) {
      // ! remplacer le "console.log" par un test de vérification d'un user et ajouter les pages utilisateurs
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });

  return (
    <div className="login">
      <form method="post">
        <h2>Connexion</h2>
        <br /> <br />
        <label>Pseudo</label>
        <br />
        <input type="text" onChange={(e) => setPseudo(e.target.value)} />
        <br />
        <br />
        <label>Mot de passe</label>
        <br />
        <input
          type="password"
          onChange={(e) => setMdp(e.target.value)}
          name=""
          id=""
        />
        <br />
        <br />
        <button type="submit">Connexion</button>
      </form>
    </div>
  );
};

export default Login;
