
const $hanafuda = ($ => {

    $.initialize = () => {
        $.view.initialize()
    }

    return $

})({})

$hanafuda.model = ($ => {

    $.cards = [
        {
            month: 1, 
            name: "松に鶴",
            pronounce: "まつ に つる",
            point: 20,
            image: "month-01.card-01.svg",
        },
        {
            month: 1, 
            name: "松に赤短",
            pronounce: "まつ に あかたん",
            point: 5,
            image: "month-01.card-02.svg",
        },
        {
            month: 1, 
            name: "松のカス",
            pronounce: "まつ の かす",
            point: 1,
            image: "month-01.card-03.svg",
        },
        {
            month: 1, 
            name: "松のカス",
            pronounce: "まつ の かす",
            point: 1,
            image: "month-01.card-04.svg",
        },
        {
            month: 2, 
            name: "梅に鶯",
            pronounce: "うめ に うぐいす",
            point: 20,
            image: "month-02.card-01.svg",
        },
        {
            month: 2, 
            name: "梅に赤短",
            pronounce: "うめ に あかたん",
            point: 5,
            image: "month-02.card-02.svg",
        },
        {
            month: 2, 
            name: "梅のカス",
            pronounce: "うめ の かす",
            point: 1,
            image: "month-02.card-03.svg",
        },
        {
            month: 2, 
            name: "梅のカス",
            pronounce: "うめ の かす",
            point: 1,
            image: "month-02.card-04.svg",
        },
        {
            month: 3, 
            name: "桜に幕",
            pronounce: "さくら に まく",
            point: 20,
            image: "month-03.card-01.svg",
        },
        {
            month: 3, 
            name: "桜に赤短",
            pronounce: "さくら に あかたん",
            point: 5,
            image: "month-03.card-02.svg",
        },
        {
            month: 3, 
            name: "桜のカス",
            pronounce: "さくら の かす",
            point: 1,
            image: "month-03.card-03.svg",
        },
        {
            month: 3, 
            name: "桜のカス",
            pronounce: "さくら の かす",
            point: 1,
            image: "month-03.card-04.svg",
        },
        {
            month: 4, 
            name: "藤に時鳥",
            pronounce: "ふじ に ほととぎす",
            point: 10,
            image: "month-04.card-01.svg",
        },
        {
            month: 4, 
            name: "藤に短冊",
            pronounce: "ふじ に たんざく",
            point: 5,
            image: "month-04.card-02.svg",
        },
        {
            month: 4, 
            name: "藤のカス",
            pronounce: "ふじ の かす",
            point: 1,
            image: "month-04.card-03.svg",
        },
        {
            month: 4, 
            name: "藤のカス",
            pronounce: "ふじ の かす",
            point: 1,
            image: "month-04.card-04.svg",
        },
        {
            month: 5, 
            name: "菖蒲に八ツ橋",
            pronounce: "あやめ に やつはし",
            point: 10,
            image: "month-05.card-01.svg",
        },
        {
            month: 5, 
            name: "菖蒲に短冊",
            pronounce: "あやめ に たんざく",
            point: 5,
            image: "month-05.card-02.svg",
        },
        {
            month: 5, 
            name: "菖蒲のカス",
            pronounce: "あやめ の かす",
            point: 1,
            image: "month-05.card-03.svg",
        },
        {
            month: 5, 
            name: "菖蒲のカス",
            pronounce: "あやめ の かす",
            point: 1,
            image: "month-05.card-04.svg",
        },
        {
            month: 6, 
            name: "牡丹に蝶",
            pronounce: "ぼたん に ちょう",
            point: 10,
            image: "month-06.card-01.svg",
        },
        {
            month: 6, 
            name: "牡丹に青短",
            pronounce: "ぼたん に あおたん",
            point: 5,
            image: "month-06.card-02.svg",
        },
        {
            month: 6, 
            name: "牡丹のカス",
            pronounce: "ぼたん の かす",
            point: 1,
            image: "month-06.card-03.svg",
        },
        {
            month: 6, 
            name: "牡丹のカス",
            pronounce: "ぼたん の かす",
            point: 1,
            image: "month-06.card-04.svg",
        },
        {
            month: 7, 
            name: "萩に猪",
            pronounce: "はぎ に いのしし",
            point: 10,
            image: "month-07.card-01.svg",
        },
        {
            month: 7, 
            name: "萩に短冊",
            pronounce: "はぎ に たんざく",
            point: 5,
            image: "month-07.card-02.svg",
        },
        {
            month: 7, 
            name: "萩のカス",
            pronounce: "はぎ の かす",
            point: 1,
            image: "month-07.card-03.svg",
        },
        {
            month: 7, 
            name: "萩のカス",
            pronounce: "はぎ の かす",
            point: 1,
            image: "month-07.card-04.svg",
        },
        {
            month: 8, 
            name: "芒に月",
            pronounce: "すすき に つき",
            point: 20,
            image: "month-08.card-01.svg",
        },
        {
            month: 8, 
            name: "芒に雁",
            pronounce: "すすき に かり",
            point: 10,
            image: "month-08.card-02.svg",
        },
        {
            month: 8, 
            name: "芒のカス",
            pronounce: "すすき の かす",
            point: 1,
            image: "month-08.card-03.svg",
        },
        {
            month: 8, 
            name: "芒のカス",
            pronounce: "すすき の かす",
            point: 1,
            image: "month-08.card-04.svg",
        },
        {
            month: 9, 
            name: "菊に盃",
            pronounce: "きく に さかずき",
            point: 10,
            image: "month-09.card-01.svg",
        },
        {
            month: 9, 
            name: "菊に青短",
            pronounce: "きく に あおたん",
            point: 5,
            image: "month-09.card-02.svg",
        },
        {
            month: 9, 
            name: "菊のカス",
            pronounce: "きく の かす",
            point: 1,
            image: "month-09.card-03.svg",
        },
        {
            month: 9, 
            name: "菊のカス",
            pronounce: "きく の かす",
            point: 1,
            image: "month-09.card-04.svg",
        },
        {
            month: 10, 
            name: "紅葉に鹿",
            pronounce: "もみじ に しか",
            point: 10,
            image: "month-10.card-01.svg",
        },
        {
            month: 10, 
            name: "紅葉に青短",
            pronounce: "もみじ に あおたん",
            point: 5,
            image: "month-10.card-02.svg",
        },
        {
            month: 10, 
            name: "紅葉のカス",
            pronounce: "もみじ の かす",
            point: 1,
            image: "month-10.card-03.svg",
        },
        {
            month: 10, 
            name: "紅葉のカス",
            pronounce: "もみじ の かす",
            point: 1,
            image: "month-10.card-04.svg",
        },
        {
            month: 11, 
            name: "柳に小野道風",
            pronounce: "やなぎ に おののみちかぜ",
            point: 20,
            image: "month-11.card-01.svg",
        },
        {
            month: 11, 
            name: "柳に燕",
            pronounce: "やなぎ に つばめ",
            point: 10,
            image: "month-11.card-02.svg",
        },
        {
            month: 11, 
            name: "柳に短冊",
            pronounce: "やなぎ に たんざく",
            point: 5,
            image: "month-11.card-03.svg",
        },
        {
            month: 11, 
            name: "柳のカス",
            pronounce: "やなぎ の かす",
            point: 1,
            image: "month-11.card-04.svg",
        },
        {
            month: 12, 
            name: "桐に鳳凰",
            pronounce: "きり に ほうおう",
            point: 20,
            image: "month-12.card-01.svg",
        },
        {
            month: 12, 
            name: "桐のカス",
            pronounce: "きり の かす",
            point: 1,
            image: "month-12.card-02.svg",
        },
        {
            month: 12, 
            name: "桐のカス",
            pronounce: "きり の かす",
            point: 1,
            image: "month-12.card-03.svg",
        },
        {
            month: 12, 
            name: "桐のカス",
            pronounce: "きり の かす",
            point: 1,
            image: "month-12.card-04.svg",
        },
    ]

    $.monthToCards = $.cards.reduce((map, card) => {
        map[card.month] ||= []
        map[card.month].push(card)
        return map
    }, {})

    $.monthToPointToCards = (map => {
        $range.closed(1, 12).forEach(month => {
            [20, 10, 5, 1].forEach(point => {
                map[month] ||= {}
                map[month][point] ||= []
            })
        })
        $.cards.forEach(card => {
            map[card.month][card.point].push(card)
        })
        return map
    })({})

    return $

})({})

$hanafuda.view = ($ => {

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
            monthElement.innerText = "" + month + "月"
        }

        function initializeCardElements(tbodyElement, month) {
            const cards = $hanafuda.model.monthToCards[month]
            cards.forEach(card => {
                const pointElement = tbodyElement.querySelector(".point-" + card.point)
                const cardElement = createCardElement(card)
                pointElement.appendChild(cardElement)
            })
        }

        function createCardElement(card) {
            const cardElement = document.createElement("img")
            const imageFileUrl = "./images/" + card.image
            const nameWithPronounce = card.name + " (" + card.pronounce + ")"
            cardElement.setAttribute("src", imageFileUrl)
            cardElement.setAttribute("alt", nameWithPronounce)
            cardElement.setAttribute("title", nameWithPronounce)
            cardElement.setAttribute("class", "card")
            return cardElement
        }

        initialize()
    }

    return $

})({})

