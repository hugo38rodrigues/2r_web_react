import React from "react";
import axios from "axios";
import { useState } from "react";

const Login = () => {
  const [mdp, setMdp] = useState("");
  const [pseudo, setPseudo] = useState("");

  const handlesubmit = () => {
    console.log(mdp);
    console.log(pseudo);
    const data_connexion = {
      pseudo: pseudo,
      mdp: mdp,
    };

    axios
      .post("http://127.0.0.1:5000/connexion", data_connexion)

      .catch((error) => console.log("Error: ", error));
  };
  // axios
  //   .post("http://localhost:5000/connexion", JSON.stringify(connexionData))
  //   .then(function (response) {
  //     // ! remplacer le "console.log" par un test de vérification d'un user et ajouter les pages utilisateurs
  //     console.log(response);
  //   })
  //   .catch(function (error) {
  //     console.log(error);
  //   });

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
          onChange={(e) => setPseudo(e.target.value)}
        />
        <br />
        <br />
        <label>Mot de passe</label>
        <br />
        <input
          type="password"
          name="mdp"
          onChange={(e) => setMdp(e.target.value)}
        />
        <br />
        <br />
        <button type="submit">Connexion</button>
      </form>
    </div>
  );
};

export default Login;
