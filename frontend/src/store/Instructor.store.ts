import {Module} from "vuex";
import {RootState} from ".";
import {InstructorModule} from "./Instructor.interface";

const module: <InstructorModule, RootState> = {
    state: {
        Lectures: null,
    },

    getters: {

    }

}

export default module;