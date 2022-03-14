 import React, {useState, useEffect} from 'react';
 import { json } from 'd3';
 
 const apiEndpoint = 'clients/all';


 export  const useData = () => {
        const [data, setData] = useState(null);
        
       
        useEffect(() => {
        json(apiEndpoint)
        .then(setData);
    
    },[]);
        //console.log(data)
        return data;
    };