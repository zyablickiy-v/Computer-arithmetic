<template>
    <div v-if="currentTask == n">
        <div>
            {{ task.text }} <b v-for="(expr, i) in task.expr" :key="i + expr">{{ expr }}</b><br>
        </div>
        <table style="width: 100%;">
            <tr>
                <td style="width: 75%">
                    <div class="flex vflex">
                        <input
                            type="text"
                            v-model="answer[i]"
                            @keydown="$event.which == 13 && $emit('answer', answer)"
                            :ref="'ans' + i"
                            v-for="(hint, i) in task.inputHints"
                            :key="i + hint"
                            :placeholder="hint"
                        >
                    </div>
                </td>
                <td><input type="button" value="Далее" @click="$emit('answer', answer)"></td>
                <td><input type="button" :value="showAnswer ? 'Скрыть ответ' : 'Посмотреть ответ'" @click="showAnswer = !showAnswer" v-if="train"></td>
            </tr>
        </table>
        <div v-if="showAnswer" style="margin-top: 8px">
            <div>Правильный ответ: {{ correctAnswer }}</div>
            <div v-if="hint">{{ hint }}</div>
        </div>
    </div>
</template>

<script lang="ts">
export default {
    props: ['task', 'n', 'currentTask', 'train', 'hint', 'correctAnswer'],
    data: () => ({
        answer: [],
        showAnswer: false,
        prevTask: null
    }),
    updated() {
        if (this.prevTask != this.task) {
            this.$refs.ans0.focus();
            this.resetState();
            this.prevTask = this.task;
            console.log(this.task);
        }
    },
    methods: {
        resetState() {
            this.showAnswer = false;
            this.answer = [];
        }
    }
}
</script>

<style scoped>
input {
    margin: 0pt;
    margin-left: 10px;
    margin-top: 4px;
    margin-bottom: 4px;
}
.vflex {
    flex-direction: column;
    width: 100%;
    margin: 0pt;
    padding: 0pt;
}
input[type="text"] {
    width: 100%;
    margin: 0pt;
}
.flex {
    display: flex;
}
div {
    text-align: left;
}
.smaller {
    font-size: 12px;
}
.bigger {
    font-size: 24px;
}
td {
    text-align: center;
    padding: 0pt;
    padding-right: 10px;
    vertical-align: middle;
}
td * {
    width: 100%;
}
</style>