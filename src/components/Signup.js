import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Signup = () => {
  const [psswrd, setPassword] = useState("");
  const [confirmPass, setConfirmPass] = useState("");
  const [email, setEmail] = useState("");
  const [pseudo, setPseudo] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (event) => {
    const post = {
      email: email,
      pseudo: pseudo,
      mdp: psswrd,
    };
    event.preventDefault();

    axios
      .post("http://localhost:5000/user", post)
      .then((res) => {
        console.log("Status", res.status);
        console.log("Data", res.data);
        console.log(post);
        if (res.data === "ok") {
          navigate("/");
          window.location.reload();
        } else {
          setError("error");
        }
      })
      .catch(({ error }) => {
        console.error("erreur envoie enregistrement", error);
      });
  };

  return (
    <div className="signup">
      <form onSubmit={handleSubmit}>
        <h2>Inscrivez-vous</h2>

        <label>Pseudo</label>
        <br />

        <input
          type="text"
          value={pseudo}
          onChange={(e) => setPseudo(e.target.value)}
          required
        />
        <br />
        <br />

        <label>Adresse mail</label>
        <br />
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        ></input>
        <br />
        <br />

        <label>Mot de passe</label>
        <br />
        <input
          type="password"
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        {psswrd.length < 8 && psswrd.length > 3 && (
          <p>
            Le mot de passe est trop petit, il doit faire 8 caractères minimum
          </p>
        )}
        <br />
        <br />
        <label>Confirmer mot de passe</label>
        <br />
        <input
          type="password"
          onChange={(e) => setConfirmPass(e.target.value)}
          required
        />
        {confirmPass.length > 4 && psswrd !== confirmPass && (
          <p>Les mots de passes ne correspondent pas</p>
        )}
        <br />
        <br />

        <button type="submit"> S'enregistrer</button>
        {error ? (
          <p style={{ color: "red", textAlign: "center" }}>
            Compte déja existant
          </p>
        ) : (
          ""
        )}
      </form>
    </div>
  );
};

export default Signup;
