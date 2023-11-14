import { IStartTest } from "@types/services/tests";
import { cast, types } from "mobx-state-tree";



export const StartedTest = types.model("StartedTest", {
    subject_test_id: types.string,
    token: types.string,
    test_name: types.string
})
.actions(self => ({
    setTest(data: IStartTest){
        self.subject_test_id = data.subject_test_id
        self.token = data.token
        self.test_name = data.test_name
    }
}))


export const StartedTestList = types.model("StartedTestList", {
    items: types.optional(types.array(StartedTest), [])
})
.actions(self => ({
    add(data: IStartTest){
        self.items.push(cast(data))
    }
}))