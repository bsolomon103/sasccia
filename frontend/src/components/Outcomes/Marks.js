import React from "react";

export const Marks = ({data, yScale, xScale, yValue, xValue}) => 
            data.map(d => 
            <g className="mark" >
                <rect 
                    y= {yScale(yValue(d))}
                    width={xScale(xValue(d))}
                    height={yScale.bandwidth()/2}
                    
                >
                <title>{xValue(d)}</title>
                
                </rect>
            </g>  
        
            );