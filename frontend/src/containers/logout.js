/*
import React, {useState} from 'react';
import {Redirect, Link, useNavigate} from 'react-router-dom';
import {connect} from 'react-redux';
import {login, logout} from '../actions/auth';

const Logout = ({logout}) => {
      let navigate = useNavigate()
    
    const [formData, setFormData] = useState({
        username: '',
        password:''
    });
    
    const { username, password } = formData;
    const onChange = (e) => setFormData({...formData, [e.target.name]: e.target.value}) 
    const onSubmit = (e) => {
    logout(username, password);
       
        
    };
 
    
    return (
        <div>
            <h1>Sign In</h1>
            <form onSubmit={e => onSubmit(e)}>
            <CSRFToken />
            <div>
            <label>Username:</label>
            <input 
                type='text'
                placeholder='Username'
                name='username'
                onChange={e=> onChange(e)}
                value = {username}
                required
                />
            </div>
            <div>
                <label>Password: </label>
                <input
                    type='password'
                    placeholder='Password'
                    name='password'
                    onChange={e => onChange(e)}
                    value={password}
                    required
                />
            </div>
            <button type='submit'>Login</button>
            </form>
        </div>
        )
};

const mapStateToProps = state => ({
    isAuthenticated : state.auth.isAuthenticated
})

export default connect (mapStateToProps, {login})(Login);
*/
