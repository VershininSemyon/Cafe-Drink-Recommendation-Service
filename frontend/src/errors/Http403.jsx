
import React from 'react';
import { Container, Card, Button } from 'react-bootstrap';
import { AlertTriangle, ArrowLeft } from 'react-feather';
import { Link } from 'react-router-dom';


const Http403 = ({ message = "У вас нет прав для просмотра этой страницы" }) => {
    return (
        <Container className="d-flex justify-content-center align-items-center" style={{ minHeight: '70vh' }}>
            <Card className="border-0 shadow-sm text-center" style={{ maxWidth: '500px', width: '100%' }}>
                <Card.Body className="p-5">
                    <div className="mb-4">
                        <AlertTriangle size={64} className="text-warning" />
                    </div>
                    <h3 className="mb-3">Доступ запрещен</h3>
                    <p className="text-muted mb-4">{message}</p>
                    
                    <Button
                        as={Link}
                        to="/"
                        variant="outline-primary"
                        className="d-flex align-items-center justify-content-center gap-2 mx-auto"
                    >
                        <ArrowLeft size={18} />
                        На главную
                    </Button>
                </Card.Body>
            </Card>
        </Container>
    );
};

export default Http403;
