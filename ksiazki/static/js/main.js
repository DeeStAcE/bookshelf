const body = document.querySelector('body');
const changeThemeButton = document.querySelector('#theme-toogle');
const themeKey = 'preferred-theme';

const preferredTheme = localStorage.getItem(themeKey);

if (preferredTheme) {
    body.classList.add(preferredTheme);
}

changeThemeButton.addEventListener('click', () => {
    if (body.classList.contains('dark-theme')) {
        body.classList.remove('dark-theme');
        body.classList.add('light-theme');
        localStorage.setItem(themeKey, 'light-theme')
    } else {
        body.classList.remove('light-theme');
        body.classList.add('dark-theme');
        localStorage.setItem(themeKey, 'dark-theme')
    }
});