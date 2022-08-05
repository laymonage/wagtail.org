import '../sass/main.scss';

import GetStartedMenu from './components/get-started-menu';

function initComponent(ComponentClass) {
    const items = document.querySelectorAll(ComponentClass.selector());
    items.forEach((item) => new ComponentClass(item));
}

document.addEventListener('DOMContentLoaded', () => {
    initComponent(GetStartedMenu);
});
