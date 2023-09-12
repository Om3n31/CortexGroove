<template>
    <div>
      <canvas id="canvas" ref="canvas" class="border-2 border-white rounded-lg w-full"></canvas>
    </div>
  </template>
  
<script lang="ts">

  import * as paper from "paper";
import { Size } from "paper/dist/paper-core";

  export default {
    mounted() {
      // Initialize Paper.js
      paper.setup(document.getElementById('canvas') as HTMLCanvasElement);
  
      var initialWidth = 100;
      var initialHeight = 50;
      var maxWidth = 300; // Maximum width for the rectangle
      var maxHeight = 150; // Maximum height for the rectangle
      var textContent = 'This is a long text that should wrap if it exceeds the width and get truncated if it exceeds both width and height';

      var rectangle1 = new paper.Rectangle(new paper.Point(100, 100), new paper.Size(initialWidth, initialHeight));
      var path1 = new paper.Path.Rectangle(rectangle1, new paper.Size(10, 10));
      path1.style = new paper.Style({
        fillColor: new paper.Color('#525b76'),
        strokeColor: new paper.Color('#c4f1be'),
        strokeWidth: 2
      });

      // Create a PointText item and set its content and position
      var text = new paper.PointText({
        content: textContent,//'Vehicle recognition network', // Replace with your desired text
        fillColor: 'white',     // Set the text color
        fontFamily: 'Arial',    // Set the font family
        fontSize: 14,            // Set the font size
        point: path1.position    // Position the text at the center of the rectangle
      });

      text.position = path1.bounds.center;
      updateRectangleSize(text, rectangle1, path1);

      var rectangle2 = new paper.Rectangle(new paper.Point(300, 300), new paper.Size(100, 50));
      var path2 = new paper.Path.Rectangle(rectangle2);
      path2.fillColor = new paper.Color('blue');
  
      // Initialize variables to track segment and mouse position
      var segment: paper.Path.Line | null;
      var mousePoint = new paper.Point(0, 0);
      var isDragging = false;
  
      // Event handler for mouse down on rectangles
      path1.onMouseDown = path2.onMouseDown = function (event: any) {
        isDragging = true;
      };
  
      // Event handler for mouse up
      paper.view.onMouseUp = function (event: any) {
        isDragging = false;
        if (segment) {
          segment.remove();
          segment = null;
        }
      };
  
      // Event handler for mouse move
      paper.view.onMouseMove = function (event: any) {
        mousePoint = event.point;
      };
  
      // Main update function
      paper.view.onFrame = function (event: any) {
        if (isDragging) {
          if (segment) {
            segment.remove();
            segment = null;
          }
          segment = new paper.Path.Line(path1.bounds.center, mousePoint);
          segment.strokeColor = new paper.Color('black');
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
          segment.strokeColor = new paper.Color('black');
        }
      };
        
      function updateRectangleSize(text: paper.TextItem, rectangle: paper.Rectangle, rectanglePath: paper.Path) {
        
        let style = rectanglePath.style; //save style 

        var textBounds = text.bounds;
        var newWidth = Math.min(maxWidth, Math.max(initialWidth, textBounds.width + 20)); // Add some padding
        var newHeight = Math.min(maxHeight, Math.max(initialHeight, textBounds.height + 20)); // Add some padding

        // Truncate text if both width and height limits are reached
        if (newWidth === maxWidth && newHeight === maxHeight) {
          var maxLength = Math.floor((maxWidth - 20) / 14); // Adjust this value based on your font size
          text.content = textContent.substring(0, maxLength) + '...';
        }
        console.log(newWidth, newHeight)

        // Update the rectangle's size
        rectangle = new paper.Rectangle(new paper.Point(100, 100), new paper.Size(newWidth, newHeight));
        rectanglePath.remove();
        rectanglePath = new paper.Path.Rectangle(rectangle, new Size(10, 10));
        rectanglePath.style = style;
        rectanglePath.sendToBack();
        // Center the text within the updated rectangle
        text.position = rectanglePath.bounds.center;
      }
    }
  };
</script>
  
