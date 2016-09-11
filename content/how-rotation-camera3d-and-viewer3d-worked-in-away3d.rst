How rotation camera3d and viewer3d worked in Away3d
###################################################
:date: 2010-02-07 06:54
:author: Arul
:category: Flash
:tags: Animation, Flash, Programming, how to
:slug: how-rotation-camera3d-and-viewer3d-worked-in-away3d

**Rotation in Away3D Flash engine**

|image0|

In this blog entry we are going to learn about How the Rotation and camera3d and viewer3d in away3d flash engine.

Red line = x-axis

Blue line = y-axis

Green Line = z-axis

**How Rotation works ..?**

Rotation in away3d based on the three axis . Those are x.y and z.  the component is rotated take any one of this axis as a center then rotated. In my `last post <http://arulraj.net/2010/02/my-first-3d-flash-animation.html>`__\  the sphere is rotated along with x axis. In that example the axis is like that (see below )

.. raw:: html

	<embed src="http://files.arulraj.net/code/flash/away3d/singlerotate.swf" width="600" height="400">
	</embed>

.. code-block:: text

	sphere.rotationX = sphere.x + 1;

The sphere takes x axis as a center and rotate like above...

In this example we add two or more components in the ObjectContainer3D then rotate this objects. In this example we are going to learn about how camera3D and Viewer3D works.

.. raw:: html

	<embed src="http://files.arulraj.net/code/flash/away3d/away3drotate.swf" width="600" height="400">
	</embed>

**How Camera3D works ..?**

|image1|

	Camera3d = real camera

	view3d = lens the viewr of the camara

	renderer = recording in real cam

	scen3d = what we seen

This diagram explained in `Papervision3d Essential <http://books.sharedaa.com/2010/02/papervision3d-essentials.html>`__ book.. In this diagram your clearly understood about camera3d.

If we assume Camera 3d is like a real camera . we assume it is with in our application in invisible mode.

The viewerport (view3d) is an lens or what you are view using the camera.

The render engine is recording engine in the real camera. In the real camera If  we start the record then only we can see the changes otherwise not. Like same as in camera3d we called

.. code-block:: plain

	viewer.render()

method each time if anything changed in the components. In the real camara If any person is not inside the seen they are not come in the flim. Same as in the scene3d if we not add add any components in the scene 3d objects  it is not visible.

**How Viewer3D Works ..?**

Download the source code `click here <http://sites.google.com/site/arulraj1985/list-of-files/Away3drotate.zip?attredirects=0&d=1>`__\  (compatible for Flashdevelop IDE)

.. |image0| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/S26cXkz167I/AAAAAAAAALs/45u4Luu4aRE/s400/away3d+rotation+example.jpg
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/S26cXkz167I/AAAAAAAAALs/45u4Luu4aRE/s1600-h/away3d+rotation+example.jpg
.. |image1| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/S260xnBaV8I/AAAAAAAAAL0/sdpPCbRPy28/s400/camera3d.jpg
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/S260xnBaV8I/AAAAAAAAAL0/sdpPCbRPy28/s1600-h/camera3d.jpg
