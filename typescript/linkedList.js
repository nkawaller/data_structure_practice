var ListNode = /** @class */ (function () {
    // Node constructor
    function ListNode(nodeValue) {
        this._value = nodeValue;
        this._next = null;
    }
    Object.defineProperty(ListNode.prototype, "value", {
        get: function () {
            return this._value;
        },
        set: function (v) {
            this._value = v;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(ListNode.prototype, "next", {
        get: function () {
            return this._next;
        },
        set: function (v) {
            this._next = v;
        },
        enumerable: false,
        configurable: true
    });
    return ListNode;
}());
var a = new ListNode(1);
console.log(a);
console.log(a.value);
console.log(a.next);
a.next(7);
console.log(a.next);
var b = new ListNode(2);
console.log(b);
