document.addEventListener('DOMContentLoaded', function() {
    var calendarDiv = document.querySelector('#calendar');
    var calendar = new FullCalendar.Calendar(calendarDiv, {
        initialView: 'dayGridMonth',
        events: '/api/data/get-calendar',
        eventTimeFormat: {
            hour: '2-digit',
            minute: '2-digit',
            hour12: true
        },
        nowIndicator: true,
        dayMaxEventRows: true,
        firstDay: 1,
        fixedWeekCount: false,
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay',
        },
        buttonText: {
            today: 'Today',
            month: 'Month',
            week: 'Week',
            day: 'Day'
        },
        views: {
            timeGridWeek: {
                allDaySlot: true
            }
        }
    });

    calendar.render();
});