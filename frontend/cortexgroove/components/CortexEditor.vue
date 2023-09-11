<template>
    <div>
      <canvas ref="canvas" class="border-2 border-white rounded-lg w-full"></canvas>
    </div>
  </template>
  
<script>

  import * as paper from "paper";

  export default {
    mounted() {
      // Initialize Paper.js
      paper.setup(this.$refs.canvas);
  
      // Create two rectangles
      var rectangle1 = new paper.Rectangle(new paper.Point(100, 100), new paper.Size(100, 100));
      var path1 = new paper.Path.Rectangle(rectangle1);
      path1.fillColor = 'red';
  
      var rectangle2 = new paper.Rectangle(new paper.Point(300, 100), new paper.Size(100, 100));
      var path2 = new paper.Path.Rectangle(rectangle2);
      path2.fillColor = 'blue';
  
      // Initialize variables to track segment and mouse position
      var segment;
      var mousePoint = new paper.Point(0, 0);
      var isDragging = false;
  
      // Event handler for mouse down on rectangles
      path1.onMouseDown = path2.onMouseDown = function (event) {
        isDragging = true;
      };
  
      // Event handler for mouse up
      paper.view.onMouseUp = function (event) {
        isDragging = false;
        if (segment) {
          segment.remove();
          segment = null;
        }
      };
  
      // Event handler for mouse move
      paper.view.onMouseMove = function (event) {
        mousePoint = event.point;
      };
  
      // Main update function
      paper.view.onFrame = function (event) {
        if (isDragging) {
          if (segment) {
            segment.remove();
            segment = null;
          }
          segment = new paper.Path.Line(path1.bounds.center, mousePoint);
          segment.strokeColor = 'black';
        } else {
          if (segment) {
            segment.remove();
            segment = null;
          }
        }
  
        // Check if the mouse is near the second rectangle
        if (path2.bounds.contains(mousePoint) && segment) {
          segment.remove();
          segment = new paper.Path.Line(path1.bounds.center, path2.bounds.center);
          segment.strokeColor = 'black';
        }
      };
  
      paper.view.draw();
    },
  };
</script>
  