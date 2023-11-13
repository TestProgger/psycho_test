export interface ICreateSubject{
    id: string
    secret: string
    first_name: string,
    last_name: string,
    middle_name: string,
    group_id: string
}

export interface IGroup{
    id: string
    name: string
}