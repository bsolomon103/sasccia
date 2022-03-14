import React from "react";
import { Container, Box, Button, Grid, Typography, TextField, FormHelperText, FormControl, RadioGroup, Radio, FormControlLabel } from "@material-ui/core";
export const DeceasedBoxx = ({data}) => {
    const status = data["Deceased"]

    
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
                            STATUS
                        </text>
                    </div>
                    <div>
                        <text component='body'style={{color:"black", fontSize:'12px',fontWeight:'bold'}}>
                            {status["status"]} 
                        </text>
                    </div>
                    </g>
                </Box>
                </>
                );
        };
    
    
        