import React from 'react';
import { BrowserRouter,Routes, Route} from 'react-router-dom';
import Accueil from './Pages/Accueil';
import NotFound from './Pages/NotFound';
import Ressources from './Pages/Ressources';
import Contact from './Pages/Contacts';
import Connexion from './Pages/Connexion';

const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" exact element={<Connexion/>}/>
                <Route path="/Contacts" element={<Contact/>}/>
                <Route path="/Ressources" element={<Ressources/>}/>
                <Route path="/Acceuil" element= {<Accueil />}/>
                <Route path="*" element= {<NotFound />}/>
                
            </Routes>
        </BrowserRouter>

    );
};

export default App;