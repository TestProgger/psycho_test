import { IListResponse } from "@/types/services/base";
import BaseService from "./base";
import { ITest } from "@/types/services/tests";


class TestsService extends BaseService{
    protected basePath: string = '/pst/test';

    constructor(secret: string){
        super(secret)
    }


    public async list(){
        return await this.get<IListResponse<ITest>>('/list')
    }

}

export default TestsService