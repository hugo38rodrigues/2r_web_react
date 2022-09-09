import Navigation from "../components/Navigations";
import React, { useState, useEffect } from "react";
import axios from "axios";

const Ressources = () => {
  const [titre, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [categorie, setCategorie] = useState([]);
  const [date_crea, setDate] = useState("");
  const [categoriesend, setCategorieSend] = useState("");

  // ? Récupere le ficher json avec une get
  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/cat")
      .then((res) => setCategorie(res.data));
  }, []);

  // ? poster la ressource
  const handleSubmit = (event) => {
    const post = {
      titre: titre,
      userid: 1,
      categorieid: categoriesend,
      description: description,
      date: date_crea,
    };
    event.preventDefault();

    axios
      .post("http://127.0.0.1:5000/ress", post)
      .then((res) => {
        console.log("Status", res.status);
        console.log("Data", res.data);
        console.log(post);
      })
      .catch(({ error }) => {
        console.error("Something went wrong!", error);
      });
  };

  // * Création du formulaire pour générer des ressources
  return (
    <div className="rs">
      <Navigation />
      <div className="ressources">
        <form onSubmit={handleSubmit}>
          <h2>Ressource</h2> <br />
          <label>Titre de la ressource</label>
          <br />
          <input
            type="text"
            name="title"
            onChange={(e) => setTitle(e.target.value)}
            required
          ></input>
          <br />
          <div className="recup-categorie">
            <label>Catégorie</label>
            <br />

            <select id="cat" onChange={(e) => setCategorieSend(e.target.value)}>
              <option value="">Sélectionnez votre catégorie</option>
              {categorie.map((cat) => (
                <option key={cat.id} value={cat.id}>
                  {cat.nom}
                </option>
              ))}
            </select>
          </div>
          <br />
          <br />
          <label>Description</label>
          <br />
          <textarea
            name="text"
            onChange={(e) => setDescription(e.target.value)}
            rows="10"
            cols="50"
            placeholder="Votre description."
            maxLength="500"
            required
          ></textarea>
          <br />
          <br />
          <label>Date de création du post</label>
          <br />
          <input
            type="date"
            name="date"
            onChange={(e) => setDate(e.target.value)}
          ></input>
          <br />
          <br />
          <button type="submit">Poster la ressource</button>
        </form>
      </div>
    </div>
  );
};

export default Ressources;
