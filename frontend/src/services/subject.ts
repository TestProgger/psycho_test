import BaseService from '@services/base';
import { ICreateSubject, IGroup } from '@/types/services/subject';
import { IListResponse } from '@/types/services/base';


class SubjectService extends BaseService{
    protected basePath: string = '/subject'

    constructor(secret: string = ''){
        super(secret);
    }

    public async create_subject(first_name: string, last_name: string, middle_name: string, group_id: string){
        return await this.post<ICreateSubject>('/create/', {first_name, last_name, middle_name, group_id})
    }

    public async list_groups(){
        return await this.get<IListResponse<IGroup>>('/list_groups/')
    }
}

export default SubjectService