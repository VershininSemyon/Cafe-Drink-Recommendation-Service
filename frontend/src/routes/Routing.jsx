
import React from 'react'
import { Routes, Route } from 'react-router-dom';
import { routes } from './routes';
import ProtectedRoute from './ProtectedRoute';


const Routing = () => {
    return (
        <Routes>
            {routes.map((data) => {
                return  <Route
                    path={data.path}
                    element={
                        data.isProtected ? <ProtectedRoute>{data.element}</ProtectedRoute> : data.element
                    }
                />
            })}
        </Routes>
    )
}

export default Routing
