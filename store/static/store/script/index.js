// Special Countdown 
let daysItem = document.querySelector("#days");
let hoursItem = document.querySelector("#hours");
let minItem = document.querySelector("#min");
let secItem = document.querySelector("#sec");

let countDown = () => {
    let futureDate = new Date("30 August 2023");
    let currentDate = new Date();
    let myDate = futureDate - currentDate;

    let days = Math.floor(myDate / 1000 / 60 / 60 / 24);
    let hours = Math.floor(myDate / 1000 / 60 / 60) % 24;
    let min = Math.floor(myDate / 1000 / 60) % 60;
    let sec = Math.floor(myDate / 1000) % 60;

    daysItem.innerHTML = days;
    hoursItem.innerHTML = hours;
    minItem.innerHTML = min;
    secItem.innerHTML = sec;
}

countDown()

setInterval(countDown, 1000)

//automatically close nav drop down on smaller devices when clicked on any option
let navBar = document.querySelectorAll('.nav-link');
let navCollapse = document.querySelector('.navbar-collapse.collapse');
navBar.forEach(function(a){
    a.addEventListener('click',function() {
        navCollapse.classList.remove('show');
    })
})

//making slider when user click on cart-icon
let shoppingCart = document.querySelector('.shopping-cart');
document.querySelector('.cart-icon').onclick = ()=>{
    shoppingCart.classList.toggle('active')
}