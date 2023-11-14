import BaseService from "./base";


class AnswerService extends BaseService{
    protected basePath: string = '/pst/answer';
    
    constructor(secret?: string){
        super(secret)
    }

    public async setAnswer(question_id: string, answer_id: string){
        return await this.post<{title: string}>('/set/', {question_id, answer_id})
    }
}

export default AnswerService