import React from "react";
import { AxisBottom } from "./AxisBottom";
import { AxisLeft } from "./AxisLeft";
import { Marks } from "./Marks";
import {Dropdown} from "./Dropdown";



const attributes = [
        {value:'routes', label:'Routes Of Access'},
        {value:'ethnicities', label:'Ethnicity'},
        {value:'reasons', label:'Primary Support Reason'}
    
        ];
export const Assessments = ({
    width, 
    height,
    margin,
    xScale,
    yScale,
    xValue,
    yValue,
    innerWidth,
    innerHeight,
    data,
    initialView,
    setAssessmentView
}) => ( 
        <>
        <div className='dropdown'>
        <label for='y-select'>Filter By</label>
        <Dropdown
            options={attributes}
            id="y-select"
            selectedValue={initialView}
            onSelectedValueChange={setAssessmentView}
        />
        </div>
        <svg>
            <g transform={`translate(${margin.left+155}, ${margin.top})`}>
            <AxisBottom xScale={xScale} innerHeight={innerHeight} tickFormat={`%`}/> 
            <AxisLeft yScale={yScale}/>
            <text className="axis-label" x={innerWidth/2 - 30} y={innerHeight-130} style={{textAnchor:"end", fontSize:'9.0px',
                fontWeight:'700'
                }}
            >
                ASSESSMENT COMPLETION TIMES (MEAN)
            </text>
            <Marks data={data} yScale={yScale} xScale={xScale} yValue={yValue} xValue={xValue}/>  
            </g>
        </svg>
        </>
    
    );