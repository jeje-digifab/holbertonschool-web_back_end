class Building {
  constructor(sqft) {
    if (new.target === Building) {
      throw new Error('Cannot instantiate abstract class Building');
    }
    this._sqft = sqft;

    if (typeof this.evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }
}

export default Building;
