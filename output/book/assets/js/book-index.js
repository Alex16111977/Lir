// JavaScript для головної сторінки книги

// Перевірка на закладки
window.addEventListener('load', () => {
    const bookmark = localStorage.getItem('bookmark');
    
    if (bookmark) {
        const data = JSON.parse(bookmark);
        const continueReading = confirm('Sie haben ein Lesezeichen. Möchten Sie weiterlesen?');
        
        if (continueReading) {
            window.location.href = `chapters/${data.chapter}`;
        }
    }
    
    // Показуємо прогрес читання
    showReadingProgress();
});

function showReadingProgress() {
    const chapters = document.querySelectorAll('.chapter-card');
    
    chapters.forEach((card, index) => {
        const chapterFile = `chapter-${String(index + 1).padStart(2, '0')}.html`;
        const position = localStorage.getItem(`reading-position-${chapterFile}`);
        
        if (position && parseInt(position) > 100) {
            const badge = document.createElement('span');
            badge.className = 'reading-badge';
            badge.textContent = '✓ Gelesen';
            badge.style.cssText = `
                position: absolute;
                top: 10px;
                right: 10px;
                background: #27ae60;
                color: white;
                padding: 5px 10px;
                border-radius: 20px;
                font-size: 0.8rem;
            `;
            card.style.position = 'relative';
            card.appendChild(badge);
        }
    });
}

// Анімація карток глав
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
});

document.querySelectorAll('.chapter-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'all 0.5s ease';
    observer.observe(card);
});