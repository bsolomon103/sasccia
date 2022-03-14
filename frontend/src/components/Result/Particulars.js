import React from "react";
import { Container, Box, Button, Grid, Typography, TextField, 
FormHelperText, FormControl, RadioGroup, 
Radio, FormControlLabel, TableContainer, Table, TableBody,
TableRow, Paper, TableHead, TableCell} from "@material-ui/core";
export const ParticularsBoxx = ({data}) => {
    const particulars = data["Service Particulars"]
    //console.log(psr)
    
    return ( <div align='center' style={{display:'block', padding:30}}>
                
                <TableContainer component={Paper}>
                    <Table>
                        <TableHead style={{backgroundColor: "royalblue"}}>
                            <TableRow>
                                <TableCell>Provider Name</TableCell>
                                <TableCell>Delivery Mechanism</TableCell>
                                <TableCell>Service Component</TableCell>
                                <TableCell>Start Date</TableCell>
                                <TableCell>End Date</TableCell>
                                <TableCell>No of Visits (Weekly)</TableCell>
                                <TableCell>Cost (Weekly)</TableCell>
                                <TableCell>Unit Cost (Hourly)</TableCell>
                                <TableCell>Minutes Allocated (Weekly)</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {particulars.map(d => 
                                <TableRow key={d}>
                                    <TableCell>{d.serviceProvider__name}</TableCell>
                                    <TableCell>{d.deliveryMechanism__name}</TableCell>
                                    <TableCell>{d.serviceComponent__name}</TableCell>
                                    <TableCell>{d.serviceStart}</TableCell>
                                    <TableCell>{d.serviceEnd}</TableCell>
                                    <TableCell>{d.weeklyVisits}</TableCell>
                                    <TableCell>£{d.weeklyCost}</TableCell>
                                    <TableCell>£{d.unitCost}</TableCell>
                                    <TableCell>{d.weeklyMins}</TableCell>
                        </TableRow>
                                
                            )}
                        </TableBody>
                    </Table>
                </TableContainer>
                
    
            </div>
   
                );
        };
    
    
        