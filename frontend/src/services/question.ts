import { IListResponse } from "@/types/services/base";
import BaseService from "./base";
import { IQuestion } from "@/types/services/question";



class QuestionService extends BaseService{
    protected basePath: string = "/pst/question";

    constructor(secret: string = ''){
        super(secret)
    }

    public async list(id: string){
        return await this.get<IListResponse<IQuestion>>('/list/', {id})
    }
}

export default QuestionService