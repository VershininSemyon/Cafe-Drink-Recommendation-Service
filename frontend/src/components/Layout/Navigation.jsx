
import React from 'react';
import { Nav } from 'react-bootstrap';
import { Link, useLocation } from 'react-router-dom';


const Navigation = () => {
    const location = useLocation();

    const navItems = [
        { path: '/', label: 'Главная страница', icon: '🏠' },
    ];

    return (
        <div className="bg-light border-end p-3" style={{ width: '250px' }}>
            <h5 className="mb-4">Навигация</h5>

            <Nav className="flex-column">
                {navItems.map((item) => (
                    <Nav.Link
                        key={item.path}
                        as={Link}
                        to={item.path}
                        active={location.pathname === item.path}
                        className="mb-2 d-flex align-items-center"
                        style={
                            location.pathname === item.path 
                            ? 
                            { backgroundColor: '#007bff', color: 'white', borderRadius: '5px', padding: '8px 12px' } 
                            : 
                            {}
                        }
                    >
                        <span className="me-2">{item.icon}</span>
                        {item.label}
                    </Nav.Link>
                ))}
            </Nav>
        </div>
    );
};

export default Navigation;
