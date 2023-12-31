import axios, { AxiosInstance } from "axios";
import { BaseURL } from "./consts";
import { IMessageListObject } from "@/types/services/base";
type RequestMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';

export interface IRefreshTokenBody {
    access: string,
    refresh: string
}


export interface IResponse<T> {
    body: T,
    status: {
        message: string | IMessageListObject,
        code: number
    }
}

class BaseService {
    protected session: AxiosInstance
    public secret: string
    protected basePath: string = ''

    constructor(secret: string = '') {
        this.secret = secret
        this.session = axios.create(
            {
                baseURL: BaseURL,
                timeout: 30000,
                withCredentials: true,
                headers: secret ? { "X-Secret": secret } : {}
            }
        )
    }

    protected async post<T>(url: string, data: object = {}): Promise<IResponse<T>> {
        return await this.request('POST', url, data, {} ) as IResponse<T>
    }

    protected async get<T>(url: string, params: object = {}, ): Promise<IResponse<T>> {
        return await this.request('GET', url, {} ,params) as IResponse<T>
    }

    protected async delete<T>(url: string): Promise<IResponse<T>> {
        return await this.request('DELETE', url, {}, {}) as IResponse<T>
    }

    protected async put<T>(url: string, data = {}): Promise<IResponse<T>> {
        return await this.request('PUT', url, data, {}) as IResponse<T>
    }

    protected async request<T>(method: RequestMethod, url: string, data: object = {}, params: object = {}): Promise<IResponse<T>> {
        try{
            const response = await this.session.request({ method, url: this.basePath + url, data, params })
            return this.formatResponse<T>(response.data)
        }
        catch(e){
            // @ts-ignore
            return e.response.data
        }
        
    }


    private formatResponse<T>(data: object): IResponse<T> {
        try{
            if ("detail" in data) {
                return { 
                    body: null, 
                    status: {
                        message: data['detail'],
                        code: 400
                    }
                } as IResponse<T>
            }
            if (!("body" in data)) {
                return { 
                    body: data, 
                    status: {
                        message: "",
                        code: 0
                    }
                } as IResponse<T>
            }
            return { ...data } as IResponse<T>
        }
        catch(e)
        {
        }
    }

}

export default BaseService;
