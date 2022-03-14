import React from "react";

export const AxisLeft = ({yScale}) => 
         yScale.domain().map(tickValue => (
            <g className="tick">
                <text key={tickValue} style={{textAnchor:'end', fontSize:'8.0px'}} x={-3} 
                    y={yScale(tickValue) + yScale.bandwidth()/2.78}>
                    {tickValue}
                </text>
            </g>    
                ))
            