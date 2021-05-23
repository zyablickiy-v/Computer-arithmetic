<template>
<div>
	<div id="header">
		<input type="text" placeholder="Фамилия Имя" id="uname" v-model="uname">
		<input type="text" placeholder="Класс" id="ugroup" v-model="ugroup">
		<TestIndicator
			v-if="runningTest"
			:timeElapsed="_timeElapsed"
			:timeTotal="_timeTotal"
			:tasksTotal="tasksTotal"
			:tasksDone="tasksDone"
		/>
	</div>
	<div id="nav">
		<router-link to="/" @click="runningTest = false">Главаная</router-link> |
		<router-link to="/test/train" @click="startTest(true)">Тренировочный режим</router-link> |
		<router-link to="/test/controll" @click="startTest(false)">Контрольный режим</router-link>
	</div>
<!-- Go to work, get married,
have some kids, pay your taxes,
pay your bills, watch your TV,
follow fashion, act normal,
OBEY THE LAW
and repeat after me:
"I AM FREE". AUF -->
	<router-view
		:_test="test"
		:tasksDone="tasksDone"
		:set="set"
		:nextTask="nextTask"
		:results="results"
		:train="train"
	/>
</div>
</template>

<script>
import TestIndicator from '@/components/TestIndicator.vue';

export default {
	data: () => ({
		runningTest: false,
		timeEnd: 0,
		timeStart: 0,
		tasksTotal: 0,
		tasksDone: 0,
		_timeElapsed: '00:00',
		_timeTotal: '00:00',
		train: false,
		results: { tasks: [], mark: null, vmark: null },
		test: [
			{ question: '1 2 3 + +', correctAnswer: '6', answer: null },
			{ question: '1 2 3 - +', correctAnswer: '2', answer: null },
		],
		uname: '',
		ugroup: ''
	}),
	methods: {
		formatTime(time) {
			time /= 1000;
			let [m, s] = [parseInt(time / 60), parseInt(time % 60)];
			return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
		},
		timeElapsed(timeStart) {
			return Date.now() - timeStart;
		},
		testNotOver() {
			if (!this.runningTest)
				return this.runningTest;

			this.runningTest = Date.now() < this.timeEnd && this.tasksDone < this.tasksTotal;
			if (!this.runningTest)
				this.testOver();
			
			return this.runningTest;
		},
		set(what, val) {
			this[what] = val;
		},
		nextTask() {
			this.tasksDone++;
			this.testNotOver();
		},
		async testOver() {
			this.$router.push('/end');
			this.results = await eel.Judge(this.test, this.train)();
		},
		async startTest(train) {
			this.train = train;
			if ((!this.uname || !this.ugroup) && !train) {
				this.$router.replace('/');
				this.runningTest = false;
				alert('Требуется авторизация. Введите "Фимилию Имя" и "Класс" в соответствующие поля.');
				return;
			}
			// fetching test
			let trainQC = null;
			if (train) {
				try {
					trainQC = prompt('Введите количество вопросов каждого типа (3) в формате: n1; n2; n3').split(';').map(v => v.replaceAll(' ', ''));
				}
				catch {
					trainQC = [0, 0, 0];
				}
				if (!trainQC || trainQC.length < 3)
					trainQC = [0, 0, 0];
			}
			this.test = await eel.GenTest(this.uname, this.ugroup, train, trainQC)();
			this.timeStart = Date.now();
			this.timeEnd = this.timeStart + 1000 * 60 * await eel.GetTime()();
			this.tasksTotal = this.test.length;
			this.tasksDone = 0;
			this.runningTest = true;
		}
	},
	components: {
		TestIndicator
	},
	mounted() {
		setInterval(() => {
			if (!this.runningTest || !this.testNotOver())
				return;
			this._timeElapsed = this.formatTime(this.timeElapsed(this.timeStart));
			this._timeTotal = this.formatTime(this.timeEnd - this.timeStart);
		}, 1000);
	},
	setup() {
		window.onclose = eel.WindowClose;
	}
}
</script>

<style>
* {
	font-size: 16px;
}
body {
	background: url('assets/ironia.jpg');
	background-attachment: fixed;
	background-size: cover;
	background-origin: content-box;
	background-repeat: no-repeat;
	background-position: 100% 100%;
	height: 100%;
}
html {
	height: 100%;
}
#app {
	font-family: Consolas, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: white;
	text-shadow: 1px 1px 5px black;
	padding: 5pt;
	padding-top: 0pt;
	height: 100%;
}

#nav {
	padding: 20px;
}
#nav a {
	font-weight: bold;
	color: #739dc7;
}
#nav a.router-link-exact-active {
	color: rgb(50, 150, 255);
}

#header {
	text-align: left;
	background: rgba(54, 108, 179, 0.7);
	color: white;
	padding: 5px;
}
#header > input {
	display: inline-block;
	vertical-align: top;
	margin-left: 3pt;
	margin-right: 3pt;
}
#uname {
	width: 40%;
	margin: 0pt;
}
#ugroup {
	width: 10%;
	margin: 0pt;
}

input, select, textarea, button {
	transition: 0.5s ease-out;
	background: rgba(10, 10, 10, 0.7);
	border: 1px solid #555;
	color: #FFF;

	padding-left: 4pt;
	padding-right: 4pt;
	padding-bottom: 3pt;
	margin-top: 1pt;
	margin-bottom: 1pt;
}
input[type="button"], input[type="submit"], button {
	cursor: pointer;
}
input[type="button"]:hover, input[type="submit"]:hover, button:hover {
	background: rgba(50, 150, 255, 0.7);
}
option {
	background-color: rgba(20, 20, 20);
}
</style>