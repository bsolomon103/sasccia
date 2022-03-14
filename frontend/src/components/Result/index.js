import React, {useState, useEffect} from 'react';
import {useParams, useNavigate} from 'react-router-dom';
import fetch from 'node-fetch';
import {Grid, Button, Typography} from '@material-ui/core';
import {Boxx} from './DemoBox.js';
import {RatioBoxx} from './RatioBox.js';
import {ReqBoxx} from './RequestBox.js';
import {SupportBoxx} from './Psr.js';
import {HealthBoxx} from './HealthConditions.js';
import {ParticularsBoxx} from  './Particulars.js';
import {AssBoxx} from './AssessmentBox.js';
import {DeceasedBoxx} from './Status.js'

export const Result = ({data}) => {  
    
    return (
        <div>
            <Grid container columnSpacing={6} rowSpacing={12}>
                <Grid item xl={2} lg={3} md={6} sm={8} xs={12}>
                <Boxx 
                    data={data}
                />
                </Grid>
                <Grid item xl={2} lg={3} md={6} sm={8} xs={12}>
                <RatioBoxx 
                    data={data}
                />
                </Grid>
                <Grid item xl={2} lg={3} md={6} sm={8} xs={12}>
                <ReqBoxx 
                    data={data}
                />
                </Grid>
                <Grid item xl={2} lg={3} md={6} sm={8} xs={12}>
                <SupportBoxx 
                    data={data}
                />
                </Grid>
                <Grid item xl={2} lg={3} md={6} sm={8} xs={12}>
                <HealthBoxx 
                    data={data}
                />
                </Grid>
                <Grid item xl={2} lg={3} md={6} sm={8} xs={12}>
                <AssBoxx 
                    data={data}
                />
                </Grid>
                <Grid item xl={2} lg={3} md={6} sm={8} xs={12}>
                <DeceasedBoxx
                    data={data}
                />
                </Grid>
                <Grid item xl={12} lg={12} md={12} sm={12} xs={4}>
                <ParticularsBoxx 
                    data={data}
                />
                </Grid>
             </Grid>
        </div>
        
    );
    
};
