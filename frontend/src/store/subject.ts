import { ICreateSubject } from "@/types/services/subject";
import { types } from "mobx-state-tree";


export const Subject = types.model('Subject', {
    id: types.string,
    first_name: types.string,
    last_name: types.string,
    middle_name: types.optional(types.maybeNull(types.string), ''),
    group_id: types.string,
    secret: types.string
})
.actions(self => ({
    setSubject(data: ICreateSubject){
        self.id = data.id
        self.first_name = data.first_name
        self.last_name = data.last_name
        self.middle_name = data.middle_name
        self.group_id = data.group_id
        self.secret = data.secret
    }
}))