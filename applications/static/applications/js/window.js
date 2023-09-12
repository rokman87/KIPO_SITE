const buttonElem = document.getElementById('open_pop_up');
const modalElem = document.getElementById('pop_up');
const modalContElem = document.getElementById('pop_up_container');

modalElem.style.cssText =`
    display: flex;
    visibility: hidden;
    opacity: 0;
    transition: opacity 300ms ease-in-out;
`;

const closeModal = event => {
    const target = event.target;

    if (target === modalContElem || target.closest('.pop_up_close')) {
    modalElem.style.opacity = 0;
    setTimeout(() => {
     modalElem.style.visibility = 'hidden';
    }, 300)
    }
}

const openModal = () => {
    modalElem.style.visibility = 'visible';
    modalElem.style.opacity = 1;
}

buttonElem.addEventListener('click', openModal)
modalElem.addEventListener('click', closeModal)



function validateWeekDate() {
        var selectedDate = document.getElementById("id_week_date").value;
        var date = new Date(selectedDate);
        if (date.getDay() !== 1) {  // 1 соответствует понедельнику (0 - воскресенье, 2 - вторник, и так далее)
            alert("Пожалуйста, выберите начало недели.");
            document.getElementById("id_week_date").value = "";
        }
    }

document.getElementById("id_week_date").onchange = validateWeekDate;