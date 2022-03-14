import React from "react";

export const AxisLeft = ({yScaleScatter, scatterinnerWidth, tickOffset=3}) => 
    yScaleScatter.ticks().map(tickValue => (
        <g className='tick' transform={`translate(0,${yScaleScatter(tickValue)})`}>
            <line x2={scatterinnerWidth}/>
            <text 
                key={tickValue}
                style={{textAnchor:'end', fontSize:'8px'}}
                x={-tickOffset}
                y={-1}
                dy='0.71em'
                >
            {tickValue}
            </text>
        </g>
        ));