import React from "react";
import { AxisBottom } from "./AxisBottom";
import { AxisLeft } from "./AxisLeft";
import { Marks } from "./Marks";
import { Dropdown } from "./Dropdown";


const attributes = [
        {value:'Male', label:'Male'},
        {value:'Female', label:'Female'},
        {value:'Unknown', label:'Unknown'},
        {value:'all', label:'All Genders'}
        ];
        
export const Outcomes = ({
    width, 
    height,
    margin,
    xScale,
    yScale,
    innerWidth,
    innerHeight,
    data,
    xValue,
    yValue, 
    //attributes,
    initialGender,
    setGender
    
    
    
}) => ( 
        <>
        <div className='dropdown'>
        <label for='y-select'>Gender</label>
        <Dropdown
            options={attributes}
            id="y-select"
            selectedValue={initialGender}
            onSelectedValueChange={setGender}
        />
        </div>
        <svg>
            <g transform={`translate(${margin.left+180}, ${margin.top+10})`}>
            <AxisBottom xScale={xScale} innerHeight={innerHeight} tickFormat={`%`}/> 
            <AxisLeft yScale={yScale}/>
            <text className="axis-label" x={innerWidth/2 - 60} y={innerHeight-180} style={{textAnchor:"end", fontSize:'9.0px',
                fontWeight:'700'
                }}
            >
                REQUEST OUTCOMES (COUNT)
            </text>
            <Marks data={data} yScale={yScale} xScale={xScale} yValue={yValue} xValue={xValue}/>  
            </g>
        </svg>
        </>
    
    );