class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  toString() {
    return `[${this._code}]`;
  }

  [Symbol.for('nodejs.util.inspect.custom')]() {
    return `Airport ${this.toString()} { _name: '${this._name}', _code: '${this._code}' }`;
  }
}

export default Airport;
