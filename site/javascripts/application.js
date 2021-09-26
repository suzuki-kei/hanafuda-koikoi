
window.onload = () => {
    $hanafuda.initialize()
}

const $hanafuda = (($) => {

    $.initialize = () => {

        function initialize() {
            const hanafudaElement = document.getElementById("hanafuda")
            const tbodyElements = createTbodyElements()
            tbodyElements.forEach(_ => hanafudaElement.appendChild(_))
        }

        function createTbodyElements() {
            const months = $range.closed(1, 12)
            return months.map(createTbodyElement)
        }

        function createTbodyElement(month) {
            const tbodyElement = createElementFromTemplateId("hanafuda-template")
            initializeMonthElement(tbodyElement, month)
            initializeCardElements(tbodyElement, month)
            return tbodyElement
        }

        function initializeMonthElement(tbodyElement, month) {
            const monthElement = tbodyElement.querySelector(".month")
            let monthText = monthElement.innerText
            monthText = monthText.replaceAll("${month}", month)
            monthElement.innerText = monthText
        }

        function initializeCardElements(tbodyElement, month) {
            const cardElements = tbodyElement.querySelectorAll(".card")
            cardElements.forEach(cardElement => initializeCardElement(cardElement, month))
        }

        function initializeCardElement(cardElement, month) {
            const monthText = "month-" + String(month).padStart(2, "0")
            let src = cardElement.getAttribute("src")
            src = src.replaceAll("${month-00}", monthText)
            cardElement.setAttribute("src", src)
        }

        initialize()
    }

    return $

})({})

