import React, { useState, useCallback, useEffect } from "react";
//import { SearchBar } from "..components/SearchBar";
import { scaleOrdinal, scaleBand, scaleLinear, max, extent, arc, pie, csv } from 'd3';
import ReactDOM from 'react-dom';
import { useData } from "../components/useData";
import { Psr } from "../components/Reasons/index.js";
import { Requests } from "../components/Requests/index.js";
import { RoutesOf } from "../components/RoutesOf/index.js";
import { Grid,Button } from "@material-ui/core";
import { Outcomes } from "../components/Outcomes/index.js";
import { Assessments} from "../components/AssessmentCompletion/index.js";
import { Delta } from "../components/DeltaAge/index.js";
import { LivingSituation} from "../components/LivingSituation/index.js";
import {TopProviders} from '../components/Providers/index.js';
import {HealthConditions} from "../components/HealthConditions/index.js";
import {DateHistogram} from "../components/Histogram/index.js";
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from "react-router-dom";
import {SearchFunction} from '../components/Search';
import {Layout} from '../hocs/layout';
import {Home} from '../containers/home';
import Login from '../containers/login';

export default function AllClientsPage (){
    const width = 1350;
    const height = 700;
    const scatter = {top: 30,
                    right:1100,
                    left: 60,
                    bottom: 35
    };
    const line = {top: 30,
                right:1000,
                left:215,
                bottom:35,
    };
    const yAxisLabelOffset = 30;
    const xAxisLabelOffset = 30;
    const reqinnerHeight = height * 0.45 - scatter.top - scatter.bottom - 50;
    const reqinnerWidth = width - scatter.left - scatter.right + 50;
    const psrinnerHeight = height * 0.45 - scatter.top - scatter.bottom - 90;
    const psrinnerWidth = width - scatter.left - scatter.right;
    const routeinnerHeight = height * 0.45 - line.top - line.bottom - 50;
    const routeinnerWidth = width - line.left - line.right;
    const assinnerHeight = height * 0.45 - line.top - line.bottom - 130;
    const assinnerWidth = width - line.left - line.right;
    const delinnerWidth = width - scatter.left - scatter.right;
    
   
 
    // ******************************************** STATES *********************************************************************
    //Set Ethnicity
    const initialethnicity = 'African';
    const [ethnicity, setEthnicity] = useState(initialethnicity);
    
    //Set Gender
    const initialGender = 'all';
    const [gender, setGender] = useState(initialGender);
    
    //Set Assessment Data
    const initialView = "routes";
    const [assessmentView, setAssessmentView] = useState(initialView);
    
    //Set Hovered Value
    const [hoveredValue, setHoveredValue] = useState(null);
    
    //Set Employment Type
    const initialEmployment = "Paid: 16 or more hours a week";
    const [employmentValue, setEmploymentValue] = useState(initialEmployment);
    
    //Set Living Hovered Value
    const [livHoveredValue, setLivHoveredValue] = useState(null);
    
    //Set Service Type
    const initialService = "Long Term Support: Community"
    const [serviceValue, setServiceValue] = useState(initialService);
    
    //Set ServiceHover Value
    const [serviceHover, setServiceHover] = useState(null);
    
    //Set Ethnicity
    const initialethnicity2 = 'African';
    const [ethnicity2, setEthnicity2] = useState(initialethnicity2);
    
    //Set HealthHover Value
    const [healthValue, setHealthValue] = useState(null);

    //Set Histogram Value
    const initialHistogramValue = 'requests'
    const [histogramValue, setHistogramValue] = useState(initialHistogramValue);
    
    //************************************************ DATA ******************************************************************
    const data = useData();
   
    
  
    if (!data){
        return <pre><b>Loading...</b></pre>;
    }
    const reasons = data['Primary Support Reason'];
    const requestCount = data['Request Count'];
    const routes = data['Routes Of Access'][ethnicity];
    const outcomes = data['Request Outcomes'][gender];
    const assessments = data['Assessment Completion'][assessmentView];
    const delta = data["Assessment Completion_Age_Eligibility"];
    const livingSituation = data['Living Situation'][employmentValue];
    const provider = data["Top Providers"][serviceValue];
    const healthProfile = data["Health Profile"][ethnicity2];
    const histo = data['Fix'][histogramValue];
    console.log(routes);
    
   
    
    //********************************************REQUEST OUTCOMES(COUNT)*********************************************************
    const oYValue = (d) => d.requestOutcome__name;
    const oXValue = (d) => d.count;
    
    const oYScale = scaleBand()
    .domain(outcomes.map(oYValue))
    .range([0, psrinnerHeight])
    .paddingInner(0.15);
    
    const oXScale = scaleLinear()
    .domain([0, max(outcomes, oXValue)])
    .range([0, psrinnerWidth])
    .nice();
    
    //******************************************* REQUESTS PER MONTH****************************************************************
    const reqxValue = (d) => d.requestStart__month;
    const reqyValue = (d) => d.count;
    const yAxisLabel = 'Count';
    const xAxisLabel = 'Month';
    
    const reqxScale = scaleLinear()
    .domain(extent(requestCount, reqxValue))
    .range([0, reqinnerWidth])
    .nice();
    
    const reqyScale = scaleLinear()
    .domain(extent(requestCount, reqyValue))
    .range([reqinnerHeight, 0])
    .nice();
    
    //*********************************************PRIMARY SUPPORT REASONS*********************************************************
    const yValue = (d) => d.primarySupportReason__name;
    const xValue = (d) => d.count;
 
    const yScale = scaleBand()
    .domain(reasons.map(yValue))
    .range([0, psrinnerHeight])
    .paddingInner(0.15);
  
    const xScale = scaleLinear()
    .domain([0, max(reasons, xValue)])
    .range([0, psrinnerWidth])
    .nice();
    
    //**********************************************ROUTES OF ACCESS (COUNT)********************************************************
    const routeXValue = (d) => d.reqcount;
    const routeYValue = (d) => d.routeOfAccess__name;

    const routeYScale = scaleBand()
    .domain(routes.map(routeYValue))
    .range([0, assinnerHeight])
    .paddingInner(0);
    
    const routeXScale = scaleLinear()
    .domain([0, max(routes, routeXValue)])
    .range([0, assinnerWidth])
    .nice();
    console.log(routeYScale.domain());
    
    //***********************************************ASSESSMENT COMPLETION TIMES(MEAN)***********************************************
    const assXValue = (d) => d.delta;
    const assYValue = (d) => d.category;
    
    const assYScale = scaleBand()
    .domain(assessments.map(assYValue))
    .range([0, assinnerHeight])
    .paddingInner(0);
    
    const assXScale = scaleLinear()
    .domain([0, max(assessments, assXValue)])
    .range([0, assinnerWidth])
    .nice();
    
    //****************************************************ASSESSMENT COMPLETION BY AGE********************************************** 
    const delxValue = (d) => d.age;
    const delyValue = (d) => d.delta;
    const colorValue = (d) => d.eligibility;
    
    const delxAxisLabel = 'Age';
    const delyAxisLabel = 'Days';
    const delColorValueLabel = 'Outcome';
    
    const filteredData = delta.filter(d => hoveredValue === colorValue(d));
    
    const delxScale = scaleLinear()
    .domain([10, 110])
    .range([0, reqinnerWidth]);
    
    const delyScale = scaleLinear()
    .domain([0,20])
    .range([reqinnerHeight,0]);
    
    const delcolorScale = scaleOrdinal()
    .domain(delta.map(colorValue))
    .range(['#4169e1','#ff6347']);
 //*****************************************************PIE CHART 1********************************************************************
   const count = (d) => d.count;
   const livingColorValue = (d) => d.accommodationStatus__name;
   const livFilteredData = livingSituation.filter(d => livHoveredValue === livingColorValue(d));
   
   const livingColorScale = scaleOrdinal()
   .domain(livingSituation.map(livingColorValue))
   .range(['#4daf4a','#377eb8','#ff7f00','#984ea3','#e41a1c','#000000',
            '#c0c0c0','#808080','#ffffff','#800000','#ff0000','#800080',
            '#ff00ff','#008000','#00ff00','#808000','#ffff00','#000080',
            '#0000ff','#008080','#00ffff','#ffa500','#f0f8ff','#faebd7',
            '#7fffd4','#f0ffff','#f5f5dc','#ffe4c4','#ffebcd']);
    
    const livingColorScale2 = scaleOrdinal()
   .domain(livingSituation.map(livingColorValue))
   .range(['#4daf4a','#377eb8']);
    
 //***************************************************PIE CHART 2***********************************************************************
 const provCount = (d) => d.count;
 const provColorValue = (d) => d.serviceProvider__name;
 const provFilteredData = provider.filter(d => serviceHover === provColorValue(d));
 
 const provColorScale = scaleOrdinal()
 .domain(provider.map(provColorValue))
 .range(['#4daf4a','#377eb8','#ff7f00','#984ea3','#e41a1c','#000000',
            '#c0c0c0','#808080','#ffffff','#800000','#ff0000','#800080',
            '#ff00ff','#008000','#00ff00','#808000','#ffff00','#000080',
            '#0000ff','#008080','#00ffff','#ffa500','#f0f8ff','#faebd7',
            '#7fffd4','#f0ffff','#f5f5dc','#ffe4c4','#ffebcd']);
            
   
 //**************************************************PIE CHART 3****************************************************************************
 const healthCount = (d) => d.count;
 const healthColorValue = (d) => d.health_condition;
 const healthFilteredData = healthProfile.filter(d => healthValue === healthColorValue(d));
 
 const healthColorScale = scaleOrdinal()
 .domain(healthProfile.map(healthColorValue))
 .range(['#4daf4a','#377eb8','#ff7f00','#984ea3','#e41a1c','#000000',
            '#c0c0c0','#808080','#ffffff','#800000','#ff0000','#800080',
            '#ff00ff','#008000','#00ff00','#808000','#ffff00','#000080',
            '#0000ff','#008080','#00ffff','#ffa500','#f0f8ff','#faebd7',
            '#7fffd4','#f0ffff','#f5f5dc','#ffe4c4','#ffebcd','#8a2be2',
            '#a52a2a','#deb887','#5f9ea0','#7fff00','#d2691e','#ff7f50',
            '#6495ed','#fff8dc','#dc143c','#00ffff','#00008b','#008b8b',
            '#b8860b','#a9a9a9','#006400','#a9a9a9','#bdb76b','#8b008b'
]);

//****************************************************HISTOGRAM***************************************************************************************
const hXValue = (d) => new Date(d['requestStart']);
const hAxisLabel = 'Reported Date';

//**************************************************ATTTRIBUTES***********************************************************************************
const livingAttributes = [
        {value:"Not in Paid Employment (not actively seeking work / retired)", label:"Not in Paid Employment (not seeking)"},
        {value:"Not in Paid Employment (seeking work)", label:"Not in Paid Employment (seeking)"},
        {value:"Paid: 16 or more hours a week", label:"Paid: 16 or more hours a week"},
        {value:"Paid: Less than 16 hours a week", label:"Paid: Less than 16 hours a week"},
        {value:"Unknown",label:"Unknown"}
        ];

    return (
    <div className = 'scrollable'>
                <h1 align='center'>SUMMARY PAGE</h1>
                <g className='grid'>
                    <Grid container columnSpacing={6} rowSpacing={2}>
                    <Grid item xl={2} lg={3} md={6} sm={8} xs={12}>
                        <Outcomes 
                            width={width} 
                            height={height} 
                            margin={scatter}
                            innerHeight={psrinnerHeight}
                            innerWidth={psrinnerWidth}
                            xScale={oXScale}
                            yScale={oYScale}
                            data={outcomes}
                            xValue={oXValue}
                            yValue={oYValue}
                            initialGender={initialGender}
                            setGender={setGender}
                            />
                    </Grid>
                    <Grid item xl={2} lg={3} md={6} sm={8} xs={12}> 
                    <Requests
                        width={reqinnerWidth+70}
                        height={reqinnerHeight+70}
                        margin={scatter}
                        xScale={reqxScale}
                        innerHeight={reqinnerHeight}
                        innerWidth={reqinnerWidth}
                        yAxisLabelOffset={yAxisLabelOffset}
                        yAxisLabel={yAxisLabel}
                        xAxisLabel={xAxisLabel}
                        yScale={reqyScale}
                        data={requestCount}
                        xValue={reqxValue}
                        yValue={reqyValue}
                    />
                    </Grid>
                    
                    <Grid item xl={2} lg={3} md={6} sm={8} xs={12}>
                            <Psr 
                                width={width} 
                                height={height} 
                                margin={scatter}
                                innerHeight={psrinnerHeight}
                                innerWidth={psrinnerWidth}
                                xScale={xScale}
                                yScale={yScale}
                                data={reasons}
                                xValue={xValue}
                                yValue={yValue}
                            />
                    </Grid>   
                  
                    <Grid item>
                      <RoutesOf
                        width={width} 
                        height={height} 
                        margin={scatter}
                        innerHeight={assinnerHeight}
                        innerWidth={assinnerWidth}
                        xScale={routeXScale}
                        yScale={routeYScale}
                        data={routes}
                        xValue={routeXValue}
                        yValue={routeYValue}
                        initialethnicity={initialethnicity}
                        setEthnicity={setEthnicity}
                    />
                    </Grid>
                    
                    <Grid item xl={2} lg={3} md={6} sm={8} xs={12}>
                      <Assessments
                        width={width}
                        height={height}
                        margin={scatter}
                        xScale={assXScale}
                        yScale={assYScale}
                        innerWidth={assinnerWidth}
                        innerHeight={assinnerHeight}
                        data={assessments}
                        xValue={assXValue}
                        yValue={assYValue}
                        initialView={initialView}
                        setAssessmentView={setAssessmentView}
                    />
                    </Grid>
                    <Grid item xl={2} lg={3} md={6} sm={8} xs={12}>
                        <LivingSituation
                            data={livingSituation}
                            margin={line}
                            height={200}
                            employmentValue={employmentValue}
                            setEmploymentValue={setEmploymentValue}
                            colorScale={livingColorScale}
                            colorValue={livingColorValue}
                            colorLegendLabel='Accommodation'
                            circleRadius={6}
                            filteredData={livFilteredData}
                            setHoveredValue={setLivHoveredValue}
                            hoveredValue={livHoveredValue}
                            xValue={count}
                            innerWidth={assinnerWidth}
                        />
                    </Grid>
                    <Grid item xl={2} lg={3} md={6} sm={8} xs={12}> 
                    <Delta
                        width={width}
                        height={reqinnerHeight+60}
                        margin={scatter}
                        xScale={delxScale}
                        innerHeight={reqinnerHeight}
                        innerWidth={reqinnerWidth}
                        yAxisLabelOffset={yAxisLabelOffset}
                        yAxisLabel={delyAxisLabel}
                        xAxisLabel={delxAxisLabel}
                        yScale={delyScale}
                        data={delta}
                        filteredData={filteredData}
                        xValue={delxValue}
                        yValue={delyValue}
                        colorValue={colorValue}
                        colorScale={delcolorScale}
                        colorLegendLabel ={delColorValueLabel}
                        hoveredValue={hoveredValue}
                        setHoveredValue={setHoveredValue}
                        circleRadius={6}
                    />
                    </Grid>
                    <Grid item>
                        <TopProviders
                            data={provider}
                            margin={line}
                            height={200}
                            serviceValue={serviceValue}
                            setServiceValue={setServiceValue}
                            colorScale={provColorScale}
                            colorValue={provColorValue}
                            colorLegendLabel='Top Providers'
                            circleRadius={6}
                            filteredData={provFilteredData}
                            setHoveredValue={setServiceHover}
                            hoveredValue={serviceHover}
                            xValue={count}
                            innerWidth={assinnerWidth}
                        />
                    </Grid>
                    
                    <Grid item xl={2} lg={3} md={6} sm={8} xs={12}>
                        <HealthConditions
                            data={healthProfile}
                            margin={line}
                            height={200}
                            initialethnicity={initialethnicity2}
                            setEthnicity={setEthnicity2}
                            colorScale={healthColorScale}
                            colorValue={healthColorValue}
                            colorLegendLabel='Health Conditions'
                            circleRadius={6}
                            filteredData={healthFilteredData}
                            setHoveredValue={setHealthValue}
                            hoveredValue={healthValue}
                            xValue={count}
                            innerWidth={assinnerWidth}
                        />
                    </Grid >
                    
                    <Grid item>
                        <DateHistogram 
                            data={histo}
                            xValue={hXValue}
                            xAxisLabel={hAxisLabel}
                            histogramValue={histogramValue}
                            setHistogramValue={setHistogramValue}
                        />
                    </Grid>
        
                   </Grid> 
                </g>
            </div>
        );
    }
    
  
   


