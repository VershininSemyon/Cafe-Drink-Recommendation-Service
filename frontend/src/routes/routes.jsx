
import Login from '../components/Account/Login';
import Registration from '../components/Account/Registration';
import CompleteRegistration from '../components/Account/CompleteRegistration';
import Http404 from '../errors/Http404';
import Home from '../pages/Home';


export const routes = [
    {
        path: "/",
        element: <Home />,
        isProtected: false
    },

    {
        path: "/register",
        element: <Registration />,
        isProtected: false
    },

    {
        path: "/complete-registration/:token",
        element: <CompleteRegistration />,
        isProtected: false
    },

    {
        path: "/login",
        element: <Login />,
        isProtected: false
    },

    {
        path: "*",
        element: <Http404 />,
        isProtected: false
    }
];
