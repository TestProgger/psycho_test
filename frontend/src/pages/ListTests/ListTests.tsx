import { ITest } from "@/types/services/tests";
import { observer } from "mobx-react-lite";
import { FC, useCallback, useEffect, useState } from "react";
import './ListTests.scss'
import { usePersistentStore } from "@store";
import TestCard from "./components/TestCard";
import TestsService from "@services/tests";
import { IMessageListObject } from "@/types/services/base";
import { useNavigate } from "react-router-dom";
import { SubjectService } from "@services";


const ListTestsPage: FC = () => {
    const navigate = useNavigate()
    const [testList, setTestList] = useState<ITest[]>([]);
    const { subject, error } = usePersistentStore()
    const testsService = new TestsService(subject.secret)
    const subjectService = new SubjectService(subject.secret)

    const listTests = useCallback(async () => {
        const response = await testsService.list();
        if(response.body){
            setTestList(response.body.list)
        }else{
            error.throw(response.status.message as IMessageListObject)
        }
    }, [testList])

    useEffect(() => {
        listTests()
    },[])

    const onStartTestClick = (id: string) => {
        console.log(`START TEST id=${id}`)
        navigate(`/test/${id}`)
    }

    return (
        <div className="list-tests-page">
            <div className="block-head">
                <div className="block-text">
                    <div className="block-text-greating">ПРИВЕТСТВУЮ,</div>
                    <div className="block-text-full-name">
                        {`${subject.last_name} ${subject.first_name} ${subject.middle_name}`}
                    </div>
                </div>
                <div className="block-logout" onClick={() => { subject.clear(); subjectService.logout()}}>Выход</div>
            </div>
            
            <div className="block-body">
                {
                    testList.length && testList.map(
                        t => <TestCard 
                                test_id={t.id} 
                                name={t.name} 
                                description={t.description} 
                                questions_count={t.questions_count} 
                                onStartTestClick={onStartTestClick}
                            />
                    )
                }
            </div>
        </div>
    )
}

export default observer(ListTestsPage)

