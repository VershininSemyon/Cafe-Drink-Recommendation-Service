
import 'bootstrap/dist/css/bootstrap.min.css';
import Layout from './components/Layout/Layout';
import Routing from './routes/Routing';
import { BrowserRouter } from 'react-router-dom';


const App = () => {
    return (
        <BrowserRouter>
            <Layout>
                <Routing />
            </Layout>
        </BrowserRouter>
    )
}

export default App;
