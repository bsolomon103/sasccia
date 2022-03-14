import React, {Fragment} from 'react';
import {Link, NavLink} from 'react-router-dom';
import { connect } from 'react-redux';
import { logout } from '../actions/auth';


const mapStateToProps = state => ({
    isAuthenticated : state.auth.isAuthenticated
})


const NavBar = ({ logout, isAuthenticated })=> {
  const guestLinks = (
              <div>
                <li className='nav-item'>
                  <NavLink className='nav-link' to='/login'>Login</NavLink>
                </li>
              </div>
            );
  const authLinks = (
              <>
                <li className='nav-item'>
                    <NavLink className='nav-link' exact to='/summary'>Summary</NavLink>
                  </li>
                <li className='nav-item'>
                  <NavLink className='nav-link' exact to='/search'>Search</NavLink>
                </li>
                <li className='nav-item'>
                  <a className='nav-link' to='/' onClick={ logout } href='http://sasccia-env.eba-h9gum2ew.eu-west-2.elasticbeanstalk.com/login'>Logout</a>
                </li>
              </>
            );
        return (
        <nav className='navbar navbar-expand-lg navbar-light bg-light'>
          <div className='container-fluid'>
            <Link className='navbar-brand' to='/'>SASCCIA</Link>
            <button className='navbar-toggler' type='button' data-bs-toggle='collapse' data-bs-target='#navbarNav' aria-controls='navbarNav' aria-expanded='false' aria-label='Toggle navigation'>
              <span className='navbar-toggler-icon'></span>
            </button>
            <div className='collapse navbar-collapse' id='navbarNav'>
              <ul className='navbar-nav'>
                <li className='nav-item'>
                  <NavLink className='nav-link' exact to='/'>Home</NavLink>
                </li>
                  { isAuthenticated ? authLinks : guestLinks }
              </ul>
            </div>
          </div>
        </nav>
    );
};



export default connect(mapStateToProps, { logout })(NavBar);