
import React from 'react';
import Http401 from '../errors/Http401';
import { useAuthCheck } from '../hooks/useAuthCheck';


const ProtectedRoute = ({ children }) => {
    const { isAuthenticated, isChecking } = useAuthCheck();

    if (isChecking) {
        return (
            <div className="d-flex justify-content-center align-items-center min-vh-100">
                <div className="spinner-border text-primary" role="status">
                    <span className="visually-hidden">Загрузка...</span>
                </div>
            </div>
        );
    }

    return isAuthenticated ? children : <Http401 />;
};

export default ProtectedRoute;
