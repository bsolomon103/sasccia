import React from 'react';
import {Link} from 'react-router-dom';


export const Home = () => (
    <div className='container'>
        <div className='mt-5 p=5 bg-light'>
        
            <h6 className='display-4'>Welcome to SASCCIA</h6>
            <p className='lead'>
             Southend Adult Social Care Client Intelligence Application.
            </p>
            <hr className='my-4'/>
             <p> Click the button below to log in.</p>
            <Link className='btn btn-primary btn-lg' to='/login'>Login</Link>
           
        </div>
    </div>
    )