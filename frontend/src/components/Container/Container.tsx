import {FC, ReactNode} from 'react';
import './Container.scss';

// @ts-ignore
export const Container: FC<{children: ReactNode}> = ({children}) => {
    return (
        <div className="block-container">
            {children}
        </div>
    )
}