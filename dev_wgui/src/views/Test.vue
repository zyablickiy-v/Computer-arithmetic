<template>
    <div class="test">
        <Task
            v-for="[k, v] of Object.entries(_test)"
            :key="k" :n="k"
            :task="v.question"
            :hint="v.hint"
            :correctAnswer="v.correctAnswer"
            :currentTask="tasksDone"
            :train="train"
            @answer="onAnswer"
        />
    </div>
</template>

<script>
import Task from '@/components/Task.vue';
export default {
    props: ['set', '_test', 'tasksDone', 'nextTask', 'train'],
    methods: {
        onAnswer(answer) {
            let test = this._test;
            console.log(typeof answer);
            test[this.tasksDone].answer = answer.join(' ');
            this.set('test', test);
            this.nextTask();
        }
    },
    mounted() {
        if (this.$route.params.mode == 'contorll') {
            // ...
        }
    },
    components: { Task }
}
</script>

<style scoped>
.test {
    padding: 5pt;
}
</style>