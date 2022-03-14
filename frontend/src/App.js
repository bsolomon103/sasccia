import React from 'react';
import { render } from "react-dom";
import AllClientsPage from "./containers/SummaryPage";
import {Home} from './containers/home';
import {Sasccia} from './containers/sasscia';
import Login from './containers/login';
import {Layout} from './hocs/layout';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store';
import {SearchFunction} from './components/Search';


export default function App () {
   

    return (
            <Provider store={store}>
               <Router>
                    <Layout>
                        <Routes>
                            <Route path='/' element={<Home />}/>
                            <Route path='/summary' element={<AllClientsPage/>}/>
                            <Route path='/login' element={<Login />}/>
                            <Route path='/search' element={<SearchFunction />}></Route>
                        </Routes>
                    </Layout>
                </Router>
            </Provider>
            );
}

/*
                



*/












