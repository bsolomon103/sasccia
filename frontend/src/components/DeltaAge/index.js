import React from "react";
import { AxisBottom } from  "./AxisBottom";
import { AxisLeft } from  "./AxisLeft";
import { Marks } from "./Marks";
import { ColorLegend } from "./ColorLegend";

export const Delta = ({
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
    yValue,
    colorValue,
    colorScale, 
    colorLegendLabel,
    hoveredValue,
    setHoveredValue,
    circleRadius, 
    filteredData
}) => (
    <svg width={width}height={height}>
                    <g transform={`translate(${margin.left-20},${margin.top+5})`}>
                        <AxisBottom xScale={xScale} innerHeight={innerHeight} tickOffset={5}/>
                        
                        <text className='axis-label' textAnchor='middle'
                        transform={`translate(${-yAxisLabelOffset+10} ${innerHeight/2}) rotate(-90)`}
                        style={{textAnchor:'middle',fontSize:'8.5px', fontWeight:'700'}}
                        >
                            {yAxisLabel}
                        </text>
                        
                        <AxisLeft yScale={yScale} innerWidth={innerWidth}/>
                        <text className='axis-label' x={innerWidth/2} y={innerHeight+20}
                        style={{textAnchor:'middle',fontSize:'8.5px', fontWeight:'700'}} tickOffset={5}>
                            {xAxisLabel}
                        </text>
                        
                        <text className='axis-label' x={innerWidth/2} y={innerHeight - 213}
                        textAnchor='middle' style={{fontSize:'9.0px', fontWeight:'700'}}>
                            ASSESSMENT COMPLETION BY AGE
                        </text>
                        <g transform={`translate(${innerWidth+10},60)`}>
                            <text 
                                x={30}
                                y={-15}
                                className='axis-label'
                                textAnchor='middle'
                                tickOffset={5}
                                style={{fontSize:'11.0px'}}
                            >
                                {colorLegendLabel}
                            </text>
                            <ColorLegend 
                                colorScale={colorScale}
                                tickSpacing={15}
                                tickSize={circleRadius/2}
                                tickTextOffset={20}
                                onHover={setHoveredValue}
                                hoveredValue={hoveredValue}
                            />
                        </g>
                        <g opacity={hoveredValue ? 0.25 : 1}>
                        <Marks
                            data={data}
                            xScale={xScale}
                            yScale={yScale}
                            xValue={xValue}
                            yValue={yValue}
                            circleRadius={2.5}
                            colorScale={colorScale}
                            colorValue={colorValue}
                        />
                        </g>
                        <Marks
                            data={filteredData}
                            xScale={xScale}
                            yScale={yScale}
                            xValue={xValue}
                            yValue={yValue}
                            circleRadius={2.5}
                            colorScale={colorScale}
                            colorValue={colorValue}
                        />
                      
                    </g>
    </svg>
 )
