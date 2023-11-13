import {FC, useCallback, useEffect, useState} from 'react'
import './Main.scss'
import { StyledInput } from './components'
import { Autocomplete, TextField } from '@mui/material';
import { IGroup } from '@/types/group';
import { Arrow } from '@icons/Arrow';
import { SubjectService } from '@services';


const OPTIONS = [
    {'name': 'ZIS' , 'id': '123'},
    {'name': 'ZISA' , 'id': '1231231'},
    {'name': 'ZISO' , 'id': '123123'}
]


export const MainPage : FC = () => {
    const [firstName, setFirstName] = useState<string>('')
    const [lastName, setLastName] = useState<string>('')
    const [middleName, setMiddleName] = useState<string>('')
    const [groupId, setGroupId] = useState<string>('')
    const [groupList, setGroupList] = useState<IGroup[]>([])

    const subjectService = new SubjectService();

    const listGroups = useCallback(async () => {
        const response = await subjectService.list_groups()
        setGroupList(response.body.list)
    }, [groupList])

    useEffect(() => {
        listGroups()
    }, [])



    return (
        <div className="main-page">
            <div className="container">
                <div className="block-text">
                    ПСИХОЛОГИЧЕСКИЕ <br />
                    <div className="block-text-right">ТЕСТЫ</div>
                </div>
                <div className="block-auth">
                    <div className="block-auth-input">
                        <StyledInput placeholder='Фамилия' value={lastName} onChange={e => setLastName(e.target.value)}/>
                        <StyledInput placeholder='Имя' value={firstName} onChange={e => setFirstName(e.target.value)}/>
                        <StyledInput placeholder='Отчество' value={middleName} onChange={e => setMiddleName(e.target.value)}/>
                        <Autocomplete
                            value={groupId}
                            onChange={(e, value) => {console.log(OPTIONS.filter(o => o.name === value)[0].id); setGroupId(OPTIONS.filter(o => o.name === value)[0].id)}}
                            disablePortal
                            options={OPTIONS.map(o => o.name)}
                            sx={{width: '100%'}}
                            renderInput={(params) => <TextField {...params} label="Группа" />}
                        />
                    </div>
                    <div className="block-auth-go-next">
                        <div className="block-auth-go-next-text">
                            Пройти тесты
                        </div>
                        <div className="block-auth-go-next-icon">
                            <Arrow width={24} height={24} />
                        </div>
                    </div> 
                </div>
            </div>
        </div>
    )
}