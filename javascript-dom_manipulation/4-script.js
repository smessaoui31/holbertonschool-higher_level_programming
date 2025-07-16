document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.querySelector('#add_item')
  const myList = document.querySelector('.my_list')

  addItem.addEventListener('click', () => {
    const li = document.createElement('li')
    li.textContent = 'Item'
    myList.appendChild(li)
  })
})