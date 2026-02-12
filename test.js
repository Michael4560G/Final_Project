function toggleMenu(btn) {
    const card = btn.closest('.our-team');
    const dropdown = btn.nextElementSibling;
    
    // סוגר תפריטים אחרים
    document.querySelectorAll('.dropdown-content').forEach(menu => {
        if (menu !== dropdown) {
            menu.classList.remove('show');
            menu.closest('.our-team').classList.remove('menu-open');
        }
    });
    
    // פותח/סוגר את הנוכחי
    const isOpen = dropdown.classList.toggle('show');
    
    if (isOpen) {
        card.classList.add('menu-open');
    } else {
        card.classList.remove('menu-open');
    }
}

document.querySelectorAll('.our-team').forEach(card => {
    
    card.addEventListener('mouseleave', () => {
        // מחפש את הדרופ-דאון בתוך הכרטיס הספציפי הזה
        const dropdown = card.querySelector('.dropdown-content');
        
        // סוגר רק אם הוא באמת פתוח
        if (dropdown && dropdown.classList.contains('show')) {
            dropdown.classList.remove('show');
            card.classList.remove('menu-open');
        }
    });
});

// סגירה בלחיצה מחוץ לתפריט
window.onclick = function(event) {
    if (!event.target.matches('.menu-btn')) {
        document.querySelectorAll('.dropdown-content').forEach(menu => menu.classList.remove('show'));
        document.querySelectorAll('.our-team').forEach(card => card.classList.remove('menu-open'));
    }
}

