const toDoList = [];

function addTodo() {
   const inputElement = document.querySelector('.js-name-input');
   const name = inputElement.value;

   toDoList.push(name);
   console.log(toDoList);

   inputElement.value = '';
}