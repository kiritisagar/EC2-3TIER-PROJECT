import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './components/Home';
import './App.css';  // Import global CSS file

const App = () => {
    return (
        <div>
            <Header />
            <main>
                <Home />
                {/* Other components or routes can be added here */}
            </main>
            <Footer />
        </div>
    );
}

export default App;

