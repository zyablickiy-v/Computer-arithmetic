import { createRouter, createWebHashHistory } from 'vue-router'
import Docs from '../views/Docs.vue';
import Test from '../views/Test.vue';
import End from '../views/End.vue';

const baseTitle = 'Компьютерная арифметика – вещественные числа - ';

const routes = [
	{
		path: '/',
		name: 'Docs',
		component: Docs,
		meta: {
			title: baseTitle + 'Главная'
		}
	},
	{
		path: '/test/:mode',
		name: 'Test',
		component: Test,
		meta: {
			title: baseTitle + 'Тестирование'
		}
	},
	{
		path: '/end',
		name: 'End',
		component: End,
		meta: {
			title: baseTitle + 'Результаты теста'
		}
	}
]

const router = createRouter({
	history: createWebHashHistory(),
	routes
});

// https://www.digitalocean.com/community/tutorials/vuejs-vue-router-modify-head copy-paste (R)
router.beforeEach((to, from, next) => {
	const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);
	const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);
	const previousNearestWithMeta = from.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);
	if(nearestWithTitle)
		document.title = nearestWithTitle.meta.title;
	else if(previousNearestWithMeta)
		document.title = previousNearestWithMeta.meta.title;
	Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => el.parentNode.removeChild(el));
	if(!nearestWithMeta)
		return next();
	nearestWithMeta.meta.metaTags.map(tagDef => {
		const tag = document.createElement('meta');
	
		Object.keys(tagDef).forEach(key => {
		tag.setAttribute(key, tagDef[key]);
		});
	
		tag.setAttribute('data-vue-router-controlled', '');
	
		return tag;
	})
	.forEach(tag => document.head.appendChild(tag));
	
	next();
});

export default router
