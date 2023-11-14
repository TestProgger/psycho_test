export interface IAnswer{
    id: string
    title: string
    description: string
    is_checked: boolean
}

export interface IQuestion{
    id: string
    title: string
    type: string
    is_answered: boolean,
    answers: IAnswer[]
}