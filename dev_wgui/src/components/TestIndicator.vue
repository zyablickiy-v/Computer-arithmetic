<template>
    <div class="timeIndicator">
        <div class="first">Времени прошло: {{ timeElapsed }} / {{ timeTotal }}</div>
        <div class="second">Заданий сделано: {{ tasksDone }} / {{ tasksTotal }}</div>
    </div>
</template>

<script>
    export default {
        props: ['timeElapsed', 'timeTotal', 'tasksTotal', 'tasksDone']
    }
</script>

<style scoped>
    .timeIndicator {
        display: inline-flex;
        padding-left: 5px;
    }
    .timeIndicator > div {
        margin: 0pt;
        padding: 0pt;
        padding-top: 4pt;
        padding-left: 7pt;
        padding-right: 7pt;
    }
    .second {
        border-left: 1px solid white;
    }
    .first {
        border-right: 1px solid white;
    }
</style>