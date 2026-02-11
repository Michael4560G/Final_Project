// your code goes here
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

(function() {
    "use strict";

    // 1. ברגע שהדף נטען - Fade In
    window.addEventListener('load', () => {
        document.body.classList.remove('is-loading');
    });

    // 2. טיפול במעבר בין דפים - Fade Out
    const links = document.querySelectorAll('a');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            const target = this.getAttribute('target');

            // בדיקה שמדובר בקישור פנימי ולא ב-Anchor (כמו #navPanel) או דף חדש
            if (!href || href.startsWith('#') || href.includes('http') || target === '_blank') {
                return;
            }

            // מניעת המעבר המיידי
            e.preventDefault();

            // הוספת ה-Class שמפעיל את ה-Fade Out ב-CSS
            document.body.classList.add('is-loading');

            // המתנה לסיום האנימציה (500ms כמו ב-CSS) ואז מעבר דף
            setTimeout(() => {
                window.location.href = href;
            }, 500);
        });
    });
})();