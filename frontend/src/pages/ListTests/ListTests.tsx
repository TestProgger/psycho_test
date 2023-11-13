import { ITest } from "@/types/services/tests";
import { observer } from "mobx-react-lite";
import { FC, useState } from "react";
import './ListTests.scss'
import { usePersistentStore } from "@store";
import TestCard from "./components/TestCard";



const ListTestsPage: FC = () => {

    const [testList, setTestList] = useState<ITest[]>([]);
    const { subject } = usePersistentStore()

    return (
        <div className="list-tests-page">
            <div className="block-head">
                <div className="block-head-greating">ПРИВЕТСТВУЮ,</div>
                <div className="block-head-full-name">
                    {`${subject.last_name} ${subject.first_name} ${subject.middle_name}`}
                </div>
            </div>
            <div className="block-body">
                <TestCard 
                    test_id="1" 
                    name='Ригидный сука' 
                    description="окшащшукшукшщу" 
                    questions_count={50} 
                    onStartTestClick={console.log} 
                />
            </div>
        </div>
    )
}

export default observer(ListTestsPage)

