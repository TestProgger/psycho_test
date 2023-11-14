import { FC } from "react";
import './Modal.scss'
import { useNavigate } from "react-router-dom";

interface IModal{
    isVisible ?: boolean
    title ?: string | null
}
const Modal: FC<IModal> = ({isVisible = false, title = ''}) => {
    const navigate = useNavigate()
    return(
        <div className={isVisible ? "block-modal active" : "block-modal"}>
            <div className="block-modal-content">
                <div className="text">Ваш результат</div>
                <div className="title">{title}</div>
                <div className="return-btn" onClick={() => navigate('/tests')}>
                    Вернуться на главную
                </div>
            </div>
        </div>
    )
}


export default Modal

