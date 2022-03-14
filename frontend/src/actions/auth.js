import Cookies from 'js-cookie';
import fetch from 'node-fetch';
import {LOGIN_SUCCESS, LOGIN_FAIL, LOGOUT_SUCCESS, LOGOUT_FAIL} from './types';
import axios from 'axios';




export const login = (username, password) => async dispatch => {
  // let csrftoken = getCookie('csrftoken')
  // console.log(csrftoken)
   
    const requestOptions = {
            headers : {'Accept':'application/json',
                        'Content-Type':'application/json',
                        'X-CSRFToken': Cookies.get('csrftoken')
            },
    }
         
    const body = JSON.stringify({username, password})
            
    
    try {
        const res = await axios.post('/clients/login', body, requestOptions);
        
        if (res.data.success) {
            dispatch({
                type: LOGIN_SUCCESS,
                payload: res.data.username
            });
            //console.log(res.json())
        } else {
            dispatch({
                type: LOGIN_FAIL
            });
          
        }
    } catch (err){
        
    }
};

export const logout = () => async dispatch => {
  // let csrftoken = CSRFToken('csrftoken')
   //console.log(csrftoken)

    const requestOptions = {
            credentials : 'include',
            headers : {'Accept':'application/json',
                        'Content-Type':'application/json',
                        'X-CSRFToken': Cookies.get('csrftoken')
            },
    }
    
    const body = JSON.stringify({
        'withCredentials':true
    });
    try {
        const res = await axios.post('/clients/logout',body,requestOptions);
        
        if (res.data.success) {
            dispatch({
                type: LOGOUT_SUCCESS
            });
            console.log(res.json())
        } else {
            dispatch({
                type: LOGOUT_FAIL
            });
          
        }
    } catch (err){
        dispatch({
            type:LOGOUT_FAIL
        })
        
    }
};




