import { IListResponse } from "@/types/services/base";
import BaseService from "./base";
import { IStartTest, ITest } from "@/types/services/tests";


class TestsService extends BaseService{
    protected basePath: string = '/pst/test';

    constructor(secret: string = ''){
        super(secret)
    }


    public async list(){
        return await this.get<IListResponse<ITest>>('/list/')
    }

    public async startTest(id: string){
        return await this.post<IStartTest>('/start/', {id})
    }

    public async endTest(id: string){
        return await this.post('/end/', {id})
    }

}

export default TestsService