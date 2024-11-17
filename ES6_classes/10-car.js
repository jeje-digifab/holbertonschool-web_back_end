class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    return new Car(this._brand, this._motor, this._color);
  }

  displayDetails() {
    return `Car(brand=${this._brand}, motor=${this._motor}, color=${this._color})`;
  }
}

export default Car;
