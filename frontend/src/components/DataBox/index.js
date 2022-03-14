import React from 'react';


export const DataBox = ({data}) => {
    const cost = d => d['unitCost']
    
    return (
            <div>
                <text component='body'style={{color:"white", fontSize:'12px'}}>
                    {cost}</text>
            </div>
        
        
        )
    
}