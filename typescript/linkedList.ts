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

class SinglyLinkedList {

    // Keeps track of the first node of the list
    private _head: ListNode;
    public get head(): ListNode {
        return this._head;
    }
    public set head(node: ListNode) {
        this._head = node;
    }

    // Keeps track of the last node of the list
    private _tail: ListNode;
    public get tail(): ListNode {
        return this._tail;
    }
    public set tail(node: ListNode) {
        this._tail = node;
    }

    // Counts the number of nodes in the list
    private _length: number;
    public get length(): number {
        return this._length;
    }
    public set length(v: number) {
        this._length = v;
    }

    constructor() {
        this._length = 0;
        this._head = null;
        this._tail = null;
    }
}
