class ListNode {
    // Store's the node's data
    private _value: number;
    public get value(): number {
        return this._value;
    }
    public set value(v: number) {
        this._value = v;
    }

    // Store's the node's pointer to next node
    private _next: ListNode;
    public get next(): ListNode {
        return this._next;
    }
    public set next(v: ListNode) {
        this._next = v;
    }

    // Node constructor
    constructor(nodeValue: number) {
        this._value = nodeValue;
        this._next = null;
    }
}