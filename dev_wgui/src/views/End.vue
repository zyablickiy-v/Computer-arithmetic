<template>
    <div>
        <table>
            <tr>
                <td>Правильность</td>
                <td>Ваш ответ</td>
                <td>Правильный ответ</td>
            </tr>
        </table>
        <table class="result" v-for="[k, v] of Object.entries(results.tasks)" :key="k" :class="{ good: v.correct }">
            <tr>
                <td>{{ v.correct ? '+' : '-' }}</td>
                <td>{{ v.answer || 'Ответ не дан' }}</td>
                <td>{{ v.correctAnswer }}</td>
            </tr>
        </table>
        <div>Результат: {{ parseInt(results.mark * 100) }}%</div>
        <div>Оценка: {{ results.vmark }}</div>
    </div>
</template>

<script>
export default {
    props: ['results']
}
</script>

<style scoped>
table {
    width: 100%;
    max-width: 1000px;
    margin: auto;
    margin-bottom: 10px;
}
table td {
    width: 33%;
}
.result {
    background: rgba(185, 66, 86, 0.4);
}
.result.good {
    background: rgba(66, 185, 131, 0.4);
}
span {
    font-size: 25px;
}
</style>