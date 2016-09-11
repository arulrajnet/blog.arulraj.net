My first 3D flash animation
###########################
:date: 2010-02-04 03:58
:author: arul
:category: Flash
:tags: Animation, Flash, red5, Programming
:slug: my-first-3d-flash-animation

**3D Animathion**

|image0|

Adobe support for native 3D only in cs4. There are lot of opensource
flash `3d engines <http://flashenabledblog.com/2008/04/17/flash-3d-list-update/>`__ are there. I tried papervision3d and away3d. Both are quite well. There are lot more tutorials for both online for away3d tutorials  `click here <http://away3d.com/tutorials>`__ , for papervision3d download this `book <http://www.packtpub.com/article/3d-vector-drawing-and-text-papervision3d-part1>`__. I got the source code of away3d from the google code http://code.google.com/p/away3d/ and for papervison3d svn http://code.google.com/p/papervision3d/. I generate swc using the command. The red5 says about `away3d. <http://osflash.org/away3d>`__

.. code-block:: text

	D:\sdk\Away3D> compc -include-sources ./src -source-path ./src -target-player 10 -output Away3d.swc

Initially i got this error when compile away3d "Error: Type was not found or was not a compile-time constant: Vector. in away3d"

Then i added the -target-player 10 in command line is fix that error. I think away3d is better than papervision3d. Here is my first animation here

I'm using away3d here...

.. raw:: html

	<embed src="http://files.arulraj.net/code/flash/away3d/away3d.swf" width="600" height="400">
	</embed>	

Source Code:

.. code-block:: as3

	package {
	   import away3d.cameras.Camera3D;
	   import away3d.cameras.HoverCamera3D;
	   import away3d.cameras.TargetCamera3D;
	   import away3d.containers.ObjectContainer3D;
	   import away3d.containers.Scene3D;
	   import away3d.containers.View3D;
	   import away3d.core.math.Number3D;
	   import away3d.materials.BitmapMaterial;
	   import away3d.materials.WireColorMaterial;
	   import away3d.primitives.Cube;
	   import away3d.core.render.Renderer;
	   import away3d.primitives.Sphere;
	   import away3d.primitives.WireSphere;
	   import away3d.core.utils.Cast;
	   import away3d.core.utils.CastError;
	   import flash.display.Bitmap;
	   import flash.display.Sprite;
	   import flash.events.Event;
	   import flash.events.MouseEvent;
	   import flash.geom.Point;
	   /**
	    * 
	    * @author Arul
	    */
	   public class FirstApplication extends Sprite {
	      public var viewer: View3D;
	      public var scene: Scene3D;
	      public var camera: Camera3D;
	      public var cube: Cube;
	      public var sphere: Sphere;
	      public var wiresphere: WireSphere;
	      public var group: ObjectContainer3D;
	      public var material: WireColorMaterial;
	      public var bitmapMaterial: BitmapMaterial;

	      [Embed(source = "assets/favicon.jpg")] 
	      private var favicon: Class;
	      public var image: Bitmap = new favicon();

	      [SWF(backgroundColor = "#EEE8DA")]

	      public function FirstApplication() {
	         init3D();
	      }

	      public function init3D(): void {
	         stage.frameRate = 30;
	         camera = new Camera3D({
	            y: 400,
	            z: -1000
	         });
	         viewer = new View3D({
	            camera: camera,
	            x: 250,
	            y: 100,
	            z: 100
	         });
	         scene = new Scene3D();
	         cube = new Cube();
	         sphere = new Sphere();
	         wiresphere = new WireSphere();
	         group = new ObjectContainer3D();
	         material = new WireColorMaterial();
	         bitmapMaterial = new BitmapMaterial(Cast.bitmap(image));

	         material.color = 0xA6111D;

	         sphere.x = 100;
	         sphere.y = 50;
	         sphere.z = 100;
	         sphere.radius = 75;
	         sphere.bothsides = true;
	         sphere.material = material;
	         group.addChild(sphere);

	         wiresphere.x = 270;
	         wiresphere.y = 150;
	         wiresphere.z = 150;
	         wiresphere.radius = 75;
	         wiresphere.bothsides = true;
	         wiresphere.material = material;
	         group.addChild(wiresphere);

	         cube.x = 250;
	         cube.y = 250;
	         cube.z = 400;
	         cube.material = bitmapMaterial;
	         group.addChild(cube);

	         viewer.scene.addChild(group);
	         viewer.render();

	         addChild(viewer);

	         addEventListener(Event.ENTER_FRAME, groupRotation);
	         group.addEventListener(Event.ENTER_FRAME, sphereRotation);
	         //addEventListener(MouseEvent.MOUSE_DOWN, lookThere);
	      }

	      public function groupRotation(e: Event): void {
	         group.rotationX = group.x + 1;
	         group.applyRotations();

	         viewer.render();
	      }

	      public function sphereRotation(e: Event): void {
	         sphere.rotationX = sphere.x + 1;
	         sphere.applyRotations();

	         wiresphere.rotationZ = wiresphere.z + 1;
	         wiresphere.applyRotations();
	         viewer.render();
	      }

	      public function lookThere(e: MouseEvent): void {
	         var clickpoint: Point = new Point(e.stageX, e.stageY);
	         var hypothines: Number = Point.distance(new Point(0, 0), clickpoint);
	         var sine: Number = Math.asin(e.stageX / hypothines);
	         var cos: Number = Math.acos(e.stageY / hypothines);
	         camera.lookAt(new Number3D(e.stageX, e.stageY, hypothines));
	         /**
	          * Horizontal angle
	          */
	         camera.pan(cos);
	         /**
	          * vertical angle
	          */
	         camera.tilt(sine);
	         viewer.render();
	      }
	   }
	}

.. |image0| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/S2sZE9RI5AI/AAAAAAAAALA/sKwq2ehHqto/s400/away3d+example.jpg
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/S2sZE9RI5AI/AAAAAAAAALA/sKwq2ehHqto/s1600-h/away3d+example.jpg
