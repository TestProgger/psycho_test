import { FC } from "react";
import './TestCard.scss'
import { Arrow } from "@icons/Arrow";

export interface ITestCard{
    test_id: string,
    name: string,
    description: string,
    questions_count: number,
    onStartTestClick: (test_id: string) => void
}
export const TestCard: FC<ITestCard> = ({test_id, name, description, questions_count, onStartTestClick}) => {
    return (
        <div className="block-test-card">
            <div className="block-test-card-head">
                <div className="block-test-card-name">
                    {name}
                </div>
                <div className="block-test-card-description">
                    {description}
                </div>
            </div>
            
            <div className="block-test-card-footer">
                <div className="block-test-card-questions">
                    <div className="block-test-card-questions-text">
                        Количесвтво вопросов:
                    </div>
                    <div className="block-test-card-questions-count">
                        {questions_count}
                    </div>
                </div>

                <div className="block-test-card-start-test">
                    <div className="block-test-card-start-test-btn"onClick={() => onStartTestClick(test_id)}>
                            <div className="block-test-card-start-test-btn-text">
                                Пройти тест
                            </div>
                            <div className="block-test-card-start-test-btn-icon">
                                <Arrow width={24} height={24} />
                            </div>
                        </div> 
                </div>
            </div>
            
        </div>
    )
}