// Навігація між главами

// Плавна прокрутка до якорів
function smoothScrollTo(target) {
    const element = document.querySelector(target);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Обробка посилань на якорі
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const target = link.getAttribute('href');
        smoothScrollTo(target);
    });
});

// Swipe жести для мобільних пристроїв
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
});

document.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
});

function handleSwipe() {
    const swipeThreshold = 50;
    const diff = touchStartX - touchEndX;
    
    if (Math.abs(diff) > swipeThreshold) {
        if (diff > 0) {
            // Swipe вліво - наступна глава
            const nextLink = document.querySelector('.nav-next');
            if (nextLink) nextLink.click();
        } else {
            // Swipe вправо - попередня глава
            const prevLink = document.querySelector('.nav-prev');
            if (prevLink) prevLink.click();
        }
    }
}

// Показувати номер сторінки при наведенні
const pageMarkers = document.querySelectorAll('.page-marker');
pageMarkers.forEach(marker => {
    marker.addEventListener('mouseenter', () => {
        marker.style.opacity = '1';
    });
    
    marker.addEventListener('mouseleave', () => {
        marker.style.opacity = '0.5';
    });
});