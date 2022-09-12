import React, { useState, useEffect } from "react";
import axios from "axios";

const AffichageRessource = () => {
  const [ressource, setRess] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/ress").then((res) => setRess(res.data));
  }, []);

  return (
    <div className="affichage-ressource">
      {ressource.map((ress) => (
        <div key={ress.titre} className="affichage-content">
          <div id="ress">
            <div className="ress">
              <div id="Global">
                <div id="gauche">
                  <h1> {ress.titre}</h1>
                </div>
                <div id="droite">
                  <p className="date_crea">{ress.date}</p>
                  <p className="createur">{ress.pseudo}</p>
                </div>
              </div>
              <br />
              <p className="text">{ress.description}</p>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default AffichageRessource;
