
import { useState, useEffect, useContext, useCallback } from 'react';
import { AuthContext } from '../contexts/AuthContext/AuthContext';
import { authService } from '../services/authService';
import { jwtDecode } from 'jwt-decode';


export const useAuthCheck = () => {
    const { initialAuthState, authState, setAuthState } = useContext(AuthContext);
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [isChecking, setIsChecking] = useState(true);

    const checkAuth = useCallback(async () => {
        setIsChecking(true);
        
        if (!authState?.accessToken) {
            setIsAuthenticated(false);
            setIsChecking(false);
            return;
        }

        try {
            const decodedToken = jwtDecode(authState.accessToken);
            const currentTime = Date.now() / 1000;
            
            if (decodedToken.exp < currentTime) {
                if (authState.refreshToken) {
                    try {
                        await authService.refreshToken(initialAuthState, authState, setAuthState);
                        setIsAuthenticated(true);
                    } 
                    catch (error) {
                        console.error('Refresh token failed:', error);
                        setIsAuthenticated(false);
                    }
                } 
                else {
                    setIsAuthenticated(false);
                }
            } 
            else {
                setIsAuthenticated(true);
            }
        } 
        catch (error) {
            console.error('Token check error:', error);
            setIsAuthenticated(false);
        } 
        finally {
            setIsChecking(false);
        }
    }, [authState, initialAuthState, setAuthState]);

    useEffect(() => {
        checkAuth();
    }, [checkAuth]);

    return { isAuthenticated, isChecking, checkAuth };
};
