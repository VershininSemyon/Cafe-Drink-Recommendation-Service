
import React, { useContext } from 'react';
import { Container, Navbar, Nav, Button } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import { AuthContext } from '../../contexts/AuthContext/AuthContext';
import { authService } from '../../services/authService';


const Header = () => {
    const { initialAuthState, authState, setAuthState } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleLogout = () => {
        authService.logout(initialAuthState, setAuthState);
        navigate('/login');
    };

    return (
        <Navbar bg="dark" variant="dark" expand="lg" className="mb-4">
            <Container>
                <Navbar.Brand as={Link} to="/" className="fw-bold">
                    Cafe Drink Recommendation Service
                </Navbar.Brand>
        
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav>
                        {authState.isAuthenticated ? (
                            <>
                                <Navbar.Text className="me-3">
                                    Привет, <strong>{authState.userData.username}</strong>
                                </Navbar.Text>
                                <Button variant="outline-light" onClick={handleLogout}>
                                    Выйти
                                </Button>
                            </>
                        ) : (
                            <>
                                <Button variant="outline-light" as={Link} to="/login" className="me-2">
                                    Войти
                                </Button>
                                <Button variant="primary" as={Link} to="/register">
                                    Регистрация
                                </Button>
                            </>
                        )}
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
};

export default Header;
