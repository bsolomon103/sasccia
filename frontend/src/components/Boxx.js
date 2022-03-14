import React from "react";
import { Container, Box, Button, Grid, Typography, TextField, FormHelperText, FormControl, RadioGroup, Radio, FormControlLabel } from "@material-ui/core";
export const Boxx = ({width, height, data}) => (
        <Box sx={{border: '3px dashed black', 
                mt: 2, 
                padding: 0,
                m: 2.5,
                b : 1,
                bgcolor: 'royalblue', 
                boxShadow: 1,
                width: width, 
                height: height}}
                align='center'>
                    <g className='boxx'>
                    <text style={{fontSize:'12px'}}>SNAPSHOT</text>
                    <div>
                        <text component='body'style={{color:"white", fontSize:'12px'}}>
                            Data Timeframe: {data['Timeframe']} Years
                        </text>
                    </div>
                    <div>
                        <text component='body'style={{color:"white", fontSize:'12px'}}>
                            {data['Total_Number_of_clients']} Clients
                        </text>
                    </div>
                     <div>
                        <text component='body'style={{color:"white", fontSize:'12px'}} >
                            Age (Avg): {data['Average_age']}
                        </text>
                    </div>
                    <div>
                        <text component='body'style={{color:"white", fontSize:'12px'}} >
                            Unit Cost (Avg): £ {data['Average_Unit_Cost']}/hour
                        </text>
                    </div>
                    <div>
                        <text component='body'style={{color:"white", fontSize:'12px'}} >
                            Most Expensive Client: £ {data['Max_Weekly_Cost']}/week
                        </text>
                    </div>
                    </g>
                </Box>);