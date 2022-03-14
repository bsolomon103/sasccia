import React from "react";
export const AxisBottom = ({xScale,innerHeight}) => 
        xScale.ticks().map(tickValue => (
            <g className="tick" key={tickValue} transform={`translate(${xScale(tickValue)},0)`}>
                <text style={{textAnchor:'middle', fontSize:'6px'}} y={innerHeight+10}>{tickValue}days</text>
            </g>
                        ));