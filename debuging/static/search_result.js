window.onload = function(){
    let pill_list = document.querySelectorAll(".dropdown_result")

    for (let pill of pill_list){
        pill.addEventListener("click", () => {
            pill.parentNode.querySelector(".pill_list").classList.toggle("activated")
        })
    }

    let radio_list = document.querySelectorAll(".pill_radio")

    for (let radio of radio_list){
        radio.addEventListener("click", () => {
            label = radio.parentNode.parentNode.parentNode.parentNode.querySelector(".dropdown_result > label")
            label.innerText = radio.parentNode.querySelector("label").innerText
        })
    }
}