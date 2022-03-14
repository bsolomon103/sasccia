import React from "react";

export const ColorLegend = ({
    colorScale,
    tickSpacing=20,
    tickSize=10,
    tickTextOffset=20,
    onHover,
    hoveredValue
}) => colorScale.domain().map((domainValue,i) =>(
    <g
        className='tick'
        transform={`translate(0,${i * tickSpacing})`}
        onMouseEnter={() => {onHover(domainValue)}}
        onMouseOut={() => {onHover(null)}}
        opacity={hoveredValue && domainValue !== hoveredValue ? 0.5 : 1}
    >
    <circle 
        fill={colorScale(domainValue)}
        r={tickSize}
    />
    <text
        x={tickTextOffset/4}
        dy='0.32em'
        fontSize='10px'
    >{domainValue}
    </text>
    </g>
    ))