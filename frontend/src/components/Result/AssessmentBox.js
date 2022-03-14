import React from "react";
import { Container, Box, Button, Grid, Typography, TextField, FormHelperText, FormControl, RadioGroup, Radio, FormControlLabel } from "@material-ui/core";
export const AssBoxx = ({data}) => {
    const assessments = data["Eligibility"]

    
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
                            ASSESSMENT OUTCOMES
                        </text>
                    </div>
                    {
                        assessments.map(d => <div key={d}style={{fontSize:'11px',fontWeight:'bold'}}>{d["eligibility__name"]} - {d['count']}</div>)
                    }
                    </g>
                </Box>
                </>
                );
        };
    
    
        