import React from "react";
import { Container, Box, Button, Grid, Typography, TextField, FormHelperText, FormControl, RadioGroup, Radio, FormControlLabel } from "@material-ui/core";
export const RatioBoxx = ({data}) => (
        <Box sx={{
               // border: '3px solid royalblue', 
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
                            SERVICES TO REQUESTS RATIO
                        </text>
                    </div>
                    <div>
                        <text component='body'style={{color:"black", fontSize:'60px',fontWeight:'bold'}}>
                            {data['Request_Service_Ratio'][0]['ratio'].toFixed(1)} 
                        </text>
                    </div>
                  
                    </g>
                </Box>);