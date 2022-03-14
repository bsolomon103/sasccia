import React from "react";
import { Container, Box, Button, Grid, Typography, TextField, FormHelperText, FormControl, RadioGroup, Radio, FormControlLabel } from "@material-ui/core";
export const SupportBoxx = ({data}) => {
    const planType = data["Plan Type"]

    
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
                            SERVICE TYPES
                        </text>
                    </div>
                    {
                        planType.map(d => <div key={d}style={{fontSize:'11px',fontWeight:'bold'}}>{d["serviceType__name"]}</div>)
                    }
                    </g>
                </Box>
                </>
                );
        };
    
    
        