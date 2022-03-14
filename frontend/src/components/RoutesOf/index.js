import React, { useState } from "react";
import { AxisBottom } from "./AxisBottom";
import { AxisLeft } from "./AxisLeft";
import { Marks } from "./Marks";
import { Dropdown } from "./Dropdown";



const attributes = [
    {value:"African", label:'African'},
    {value:'Other Ethnicity', label:'Any Other'},
    {value:'Other Asian', label:'Any Other Asian'},
    {value:'Any other Black', label:'Any Other Black'},
    {value:'Other White', label:'Any Other White'},
    {value:"Arab", label:'Arab'},
    {value:"Bangladeshi", label:'Bangladeshi'},
    {value:"White and Black African", label:'Black/White - African'},
    {value:"White and Black Caribbean", label:'Black/White - Caribbean'},
    {value:"Caribbean", label:'Caribbean'},
    {value:"Chinese", label:'Chinese'},
    {value:"Indian", label:'Indian'},
    {value:'Other Mixed', label:'Mixed'},
    {value:"Pakistani", label:'Pakistani'},
    {value:"Refused", label:'Refused'},
    {value:'Unknown/Undeclared', label:'Undeclared'}, 
    {value:"White and Asian", label:'White/Asian'},
    {value:'White British', label:'White British'},
    {value:'White Gypsy', label:'White Gypsy'}, 
    {value:"White Irish", label:'White Irish'},
    ];

    
export const RoutesOf = ({
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
   // attributes,
    initialethnicity, 
    setEthnicity
  
    
}) => (
       <>
       <div className='dropdown'>
       <label for='y-select'>Ethnicity</label>
       <Dropdown
        options={attributes}
        id="x-select"
        selectedValue={initialethnicity}
        onSelectedValueChange={setEthnicity}
       />
       </div>
        <svg>
            <g transform={`translate(${margin.left+70}, ${margin.top})`}>
            <AxisBottom xScale={xScale} innerHeight={innerHeight} tickFormat={''}/> 
            <AxisLeft yScale={yScale}/>
            <text className="axis-label" x={innerWidth/2+ 25} y={innerHeight-130} style={{textAnchor:"end", fontSize:'9.0px',
            fontWeight:'700'}}
            >
                ROUTES OF ACCESS (COUNT)
            </text>
            <Marks data={data} yScale={yScale} xScale={xScale} yValue={yValue} xValue={xValue}/>  
            </g>
        </svg>
        </>
    
    )