
import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Card, Alert, Container, Row, Col, Button, Spinner } from 'react-bootstrap';
import api from '../../services/api';


const CompleteRegistration = () => {
    const { token } = useParams();
    const navigate = useNavigate();
    const [status, setStatus] = useState('verifying');
    const [message, setMessage] = useState('');
    const [errorDetail, setErrorDetail] = useState('');

    useEffect(() => {
        const completeRegistration = async () => {
            try {
                const response = await api.post(`/users/register/complete/${token}/`);
                setStatus('success');
                setMessage(response.data.message);
                
                setTimeout(() => {
                    navigate('/login');
                }, 5000);
            } catch (error) {
                setStatus('error');
                setMessage(error.response?.data?.error || 'Невалидный формат ссылки.');
                setErrorDetail(error.response?.data?.detail || '');
            }
        };

        if (token) {
            completeRegistration();
        }
    }, [token, navigate]);

    const handleResendClick = async () => {
        const email = prompt('Введите ваш email для повторной отправки письма:');
        if (email) {
            try {
                await api.post('/users/register/resend/', { email });
                alert('Письмо отправлено повторно! Проверьте почту.');
            } catch (error) {
                alert('Ошибка: ' + (error.response?.data?.error || error.message));
            }
        }
    };

    return (
        <Container className="d-flex justify-content-center align-items-center min-vh-100">
            <Row className="w-100">
                <Col md={6} lg={4} className="mx-auto">
                    <Card className="shadow">
                        <Card.Body className="p-4 text-center">
                            {status === 'verifying' && (
                                <>
                                    <Spinner animation="border" variant="success" className="mb-3" />
                                    <h4>Завершение регистрации...</h4>
                                    <p className="text-muted">Пожалуйста, подождите</p>
                                </>
                            )}

                            {status === 'success' && (
                                <>
                                    <Alert variant="success" className="mb-3">
                                        <Alert.Heading>✓ Регистрация завершена!</Alert.Heading>
                                        <p>{message}</p>
                                    </Alert>
                                    <p className="text-muted">
                                        Вы будете перенаправлены на страницу входа через 5 секунд
                                    </p>
                                    <Button 
                                        variant="success" 
                                        onClick={() => navigate('/login')}
                                    >
                                        Перейти к входу
                                    </Button>
                                </>
                            )}

                            {status === 'error' && (
                                <>
                                    <Alert variant="danger" className="mb-3">
                                        <Alert.Heading>✗ Ошибка</Alert.Heading>
                                        <p>{message}</p>
                                        {errorDetail && <p className="small">{errorDetail}</p>}
                                    </Alert>
                                    <div className="d-grid gap-2">
                                        <Button 
                                            variant="primary" 
                                            onClick={() => navigate('/register')}
                                        >
                                            Попробовать снова
                                        </Button>
                                        <Button 
                                            variant="outline-secondary" 
                                            onClick={handleResendClick}
                                        >
                                            Отправить письмо повторно
                                        </Button>
                                    </div>
                                </>
                            )}
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
    );
};

export default CompleteRegistration;
