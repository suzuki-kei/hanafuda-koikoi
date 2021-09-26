
/**
 *
 *
 *
 */
const $range = (() => {

    // デフォルトは [start, end).
    function range(start, end) {
        return this.open(start, end)
    }

    // 半開区間 [start, end).
    range.open = function(start, end) {
        const n = end - start
        return [...Array(n).keys()].map(_ => _ + start)
    }

    // 閉区間 [start, end].
    range.closed = function(start, end) {
        const n = end - start + 1
        return [...Array(n).keys()].map(_ => _ + start)
    }

    return range

})()

/**
 *
 * 指定した Element ID を持つテンプレートから, 新しい要素を生成する.
 *
 * @param {string} templateId
 *     テンプレートに使用する <template> 要素の ID.
 *
 * @param {function(Element):Element|undefined} initialize
 *     作成した要素を初期化する関数.
 *
 */
function createElementFromTemplateId(templateId, initialize) {
    const template = document.getElementById(templateId)
    const element = template.content.cloneNode(true)
    return (initialize || (_ => _))(element)
}

