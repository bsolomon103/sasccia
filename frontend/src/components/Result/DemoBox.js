import React from "react";
import { Container, Box, Button, Grid, Typography, TextField, FormHelperText, FormControl, RadioGroup, Radio, FormControlLabel } from "@material-ui/core";
export const Boxx = ({data}) => (
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
                            Name: {data['Basics']['name']} 
                        </text>
                    </div>
                    <div>
                        <text component='body'style={{color:"black", fontSize:'12px',fontWeight:'bold'}}>
                            Gender: {data['Basics']['gender']}
                        </text>
                    </div>
                     <div>
                        <text component='body'style={{color:"black", fontSize:'12px',fontWeight:'bold'}} >
                            Age: {data['Basics']['age']}
                        </text>
                    </div>
                     <div>
                        <text style={{fontSize:'12px', fontWeight:'bold'}}>
                            {data['Basics']['ethnicity']}
                        </text>
                    </div>
                    <div>
                        <text component='body'style={{color:"black", fontSize:'12px', fontWeight:'bold'}} >
                            Postcode:  {data['Basics']['postcode']}
                        </text>
                    </div>
                    </g>
                </Box>);