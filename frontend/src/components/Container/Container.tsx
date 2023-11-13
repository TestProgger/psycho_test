import {FC} from 'react';
import './Container.scss';


export const Container: FC = ({children}) => {
    return (
        <div className="block-container">
            {children}
        </div>
    )
}