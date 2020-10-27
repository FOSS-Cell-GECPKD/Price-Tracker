import React from "react";
import propTypes from 'prop-types'


const Navbar = ({ icon, title }) => {



    return (
        <nav className='navbar bg-primary'>
            <h1>
                <i className={icon} /> {title}
            </h1>
            <ul>
                <li>Home</li>
                <li>About us</li>
            </ul>
        </nav>
    );
}

Navbar.defaultProps = {
    title: "Price Tracker",
    icon: "fas fa-hand-holding-usd"
}
Navbar.propTypes = {
    title: propTypes.string.isRequired,
    icon: propTypes.string.isRequired
}

export default Navbar;
