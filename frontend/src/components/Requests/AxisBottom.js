import React from "react";
export const AxisBottom = ({xScaleScatter, scatterinnerHeight, tickOffset=3}) => 
    xScaleScatter.ticks().map(tickValue => (
        <g className='tick' key={tickValue} transform={`translate(${xScaleScatter(tickValue)},0)`}>
            <line y2={scatterinnerHeight} />
            <text style={{textAnchor:'middle',fontSize:'8.5px'}} dy='.71em' y={scatterinnerHeight + tickOffset}>
                {tickValue}
            </text>
        </g>
        
        ))