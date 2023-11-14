import QuestionService from "@services/question";
import TestsService from "@services/tests";
import { usePersistentStore } from "@store";
import { IMessageListObject } from "@/types/services/base";
import { IQuestion } from "@/types/services/question";
import { observer } from "mobx-react-lite";
import { FC, useCallback, useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import './Test.scss';
import { QuestionCard } from "./components/QuestionCard/QuestionCard";
import AnswerService from "@services/answer";
import Modal from "@components/Modal";


const TestPage: FC = () => {
    const { started_tests, error, subject } = usePersistentStore()

    const params = useParams()
    const testsService = new TestsService(subject.secret)
    const questionService = new QuestionService(subject.secret)
    const answerService = new AnswerService(subject.secret)
    const [testName, setTestName] = useState<string>('')
    const [questionList, setQuestionList] = useState<IQuestion[]>([])
    const [testId, setTestId] = useState<string>('')
    const navigate = useNavigate()

    const [isModalView, setIsModalView] = useState<boolean>(false)
    const [modalTitle, setModalTitle] = useState<string>('')

    const startTest = async () => {
        const response = await testsService.startTest(params?.id as string)
        if(response.body){
            started_tests.add(response.body)
            setTestName(response.body.test_name)
            setTestId(response.body.subject_test_id)
            const q_response = await questionService.list(response.body.subject_test_id)
            if(q_response.body){
                setQuestionList(q_response.body.list)
            }
            else{
                error.throw(response.status.message as IMessageListObject)
            }
        }
        else
        {
            error.throw(response.status.message as IMessageListObject)
        }
    }

    const handleAnswerClick = async (question_id: string, answer_id: string) => {
        const response = await answerService.setAnswer(question_id, answer_id)
        if(!response.body)
        {
            error.throw(response.status.message)
        }
    }

    const handleEndTest = useCallback( async () => {
        const response = await testsService.endTest(testId)
        if(!response.body){
            error.throw(response.status.message)
        }
        else{
            setIsModalView(true);
            setModalTitle(response.body.title)
        }
    }, [testId])

    useEffect(() => {
        startTest()
    }, [])

    return(
        <div className="test-page">
            <div className="block-head">
                {testName}
            </div>
            <div className="block-body">
                {
                    questionList && questionList.map((q, index) => 
                        <QuestionCard
                            key={q.id}
                            question_id={q.id}
                            answers={q.answers}
                            index={index+1}
                            onAnswerClick={handleAnswerClick}
                            title={q.title}
                        />    
                    )
                }
            </div>
            <div className="block-footer">
                <div className="block-button-group">
                    <div className="block-button-return" onClick={() => navigate(-1)}>
                        Вернуться назад
                    </div>
                    <div className="block-button-end-test" onClick={() => handleEndTest()}>
                        Завершить тест
                    </div>
                </div>
            </div>
            <Modal isVisible={isModalView} title={modalTitle}/>
        </div>
    )
}

export default observer(TestPage)