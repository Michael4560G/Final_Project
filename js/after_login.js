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



document.addEventListener('DOMContentLoaded', () => {
    const row = document.getElementById('vehicleRow');
    const addWrapper = document.getElementById('addCardWrapper');
    const savedCars = JSON.parse(localStorage.getItem('userCars')) || [];

    savedCars.forEach(car => {
        const col = document.createElement('div');
        col.className = 'col-12 col-sm-6 col-md-5 col-lg-3';
        // המבנה המקורי שלך מילה במילה
        col.innerHTML = `
            <div class="our-team">
                <div class="card-menu">
                    <button class="menu-btn" onclick="toggleMenu(this)">⋮</button>
                    <div class="dropdown-content">
                        <a href="#" onclick="action('Preview')">Preview</a>
                        <a href="#" onclick="action('Edit')">Edit</a>
                        <a href="#" onclick="deleteCar(${car.id})" class="delete">Delete</a>
                    </div>
                </div>
                <div class="picture">
                    <img src="${car.logo}" onerror="this.src='logos/original/default.png'">
                </div>
                <div class="team-content">
                    <h3 class="name">${car.brandHeb} ${car.model}</h3>
                    <ul class="social"><li></li></ul>
                    <a class="btn_enter" href="test.html">כניסה לרכב</a>
                    <br><br>
                    <h4 class="title">${car.year}</h4>
                </div>
            </div>
        `;
        row.insertBefore(col, addWrapper);
    });
});

function toggleMenu(btn) {
    btn.nextElementSibling.classList.toggle('show');
}

function deleteCar(id) {
    let cars = JSON.parse(localStorage.getItem('userCars')) || [];
    cars = cars.filter(c => c.id !== id);
    localStorage.setItem('userCars', JSON.stringify(cars));
    location.reload();
}