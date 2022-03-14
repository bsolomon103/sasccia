import React, {useState, useEffect} from "react";
import {Typography, FormControl, FormHelperText,TextField,InputAdornment,Input,Button} from "@material-ui/core";
import  fetch  from 'node-fetch';
import {json} from 'd3';
import { BrowserRouter as Router, Routes, Route, Link, Redirect, useNavigate } from "react-router-dom";
import {Result} from './Result';
  
export const SearchBar = ({data,onChange, error}) => {
    console.log(data)
    return (
    <div>
        
            <FormControl component='fieldset'>
                <TextField
                    error={error}
                    required={true}
                    value={data}
                    onChange={onChange}
                    placeholder="Search LAS ID"
                    color='primary' 
                    variant='outlined' 
                    size="small" 
                    label="Search"
                    helperText={error}
                />
            </FormControl>
            
    
    </div>
            
    );

}


