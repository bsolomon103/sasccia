import React, {Fragment} from 'react';
import NavBar from '../components/navbar';

export const Layout = ({ children }) =>  {
        return (<Fragment>
                    <NavBar />
                    {children}
                </Fragment>
                
        );
    };
    