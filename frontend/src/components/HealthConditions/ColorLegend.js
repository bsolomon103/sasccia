import React from 'react';


export const ColorLegend = ({
    colorScale, 
    tickSpacing=10,
    tickSize=15,
    tickTextOffset=4,
    onHover,
    hoveredValue
}) => colorScale.domain().map((domainValue,i ) => (
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
        fontSize='8px'
    >
    {domainValue}
    </text>
    </g>
    ))