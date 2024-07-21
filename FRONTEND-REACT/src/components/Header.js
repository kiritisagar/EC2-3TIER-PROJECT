import React from 'react';
import './Header.css';  // Import CSS file specific to the Header component

const Header = () => {
    return (
        <header>
            <h1>My React App</h1>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about.html">About</a></li>
                    <li><a href="/contact.html">Contact</a></li>
                    <li><a href="/product.html">Product</a></li>
                    <li><a href="/testimonial.html">Testimonials</a></li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;

