import React from 'react';
import {arc, pie} from 'd3';
import {Dropdown} from './Dropdown';
import {ColorLegend} from './ColorLegend';



const attributes = [
    {value:"Long Term Support: Community", label:"Long Term Support: Community"},
    {value:"Long Term Support: Nursing Care", label:"Long Term Support: Nursing Care"},
    {value:"Long Term Support: Residential Care", label:"Long Term Support: Residential Care"},
    {value:"Short Term Support: Other Short Term", label:"Short Term Support: Other Short Term"},
    {value:"Short Term Support: ST-Max", label:"Short Term Support: ST-Max"}
        ];

export const TopProviders = ({
data,
xValue,
height, 
margin,
serviceValue, 
setServiceValue,
colorScale,
colorValue,
innerWidth,
innerHeight,
colorLegendLabel,
circleRadius,
setHoveredValue,
hoveredValue,
filteredData
}) => {
    const pieArc = arc().innerRadius(50).outerRadius(65);
    const colorPie = pie().value(d => d.count);

    
    return ( 
            <>
            <div className='dropdown'>
                <label for='y-select'>Filter By</label>
                <Dropdown
                    options={attributes}
                    id="y-select"
                    selectedValue={serviceValue}
                    onSelectedValueChange={setServiceValue}
                />
            </div>
            
            <svg height={height}>
            <g transform={`translate(${margin.left-105},${margin.top - 5})`}>
            <text className="axis-label" 
                   x={innerWidth/2 + 30} 
                   y={innerHeight-130} 
                   style={{textAnchor:"end", fontSize:'9.0px',
                fontWeight:'700'
                }}>
                TOP PROVIDERS BY SERVICE TYPE
            </text> 
            </g>
               
                <g transform={`translate(${innerWidth+70},${margin.top+35})`}>
                            <text 
                                x={30}
                                y={-15}
                                className='axis-label'
                                textAnchor='middle'
                                tickOffset={5}
                                style={{fontSize:'9.0px'}}
                            >
                                {colorLegendLabel}
                            </text>
                            <ColorLegend 
                                colorScale={colorScale}
                                tickSpacing={10}
                                tickSize={circleRadius/2}
                                tickTextOffset={20}
                                onHover={setHoveredValue}
                                hoveredValue={hoveredValue}
                            />
                </g>
                <g 
                height={height-30} transform={`translate(${margin.left-80},${margin.top+70})`}>
                        {colorPie(data).map(d => (
                    <path 
                        fill={colorScale(d.data["serviceProvider__name"])}
                        d={pieArc(d)}>
                        <title>{`${d.data["serviceComponent__name"]} - ${d.data['count']}`}</title>
                        <title>{}</title>
                    </path>))}
                </g>
                
            </svg>
            </>
         )};
    
   
    