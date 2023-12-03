const isLeapYear = (year) => {
    return ((year % 4 === 0 && year !== 0 && year% 400!== 0) ||
            (year % 100 === 0 && year % 400 === 0)
    );
};

const getFebDays = (year)=>{
    return isLeapYear(year) ? 29 :28 ;
};

let calendar = document.querySelector('.calendar');
const month_names = [
    'January',
    'February',
    'March',
    'April',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
];
let month_picker = document.querySelector('#month_picker');
let dayTextFormate = document.querySelector('.day-text-formate');
const timeFormate = document.querySelector('.time_formate');
const dateFormate = document.querySelector('.date_formate');

month_picker.onclick = () => {
    month_list.classList.remove('hideonce');
    month_list.classList.remove('hide');
    month_classList.add('add');
    dayTextFormate.classList.remove('showtime');
    dayTextFormate.classList.add('hidetime');
    timeFormate.classList.remove('showtime');
    timeFormate.classList.add('hideTime');
    dateFormate.classList.remove('showtime');
    dateFormate.classList.add('hideTime');
};

const generateCalendar = (month,year) => {
    let calendar_days = document.querySelector('.calendar_days');
    calendar_days.innerHTML='';
    let calendar_header_years = document.querySelector('#year');
    let days_of_month = [
        31,
        getFebDays(year),
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31,
    ]
    let currentDate = new Date ();
    month_picker.innerHTML = month_names[month];
    calendar_header_year.innerHTML = year;
    let first_date = new Date(year,month);

    for(let i = 0; i<=days_of_month[month]+first_date.getDay()-1; i++){
        let day = document.createElement('div');
        if(i >= first_day.getDay()){
            day.innerHTML=i - first_day.getDay() + 1;
            if(i - first_day.getDay() + 1 === currentDate.getDate() 
            && year === currentDate.getFullYear 
            && month === currentDate.getMonth() ){
                day.classList.add('current-date');
            }
        }
        calendar_days.appendChild(day)
    }
}