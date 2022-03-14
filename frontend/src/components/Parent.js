import React, {useState, useEffect} from "react";
import {Typography, FormControl, FormHelperText,TextField,InputAdornment,Input,Button} from "@material-ui/core";
import  fetch  from 'node-fetch';
import {json} from 'd3';
import { BrowserRouter as Router, Routes, Route, Link, Redirect, useNavigate } from "react-router-dom";
import {SearchBar} from './SearchBar';
import {Result} from './Result/index.js';
import Cookies from 'js-cookie';


export const Parent = () => {
    let navigate = useNavigate();
    const [data, setData] = useState({
        lasID: '',
        error:''
    })
    
    const[result, setResult] = useState('');
    
    const handleLASChange=(e) => {
      
        setData(data => ({
            ...data,
            lasID:e.target.value
        }));
    }
    
    const handleBackButtonPressed = () => {
     navigate('/summary')
    };
    
  

    
    //let csrftoken = CSRFToken('csrftoken');
    const handleEnterButtonPressed = async () => {
        const requestOptions = {
            method : 'POST',
            headers : {'Accept':'application/json',
                        'Content-Type':'application/json',
                        'X-CSRFToken': Cookies.get('csrftoken')
            },
            credentials:'include',
            credientials:'same-origin',
            body : JSON.stringify({lasID : + data.lasID}),
            };
            
            return await fetch('/clients/get-client', requestOptions)
            .then((response ) => {
                if (response.ok) {
                    return (response.json())
                    .then((data)=> {
                        setResult(data)
                    })
                 } 

                else {
                    setData((data) => ({
                        ...data,
                        error:'Client Not Found'
                    }));
                }
            }).catch((error) => {
                //console.log(error)
            })
          
    }   
    
   
            
   console.log(result);
   
 
  
  if (!result){  
         return (<h6 align='center'>

                        <SearchBar data={data.lasID} onChange={handleLASChange} error={data.error}/>
                        <Button color='primary' to='/search' variant='contained' onClick={handleEnterButtonPressed}>Enter</Button>
                        <Button color='secondary'  to='/summary' variant="contained" component={Link}>Back</Button>
                </h6>
               
                
                )
    }
    
    else return (<>
                <div className='scrollable'>
                <h6 align='center'>
                    <Button color='secondary' to='/summary' variant='contained' component={Link}>Back</Button>
                </h6>
                <div>
                    <Result data={result} />
                </div>
                </div>
                </>
                )
    
}


   
  
    

    

   
    
