import React from "react";
import { Container, Box, Button, Grid, Typography, TextField, FormHelperText, FormControl, RadioGroup, Radio, FormControlLabel } from "@material-ui/core";
export const HealthBoxx = ({data}) => {
    const conditions = data["Health Conditions"]
    //console.log(psr)
    
    return (
    <>
    <Box sx={{
                //border: '3px solid royalblue', 
                mt: 2, 
                padding: 0,
                m: 2.5,
                b : 1,
                //bgcolor: 'royalblue', 
                boxShadow: 1
                //width: width, 
                //height: height
                }}
                align='center'>
                    <g className='boxx'>
                    <div>
                        <text component='body'style={{color:"black", fontSize:'12px',fontWeight:'bold'}}>
                            HEALTH CONDITIONS
                        </text>
                    </div>
                    {
                        conditions.map(d => <div key={d}style={{fontSize:'9.5px',fontWeight:'bold'}}>{d["condition"]}</div>)
                    }
                  
                    </g>
                </Box>
                </>
                );
        };
    
    
        