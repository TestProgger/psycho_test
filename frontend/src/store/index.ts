import { types } from "mobx-state-tree";
import createPersistentStore from "mst-persistent-store";
import { Subject } from "@store/subject";
import { INITIAL_SUBJECT, INITIAL_ERROR } from "./consts";
import { Error } from "./error";
import { StartedTestList } from "./tests";

const RootStore = types.model('RootStore', {
    subject: types.optional(Subject, INITIAL_SUBJECT),
    error: types.optional(Error, INITIAL_ERROR),
    started_tests: types.optional(StartedTestList, {items: []})
})

export const [PersistentStoreProvider, usePersistentStore] =
  createPersistentStore(RootStore, {}, {}, { writeDelay: 100, logging: false });