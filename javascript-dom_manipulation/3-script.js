document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('#toggle_header')
  const header = document.querySelector('header')

  toggle.addEventListener('click', () => {
    if (header.classList.contains('red')) {
      header.classList.remove('red')
      header.classList.add('green')
    } else {
      header.classList.remove('green')
      header.classList.add('red')
    }
  })
})