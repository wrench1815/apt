import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import './assets/main.css';

const app = createApp(App);

// mdb
import * as mdb from 'mdb-ui-kit';
import 'mdb-ui-kit/css/mdb.min.css';

app.use(router, mdb);

app.mount('#app');
