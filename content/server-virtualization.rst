Server Virtualization
#####################
:date: 2009-04-22 06:00
:author: arul
:category: Virtualization
:tags: cloud computing, Linux, xen
:slug: server-virtualization

**Server Virtualization**

***What is Virtualization..?***

| `Virtualization <http://en.wikipedia.org/wiki/Virtualization>`__\ is a
  technique of partitioning or dividing the resources of a single
|  server into multiple segregated execution environments. Each of these
  environments
|  runs independently of the other, thus allowing multiple operating
  systems to run on
|  the same hardware. This concept has been widely used in the world of
  mainframe
|  computers over the years.

***What is VMM (Virtual Machine Monitor)?***

| Each execution environment is called a guest and the server on
|  which they execute is called the host. The software running on the
  host that acts as
|  a bridge between the host and the guests, and that enables these
  multiple execution
|  environments is commonly referred to as the *Virtual Machine Monitor*
  (VMM) or
|  a *Hypervisor*.

***What are the Methods in Virtualization Technique ?***

| **System emulation:** The execution environment is called a virtual
  machine and
|  it emulates all the hardware resources. This emulation layer in turn
  uses the
|  real hardware resources from the host.

This approach Followed by :  `VMware <http://www.vmware.com/>`__,
`Microsoft virtual
PC <http://www.microsoft.com/Windows/products/winfamily/virtualpc/default.mspx>`__

| **Paravirtualization**: There is no hardware emulation. The operating
  system
|  that runs on a guest needs to be a modifed version that is aware of
  the
|  fact that it is running inside a hypervisor.

This approach Followed by : `Xen <http://www.xen.org/>`__

| **Operating System level virtualization**: Each guest instance is
  isolated and
|  runs in a secure environment. However, you can execute only multiple
|  instances of guests that run the same operating system as the host.

This approach Followed by : `Sun
Solaris <http://www.sun.com/software/solaris/virtualization.jsp>`__

***What is Xen?***

| Xen is an open-source paravirtualization technology that provides a
  platform for
|  running multiple operating systems in parallel on one physical
  hardware resource,
|  while providing close to native performance. Xen supports several
  operating
|  systems—Linux, FreeBSD and NetBSD. The current version of Xen also
  supports
|  the new generation of AMD Pacifca and Intel VT-x chipsets and can run
  an OS on
|  these chips without any modifcations by using a version of the
  hypervisor called
|  the *Hardware Virtual Machine* (HVM)

**What is HVM (Hardware Virtual Machine) ?**

| HVM mediates between the guest operating
|  system and the hardware and passes on the calls made by the guest to
  the physical
|  hardware.

Xen Architecture

|image0|

**Intel Server Virtualization Demo:**

Intel® Xeon® processors based on Intel® Core™ microarchitecture
integrate hardware for virtualization into all key server components
including `Intel® Virtualization
Technology <http://www.intel.com/technology/virtualization/server/index.htm?iid=tech_vt+server>`__
(Intel® VT) helping IT organizations consolidate more applications and
heavier workloads on each server to improve flexibility, reliability,
and total cost of ownership (TCO).

Intel® Virtualization Technology for servers Demo :

.. raw:: html

   <div align="center">

.. raw:: html

   <object width="320" height="240" data="http://www.intel.com/technology/virtualization/demos/closer/demo.swf" type="application/x-shockwave-flash">

.. raw:: html

   </object>

.. raw:: html

   </div>

Flexible virtualization

.. raw:: html

   <div align="center">

.. raw:: html

   <object width="320" height="240" data="http://www.intel.com/business/resources/demos/xeon5500/virtualization/demo.swf" type="application/x-shockwave-flash">

.. raw:: html

   </object>

.. raw:: html

   </div>

.. |image0| image:: http://4.bp.blogspot.com/_Tq9uaJI0Xww/Se8KOh04_5I/AAAAAAAAETY/Gkl-Ck_wpNo/s400/Xen+Architecture.jpg
   :target: http://4.bp.blogspot.com/_Tq9uaJI0Xww/Se8KOh04_5I/AAAAAAAAETY/Gkl-Ck_wpNo/s1600-h/Xen+Architecture.jpg
