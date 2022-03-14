import React from 'react';
import {arc, pie} from 'd3';
import {Dropdown} from './Dropdown';
import {ColorLegend} from './ColorLegend';



const attributes = [
        {value:"Not in Paid Employment (not actively seeking work / retired)", label:"Not in Paid Employment (not seeking)"},
        {value:"Not in Paid Employment (seeking work)", label:"Not in Paid Employment (seeking)"},
        {value:"Paid: 16 or more hours a week", label:"Paid: 16 or more hours a week"},
        {value:"Paid: Less than 16 hours a week", label:"Paid: Less than 16 hours a week"},
        {value:"Unknown",label:"Unknown"}
        ];

export const LivingSituation = ({
data,
xValue,
height, 
margin,
employmentValue, 
setEmploymentValue,
colorScale,
colorScale2,
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
                    selectedValue={employmentValue}
                    onSelectedValueChange={setEmploymentValue}
                />
            </div>
            
            <svg height={height}>
             <g transform={`translate(${margin.left-100},${margin.top - 5})`}>
            <text className="axis-label" 
                   x={innerWidth/2 + 30} 
                   y={innerHeight-130} 
                   style={{textAnchor:"end", fontSize:'9.0px',
                fontWeight:'700'
                }}>
                LD CLIENTS - WORK AND LIVING 
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
                        {colorPie(data).map((d,i) => (
                    <path 
                        fill={colorScale(d.data['accommodationStatus__name'])}
                        d={pieArc(d)}>
                      
                        
                        
                        <title>{d.data['percentage'].toFixed(2)}%</title>
                    </path>))
                        }
                </g>
            </svg>
            </>
         )};
    
   
    