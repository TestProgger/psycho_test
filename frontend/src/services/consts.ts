export const BaseURL =  /(localhost|127.0.0.1)/gmi.test(window.location.origin) ? 'http://127.0.0.1:8000/api' : '/api'

export enum HTTP_CODE{
    HTTP_200_OK = 200,
    HTTP_400_BAD_REQUEST = 400
}