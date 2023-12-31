import BaseService from '@services/base';
import { ICreateSubject, IGroup } from '@/types/services/subject';
import { IListResponse } from '@/types/services/base';


class SubjectService extends BaseService{
    protected basePath: string = '/subject'

    constructor(secret: string = ''){
        super(secret);
    }

    public async createSubject(first_name: string, last_name: string, middle_name: string, group_id: string, secret: string | null = null){
        return await this.post<ICreateSubject>('/create/', {first_name, last_name, middle_name, group_id, secret})
    }

    public async listGroups(){
        return await this.get<IListResponse<IGroup>>('/list_groups/')
    }

    public async logout(){
        return await this.post('/logout/')
    }
}

export default SubjectService