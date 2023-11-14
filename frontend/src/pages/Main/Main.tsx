import {FC, useCallback, useEffect, useState} from 'react'
import './Main.scss'
import { StyledInput } from './components'
import { Autocomplete, TextField } from '@mui/material';
import { IGroup } from '@/types/group';
import { Arrow } from '@icons/Arrow';
import { SubjectService } from '@services';
import { observer } from 'mobx-react-lite';
import { usePersistentStore } from '@store';
import { IMessageListObject } from '@/types/services/base';

const MainPage : FC = () => {
    const [firstName, setFirstName] = useState<string>('')
    const [lastName, setLastName] = useState<string>('')
    const [middleName, setMiddleName] = useState<string>('')
    const [group, setGroup] = useState<IGroup>({id: '', name: ''})
    const [groupList, setGroupList] = useState<IGroup[]>([])

    const subjectService = new SubjectService();
    const {error, subject} = usePersistentStore()

    const listGroups = useCallback(async () => {
        const response = await subjectService.listGroups()
        if (response.body){
            setGroupList(response.body.list)
        }
    }, [groupList])

    const onGroupSelectorChange = (name: string) => {
        const _group = groupList.find(g => g.name == name)
        setGroup(prev => ({...prev, ..._group}))
    }

    useEffect(() => {
        listGroups()
    }, [])

    const handleCreateSubject = async () => {
        const response = await subjectService.createSubject(
            firstName, lastName, middleName, group.id, subject?.secret || null
        )
        if(response.body){
            subject.setSubject(response.body)
        }else{
            error.throw(response.status.message as IMessageListObject)
        }
    }



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
                            value={group.name}
                            // @ts-ignore
                            onChange={(e, value) => {onGroupSelectorChange(value as string)}}
                            disablePortal
                            options={groupList.map(o => o.name)}
                            sx={{width: '100%'}}
                            renderInput={(params) => <TextField {...params} label="Группа" />}
                        />
                    </div>
                    <div className="block-auth-go-next"onClick={handleCreateSubject}>
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


export default observer(MainPage)