
function validateWeekDate() {
        var selectedDate = document.getElementById("id_week_date").value;
        var date = new Date(selectedDate);
        if (date.getDay() !== 1) {  // 1 соответствует понедельнику (0 - воскресенье, 2 - вторник, и так далее)
            alert("Пожалуйста, выберите начало недели.");
            document.getElementById("id_week_date").value = "";
        }
    }

document.getElementById("id_week_date").onchange = validateWeekDate;