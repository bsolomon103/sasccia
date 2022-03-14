import React, {useState} from 'react';
import {useNavigate, Link} from 'react-router-dom';
import {connect} from 'react-redux';
import {login} from '../actions/auth';
//import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
//import AllClientsPage from './SummaryPage';
import CSRFToken from '../components/CSRFToken';


const mapStateToProps = state => ({
    isAuthenticated : state.auth.isAuthenticated
})

 const Login = ({ login, isAuthenticated }) => {
    const navigate = useNavigate()
    
    const [formData, setFormData] = useState({
        username: '',
        password:''
    });
    
    const { username, password } = formData;
    
    const onChange = (e) => setFormData({...formData, [e.target.name]: e.target.value}) 
    
    const onSubmit = (e) => {
        e.preventDefault();
        login(username, password)
    };
    
    if (isAuthenticated)
        navigate('/summary')
   
        
    
    
    return (
            <div className='container mt-5'>
                <h1>Sign In</h1>
                <form onSubmit={e => onSubmit(e)}>
                <CSRFToken />
                    <div className="form-group">
                        <label className="form-label">Username: </label>
                        <input 
                            className="form-control"
                            type="text"
                            placeholder="Username*"
                            name="username"
                            onChange={e => onChange(e)}
                            value={username}
                            required
                            >
                        </input>
                    </div>
                      <div className='form-group'>
                        <label className='form-label mt-3'>Password: </label>
                        <input 
                            className='form-control'
                            type='password'
                            placeholder='Password*'
                            name='password'
                            onChange={e => onChange(e)}
                            value={password}
                            minLength='6'
                            required
                            >
                        </input>
                    </div>
                    <button className='btn btn-primary mt-3' type='submit'>Login</button>
                </form>
            
            </div>
        );
    };


export default connect(mapStateToProps, { login })(Login);