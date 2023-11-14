import { IAnswer } from "./services/question"


interface IQuestionObject{
    id: string
    title: string
    type: string
    is_answered: boolean,
    answers: {
        [key: string]: IAnswer
    }
}


export interface IQuestionObjectList{
    [key: string] : IQuestionObject
}