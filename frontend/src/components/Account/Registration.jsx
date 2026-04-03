
import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import { useErrorMessage } from '../../hooks/useErrorMessage';
import { Form, Button, Card, Alert, Container, Row, Col } from 'react-bootstrap';
import { authService } from '../../services/authService';


const Registration = () => {
    const initialFormData = {
        username: "",
        email: "",
        password: "",
        re_password: ""
    }
    const [formData, setFormData] = useState(initialFormData);
    const [registrationInitiated, setRegistrationInitiated] = useState(false);
    const [registeredEmail, setRegisteredEmail] = useState('');
    const [passwordError, setPasswordError] = useState('');
    const [fieldErrors, setFieldErrors] = useState({});
    const {errorMessage, handleError} = useErrorMessage();

    const navigate = useNavigate();

    const validatePasswords = (pass = formData.password, re_pass = formData.re_password) => {
        if (pass !== re_pass) {
            setPasswordError('Пароли не совпадают');
            return false;
        }
        if (pass.length < 8) {
            setPasswordError('Пароль должен содержать минимум 8 символов');
            return false;
        }
        setPasswordError('');
        return true;
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        
        if (!validatePasswords(formData.password, formData.re_password)) {
            return;
        }

        setFieldErrors({});
        
        authService.initiateRegistration(formData)
            .then((response) => {
                setRegisteredEmail(response.data.email);
                setRegistrationInitiated(true);
            })
            .catch((err) => {
                if (err.response?.data) {
                    setFieldErrors(err.response.data);
                }
                handleError(err);
            });
    }

    const handleResendClick = () => {
        authService.resendVerification(registeredEmail)
            .then(() => {
                alert('Письмо отправлено повторно! Проверьте почту.');
            })
            .catch((err) => {
                alert('Ошибка при отправке письма: ' + (err.response?.data?.error || err.message));
            });
    };

    if (registrationInitiated) {
        return (
            <Container className="d-flex justify-content-center align-items-center min-vh-100">
                <Row className="w-100">
                    <Col md={6} lg={4} className="mx-auto">
                        <Card className="shadow">
                            <Card.Body className="p-4 text-center">
                                <Alert variant="success" className="mb-3">
                                    <Alert.Heading>✓ Письмо отправлено!</Alert.Heading>
                                </Alert>
                                <p className="mb-3">
                                    Мы отправили письмо с подтверждением на адрес <strong>{registeredEmail}</strong>.
                                </p>
                                <p className="mb-3">
                                    Перейдите по ссылке в письме, чтобы завершить регистрацию.
                                </p>
                                <div className="d-grid gap-2">
                                    <Button 
                                        variant="primary" 
                                        onClick={() => navigate('/login')}
                                    >
                                        Перейти к входу
                                    </Button>
                                    <Button 
                                        variant="outline-secondary" 
                                        onClick={handleResendClick}
                                    >
                                        Отправить письмо повторно
                                    </Button>
                                </div>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
        );
    }

    const getFieldError = (fieldName) => {
        if (fieldErrors[fieldName]) {
            return Array.isArray(fieldErrors[fieldName]) 
                ? fieldErrors[fieldName][0] 
                : fieldErrors[fieldName];
        }
        return null;
    };

    return (
        <Container className="d-flex justify-content-center align-items-center min-vh-100">
            <Row className="w-100">
                <Col md={6} lg={4} className="mx-auto">
                    <Card className="shadow">
                        <Card.Body className="p-4">
                            <Card.Title className="text-center mb-4">
                                <h3>Создание аккаунта</h3>
                            </Card.Title>
                            
                            <Form method="POST" onSubmit={handleSubmit}>
                                <Form.Group className="mb-3">
                                    <Form.Label htmlFor="username">Никнейм</Form.Label>
                                    <Form.Control
                                        id="username"
                                        type="text"
                                        placeholder="Введите ваш никнейм"
                                        value={formData.username}
                                        onChange={(e) => {
                                            setFormData({...formData, username: e.target.value});
                                            setFieldErrors({...fieldErrors, username: null});
                                        }}
                                        required
                                        isInvalid={!!getFieldError('username')}
                                    />
                                    <Form.Control.Feedback type="invalid">
                                        {getFieldError('username')}
                                    </Form.Control.Feedback>
                                </Form.Group>

                                <Form.Group className="mb-3">
                                    <Form.Label htmlFor="email">Почта</Form.Label>
                                    <Form.Control
                                        id="email"
                                        type="email"
                                        placeholder="Введите вашу почту"
                                        value={formData.email}
                                        onChange={(e) => {
                                            setFormData({...formData, email: e.target.value});
                                            setFieldErrors({...fieldErrors, email: null});
                                        }}
                                        required
                                        isInvalid={!!getFieldError('email')}
                                    />
                                    <Form.Control.Feedback type="invalid">
                                        {getFieldError('email')}
                                    </Form.Control.Feedback>
                                </Form.Group>

                                <Form.Group className="mb-3">
                                    <Form.Label htmlFor="password">Пароль</Form.Label>
                                    <Form.Control
                                        id="password"
                                        type="password"
                                        placeholder="Введите пароль"
                                        value={formData.password}
                                        onChange={(e) => {
                                            const val = e.target.value;
                                            setFormData({...formData, password: val});
                                            validatePasswords(val, formData.re_password);
                                        }}
                                        required
                                        isInvalid={!!passwordError || !!getFieldError('password')}
                                    />
                                    {getFieldError('password') && (
                                        <Form.Text className="text-danger">
                                            {getFieldError('password')}
                                        </Form.Text>
                                    )}
                                </Form.Group>

                                <Form.Group className="mb-4">
                                    <Form.Label htmlFor="re_password">Подтверждение пароля</Form.Label>
                                    <Form.Control
                                        id="re_password"
                                        type="password"
                                        placeholder="Повторите пароль"
                                        value={formData.re_password}
                                        onChange={(e) => {
                                            const val = e.target.value;
                                            setFormData({...formData, re_password: val});
                                            validatePasswords(formData.password, val);
                                        }}
                                        required
                                        isInvalid={!!passwordError}
                                    />
                                    <Form.Control.Feedback type="invalid">
                                        {passwordError}
                                    </Form.Control.Feedback>
                                </Form.Group>

                                {errorMessage && (
                                    <Alert variant="danger" className="mb-3">
                                        Ошибка: {errorMessage}
                                    </Alert>
                                )}
                                
                                <div className="d-grid gap-2 mb-3">
                                    <Button 
                                        variant="primary" 
                                        type="submit" 
                                        size="lg"
                                        disabled={!!passwordError || !formData.password || !formData.re_password}
                                    >
                                        Зарегистрироваться
                                    </Button>
                                </div>
                                
                                <div className="text-center">
                                    <p className="mb-2">Уже есть аккаунт?</p>
                                    <Button variant="outline-secondary" as="a" href="/login">
                                        Войти
                                    </Button>
                                </div>
                            </Form>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
    )
}

export default Registration;
