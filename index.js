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

    // 2. בחירת כל הלינקים וגם את הכפתורים עם הקלאס הספציפי
    // הסלקטור בוחר את כל ה-a וגם כל אלמנט עם הקלאס .login_btn
    const navElements = document.querySelectorAll('a, .login_btn');

    navElements.forEach(element => {
        element.addEventListener('click', function(e) {
            // שליפת היעד: בודק href ללינקים, או data-href לכפתורים
            const href = this.getAttribute('href') || this.getAttribute('data-href');
            const target = this.getAttribute('target');

            // אם אין כתובת יעד או שזה לינק פנימי (#), אל תפעיל את האנימציה
            if (!href || href.startsWith('#') || href.includes('http') || target === '_blank') {
                return;
            }

            // מניעת הפעולה הדיפולטיבית
            e.preventDefault();

            // הפעלת ה-Fade Out
            document.body.classList.add('is-loading');

            // מעבר דף לאחר חצי שנייה
            setTimeout(() => {
                window.location.href = href;
            }, 500);
        });
    });
})();