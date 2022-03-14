import React from "react";

export const AxisLeft = ({yScale}) => 
         yScale.domain().map(tickValue => (
            <g className="tick">
                <text key={tickValue} style={{textAnchor:'end', fontSize:'8.5px'}} x={-3} 
                    y={yScale(tickValue) + yScale.bandwidth()/3}>
                    {tickValue}
                </text>
            </g>    
                ))