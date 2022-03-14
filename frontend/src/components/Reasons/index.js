import React from "react";
import { AxisBottom } from "./AxisBottom";
import { AxisLeft } from "./AxisLeft";
import { Marks } from "./Marks";


export const Psr = ({
    width, 
    height,
    margin,
    xScale,
    yScale,
    innerWidth,
    innerHeight,
    data,
    xValue,
    yValue
    
    
}) => (
        <svg>
                    <g transform={`translate(${margin.left+130}, ${margin.top})`}>
                    <AxisBottom xScale={xScale} innerHeight={innerHeight} tickFormat={`%`}/> 
                    <AxisLeft yScale={yScale}/>
                    <text className="axis-label" x={innerWidth/2} y={innerHeight-170} style={{textAnchor:"end", fontSize:'9.0px',
                        fontWeight:'700'
                    }}
                    >
                        PRIMARY SUPPORT REASONS
                    </text>
                    <Marks data={data} yScale={yScale} xScale={xScale} yValue={yValue} xValue={xValue}/>  
                    </g>
                </svg>
    
    )