<template>
    <div>
      <canvas id="canvas" class="border-2 border-white rounded-lg w-full"></canvas>
    </div>
</template>
  
<script lang="ts">

  import * as paper from "paper";
import { Item, PaperScope, Rectangle } from "paper/dist/paper-core";

  export default {
  mounted() {
    // Initialize Paper.js
    paper.setup(document.getElementById('canvas') as HTMLCanvasElement);

    /* TODO : display existing neural networks
    let neuralNetworks: GraphicalNeuralNetwork[];

    neuralNetworks.forEach(element => {
        
    });

    */

    // TODO create neural networks from scratch

    // Create two rectangles
    let rectangle1: paper.Rectangle  = new paper.Rectangle(new paper.Point(100, 100), new paper.Size(100, 100));
    var path1 = new paper.Path.Rectangle(rectangle1);
    path1.fillColor = new paper.Color('red');

    var rectangle2 = new paper.Rectangle(new paper.Point(300, 100), new paper.Size(100, 100));
    var path2 = new paper.Path.Rectangle(rectangle2);
    path2.fillColor = 'blue';

    // Initialize variables to track segment and mouse position
    var segment;
    var mousePoint = new paper.Point(0, 0);
    var isDrawing = false;

    // Initialize circles at the center of the rectangle segments


    var firstCircle = new paper.Path.Circle(path1.bounds.rightCenter, 5);
    firstCircle.fillColor = 'white';

    var secondCircle = new paper.Path.Circle(path2.bounds.leftCenter, 5);
    secondCircle.fillColor = 'white';

    /*
    var circleSymbol = new paper.Symbol(new paper.Path.Circle(new paper.Point(0, 0), 5));
    circleSymbol.fillColor = 'black';
    var startCircle = circleSymbol.place();
    startCircle.position = path1.bounds.rightCenter.point;
    var endCircle = circleSymbol.place();
    endCircle.position = path2.bounds.leftCenter.point;
    */
    // Event handler for mouse down on the first rectangle
    path1.onClick = function (event) {
      if (!isDrawing) {
        isDrawing = true;
        segment = new paper.Path();
        segment.strokeColor = 'black';
        segment.strokeWidth = 3;
        segment.add(firstCircle.bounds.center);
        segment.add(mousePoint);
        segment.visible = true;
      }
    };

    // Event handler for mouse down on the second rectangle
    path2.onClick = function (event) {
        console.log('test3');
      if (isDrawing) {
            console.log("test");

            var segment2;

            segment2 = new paper.Path();
            segment2.strokeColor = new paper.Color('black');
            segment2.strokeWidth = 3;
            segment2.add(path1.bounds.rightCenter);
            segment2.add(path2.bounds.leftCenter);
            segment2.visible = true;
            segment2.smooth();
            segment.remove();

            isDrawing = false;
        };
    };

    // Event handler for mouse down in the void
    paper.view.onClick = function (event: any) {
        if (isDrawing && !rectangle1.contains(mousePoint) && !rectangle2.contains(mousePoint)) {
            console.log('test2');
            segment.remove();
            isDrawing = false;
        };
    };

    // Event handler for mouse move
    paper.view.onMouseMove = function (event: any) {
    mousePoint = event.point;
      if (isDrawing) {
        segment.segments[1].point = mousePoint;
      }
    };

    paper.view.draw();
  },
};

class GraphicalNeuralNetwork {

    public id: number
    public rectangle: paper.Rectangle;
    public path: paper.Path.Rectangle;
    public startPoint: paper.Point;
    public size: paper.Size;
    public color: paper.Color;
    public isFirst: boolean;
    public isLast: boolean;
    public leftHook: paper.Path.Circle | null;
    public rightHook: paper.Path.Circle | null;
    public links: GraphicalLink[];
    public inputs: number;
    public outputs: number;
    
    /*var firstCircle = new paper.Path.Circle(path1.bounds.rightCenter, 5);
    firstCircle.fillColor = 'white';
    */



    constructor(id: number, startPointX: number, startPointY: number, width: number, height: number, color: string, isFirst: boolean, isLast: boolean) {

       this.id = id;
       this.startPoint = new paper.Point(startPointX, startPointY);
       this.size = new paper.Size(width, height);
       this.color = new paper.Color(color);
       this.rectangle = new paper.Rectangle(this.startPoint, this.size);
       this.path = new paper.Path.Rectangle(this.rectangle);
       this.path.fillColor = this.color;
       this.isFirst = isFirst;
       this.isLast = isLast;
       this.rightHook = new paper.Path.Circle(this.path.bounds.rightCenter, 5);
       this.leftHook = new paper.Path.Circle(this.path.bounds.leftCenter, 5);
       this.links = [];
       this.inputs = 1;
       this.outputs = 1;
       

       if(this.isFirst) {
        this.leftHook = null;
       }

       if (this.isLast) {
        this.rightHook = null;
       }

    }

    public addLink(neuralNetwork: GraphicalNeuralNetwork): void {
        
        this.links.forEach(element => {
            if (element.toNetwork.id == neuralNetwork.id){
                throw new Error('link already exists');
            }
        });

        neuralNetwork.links.forEach(element => {
            if (element.fromNetwork.id == this.id){
                throw new Error('link already exists');
            }
        });

        if (this.outputs != neuralNetwork.inputs) {
            throw new Error('inputs number must match outputs number');
        }
        
        let link = new GraphicalLink(this, neuralNetwork);

        this.links.push(link);

        neuralNetwork.links.push(link);
        
        return;
    };

    public removeLink(neuralNetwork: GraphicalNeuralNetwork): void {

        let index: number = 0;

        this.links.forEach(element => {
            if (element.toNetwork.id == neuralNetwork.id){

                element.removeLink();
                neuralNetwork.removeLinkDistant(this);
                this.links.splice(index,1);
            }  
            index ++;
        });

        return;
    }
    
    public removeLinkDistant(neuralNetwork: GraphicalNeuralNetwork): void {
        let index: number = 0;

        this.links.forEach(element => {
            if (element.fromNetwork.id == neuralNetwork.id){

                this.links.splice(index,1);
            }  

            index ++;
        });

        return;
    }

  }

  class GraphicalLink {

    public fromNetwork: GraphicalNeuralNetwork;
    public toNetwork: GraphicalNeuralNetwork;
    public segment: paper.Path | null;

    constructor(fromNetwork: GraphicalNeuralNetwork, toNetwork: GraphicalNeuralNetwork) {
        this.fromNetwork = fromNetwork;
        this.toNetwork = toNetwork;
        this.segment = new paper.Path();
        this.segment.strokeColor = new paper.Color('black');


        if (this.fromNetwork.rightHook)
            this.segment.add(this.fromNetwork.rightHook.bounds.center);

        if (this.toNetwork.leftHook)
            this.segment.add(this.toNetwork.leftHook.bounds.center);

        this.segment.visible = true;
        this.segment.smooth();

    }

    public removeLink() : void {

        if(this.segment)
            this.segment.visible = false;
            this.segment = null;

        return;
    };

  }

</script>

