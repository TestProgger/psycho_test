export interface ITest{
    id: string,
    questions_count: number,
    name: string,
    description: string,
    image_url: string
}

export interface IStartTest{
    subject_test_id: string
    token: string
    test_name: string
}