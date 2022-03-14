import React from 'react';
import {arc, pie} from 'd3';
import {Dropdown} from './Dropdown';
import {ColorLegend} from './ColorLegend';



const attributes = [
    {value:"African", label:'African'},
    {value:'White British', label:'White British'},
    {value:'Other Asian', label:'Any Other Asian'},
    {value:'Other Ethnicity', label:'Any Other'},
    {value:"White Irish", label:'White Irish'},
    {value:'Other White', label:'Any Other White'},
    {value:"Bangladeshi", label:'Bangladeshi'},
    {value:"White and Black African", label:'Black/White - African'},
    {value:"White and Black Caribbean", label:'Black/White - Caribbean'},
    {value:"Caribbean", label:'Caribbean'},
    {value:"Indian", label:'Indian'},
    {value:'Other Mixed', label:'Mixed'},
    {value:"Pakistani", label:'Pakistani'},
    {value:"Refused", label:'Refused'},
    {value:'Unknown/Undeclared', label:'Undeclared'}, 
    //{value:'Any other Black', label:'Any Other Black'},
    //{value:'White Gypsy', label:'White Gypsy'}, 
    //{value:"Arab", label:'Arab'},
    //{value:"Chinese", label:'Chinese'},
    ];


export const HealthConditions = ({
data,
xValue,
height, 
margin,
initialethnicity,
setEthnicity,
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
                    selectedValue={initialethnicity}
                    onSelectedValueChange={setEthnicity}
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
                HEALTH PROFILE (COUNT)
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
                        fill={colorScale(d.data["health_condition"])}
                        d={pieArc(d)}
                        >
                
                        <title>{d.data['count']}</title>
                    </path>
                    ))} 
                </g>
            </svg>
            </>
         )};
    
   
    