// Функції читання
let currentFontSize = 18;
const MIN_FONT_SIZE = 12;
const MAX_FONT_SIZE = 32;

// Збільшення шрифту
document.getElementById('font-size-up')?.addEventListener('click', () => {
    if (currentFontSize < MAX_FONT_SIZE) {
        currentFontSize += 2;
        document.querySelector('.text-content').style.fontSize = currentFontSize + 'px';
        localStorage.setItem('fontSize', currentFontSize);
    }
});

// Зменшення шрифту
document.getElementById('font-size-down')?.addEventListener('click', () => {
    if (currentFontSize > MIN_FONT_SIZE) {
        currentFontSize -= 2;
        document.querySelector('.text-content').style.fontSize = currentFontSize + 'px';
        localStorage.setItem('fontSize', currentFontSize);
    }
});

// Перемикання теми
document.getElementById('toggle-theme')?.addEventListener('click', () => {
    const body = document.body;
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    // Оновлюємо іконку кнопки
    const button = document.getElementById('toggle-theme');
    button.textContent = newTheme === 'dark' ? '☀️' : '🌙';
});

// Повноекранний режим
document.getElementById('fullscreen')?.addEventListener('click', () => {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
    } else {
        document.exitFullscreen();
    }
});

// Закладки
document.getElementById('bookmark')?.addEventListener('click', () => {
    const chapter = window.location.pathname.split('/').pop();
    const scrollPosition = window.scrollY;
    
    const bookmark = {
        chapter: chapter,
        position: scrollPosition,
        date: new Date().toISOString()
    };
    
    localStorage.setItem('bookmark', JSON.stringify(bookmark));
    
    // Візуальний фідбек
    const button = document.getElementById('bookmark');
    button.style.transform = 'scale(1.2)';
    setTimeout(() => {
        button.style.transform = 'scale(1)';
    }, 300);
});

// Прогрес читання
function updateProgress() {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    
    const progressBar = document.getElementById('progress-fill');
    if (progressBar) {
        progressBar.style.width = scrolled + '%';
    }
    
    // Зберігаємо позицію читання
    const chapter = window.location.pathname.split('/').pop();
    localStorage.setItem(`reading-position-${chapter}`, winScroll);
}

window.addEventListener('scroll', updateProgress);

// Відновлення налаштувань при завантаженні
window.addEventListener('load', () => {
    // Відновлюємо розмір шрифту
    const savedFontSize = localStorage.getItem('fontSize');
    if (savedFontSize) {
        currentFontSize = parseInt(savedFontSize);
        document.querySelector('.text-content').style.fontSize = currentFontSize + 'px';
    }
    
    // Відновлюємо тему
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.body.setAttribute('data-theme', savedTheme);
        const button = document.getElementById('toggle-theme');
        if (button) {
            button.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
        }
    }
    
    // Відновлюємо позицію читання
    const chapter = window.location.pathname.split('/').pop();
    const savedPosition = localStorage.getItem(`reading-position-${chapter}`);
    if (savedPosition) {
        window.scrollTo(0, parseInt(savedPosition));
    }
});

// Клавіші швидкого доступу
document.addEventListener('keydown', (e) => {
    // Alt + → для наступної глави
    if (e.altKey && e.key === 'ArrowRight') {
        const nextLink = document.querySelector('.nav-next');
        if (nextLink) nextLink.click();
    }
    
    // Alt + ← для попередньої глави
    if (e.altKey && e.key === 'ArrowLeft') {
        const prevLink = document.querySelector('.nav-prev');
        if (prevLink) prevLink.click();
    }
    
    // F11 для повноекранного режиму
    if (e.key === 'F11') {
        e.preventDefault();
        document.getElementById('fullscreen').click();
    }
});