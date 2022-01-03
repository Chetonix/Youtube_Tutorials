// const circle = {
//   radius: 1,
//   location: {
//     x: 1,
//     y: 1,
//   },
//   draw: function () {
//     console.log("draw");
//   },
// };

//factory function
// function createCircle(radius) {
//   return {
//     radius, //eliminate noise by adding just the name i.e. this is equal to radius = radius
//     //    location: {
//     //     x: 1,
//     //     y: 1,
//     //   },
//     draw: function () {
//       console.log("draw");
//     },
//   };
// }

//constructor function
function Circle(radius) {
  this.radius = radius;
  let defaultLocation = { x: 0, y: 0 };
  //   let computeOptimumLocation = function (factor) {};
  this.draw = function () {
    // computeOptimumLocation(0.1);
    console.log("draw");
  };
  //can be done in an another way as shown below:
  this.getDefaultLocation = function () {
    return defaultLocation;
  };
  Object.defineProperty(this, "defaultLocation", {
    get: function () {
      return defaultLocation;
    },
    set: function (value) {
      if (!value.x || !value.y) throw new Error("Invalid location.");
      else defaultLocation = value;
    },
  });
}

//Function() is used to create the Circle Object, like so:
// const Circle2 = new Function(
//   "radius",
//   `
// this.radius = radius;
// this.draw = function () {
//   console.log("draw");
// }
// `
// );

// const circle1 = createCircle(1);
// circle.draw();

const another = new Circle(1);
//the above is similar to this:
// Object.call({}, 1); //we use apply instead of call to supply an array as the second argument
// another.draw();

// const circle2 = new Circle2(1);
