import React from "react";
import { AxisBottom } from  "./AxisBottom";
import { AxisLeft } from  "./AxisLeft";
import { Marks } from "./Marks";

export const Requests = ({
    width,
    height,
    margin,
    xScale,
    innerHeight,
    innerWidth,
    yAxisLabelOffset,
    yAxisLabel,
    xAxisLabel,
    yScale,
    data,
    xValue,
    yValue
}) => (
    <svg width={width}height={height}>
                    <g transform={`translate(${margin.left},${margin.top+10})`}>
                        <AxisBottom xScaleScatter={xScale} scatterinnerHeight={innerHeight} tickOffset={5}/>
                        
                        <text className='axis-label' textAnchor='middle'
                        transform={`translate(${-yAxisLabelOffset} ${innerHeight/2}) rotate(-90)`}
                        style={{textAnchor:'middle',fontSize:'8.5px', fontWeight:'700'}}
                        >
                            {yAxisLabel}
                        </text>
                        
                        <AxisLeft yScaleScatter={yScale} scatterinnerWidth={innerWidth}/>
                        <text className='axis-label' x={innerWidth/2} y={innerHeight+20}
                        style={{textAnchor:'middle',fontSize:'8.5px', fontWeight:'700'}} tickOffset={5}>
                            {xAxisLabel}
                        </text>
                        
                        <text className='axis-label' x={innerWidth/2 - 10} y={innerHeight - 213}
                        textAnchor='middle' style={{fontSize:'9.0px', fontWeight:'700'}}>
                            REQUESTS PER MONTH
                        </text>
                        <Marks
                            data={data}
                            xScaleScatter={xScale}
                            yScaleScatter={yScale}
                            xValueScatter={xValue}
                            yValueScatter={yValue}
                            circleRadius={2.5}
                        />
                    </g>
    </svg>
 )
