import { IAnswer } from "@/types/services/question";
import { FC, useEffect, useState } from "react";
import './QuestionCard.scss'

export interface IQuestionCard{
    question_id: string
    index: number
    title: string
    answers: IAnswer[]
    onAnswerClick: (question_id: string, answer_id: string) => void
}
export const QuestionCard: FC<IQuestionCard> = ({question_id, index, title, answers, onAnswerClick}) => {
    const [checkedAnswer, setCheckedAnswer] = useState<string|null>()

    useEffect(()=>{
        for(const answer of answers){
            console.log(answer, checkedAnswer)
            if(answer.is_checked && !checkedAnswer){
                setCheckedAnswer(answer.id);
                break
            }
        }
    }, [])

    const handleAnswerClick = (answer_id: string) => {
        setCheckedAnswer(answer_id)
        onAnswerClick(question_id, answer_id)
    }

    return(
        <div className="block-question-card">
            <div className="block-question-card-title">
                <div className="block-question-card-title-index">
                    {`${index}.`}
                </div>
                <div className="block-question-card-title-text">
                    {title}
                </div>
            </div>
            <div className="block-question-card-answers">
                {
                    answers.map(a => 
                        <AnswerItem
                            key={a.id}  
                            title={a.title}
                            answer_id={a.id}
                            description={a.description}
                            is_checked={a.id == checkedAnswer}
                            onClick={handleAnswerClick}
                        />    
                    )
                }
            </div>
        </div>
    )
}

interface IAnswerItem{
    answer_id: string
    title: string
    description: string
    is_checked: boolean
    onClick: (id: string) => void
}
const AnswerItem: FC<IAnswerItem> = ({answer_id, title, description, is_checked, onClick}) => {
    return (
        <div className="block-answer" onClick={() => onClick(answer_id)}>
            <div className="block-answer-radio">
                {is_checked ? <div className="block-answer-radio-checked"></div> : null}
            </div>
            <div className="block-answer-text">{title}</div>
        </div>
    )
}