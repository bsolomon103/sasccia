import React from 'react';
import {NavLink, Link} from 'react-router-dom';


export const Sasccia = () => (
    <div className='container'>
        <div className='mt-5 p=5 bg-light'>
        
            <h6 className='display-4'>Welcome to SASCCIA</h6>
            <p className='lead'>
             Southend Adult Social Care Client Intelligence Application.
            </p>
            <hr className='my-4'/>
             <p>Navigate the App</p>
             <li className='nav-item'>
            <Link className='nav-link' to='/search'>Search</Link>
            </li>
             <li className='nav-item'>
            <Link className='nav-link' exact to='/summary'>Summary</Link>
            </li>
        </div>
    </div>
    )