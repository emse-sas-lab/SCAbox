.. figure:: media/img/SCAbox_logo.png
   :width: 250
   :alt: SCAbox logo
   :align: center
   :figclass: align-center


Welcome to SCAbox's documentation !
***************************************************************

SCAbox is an FPGA-based side-channel analysis framework dedicated to research and educational purposes. 

SCAbox aims at popularizing hardware security by enabling  SCA  experiments at low-cost using software-based hardware attacks. With the SCAbox framework you will be able to:

- **Familiarize** with SCA and co-design development.
- **Reproduce** attacks conducted in recent academic papers.
- **Build** your own FPGA-based side-channel sensors.
- **Characterize** the SCA leakage of your hardware and software algorithm implementation

For more information please check out our paper introducing SCAbox: PAPER_PATH

Content
---------------------------------------------------------------

This website provides a `series of tutorials <tuto/home.html>`_ in which you will learn how to setup and use the SCAbox framework.

Please follow the tutorial order to setup the framework. You can stop the tutorials at any step depending on your needs. The content of each tutorial is described below:

..
   from the Tuto#0 that avoid any programming to the most advanced that consists in building custom target IP cores.

- `Tuto #0 <tuto/download.html>`_ : Download the SCAbox Framework from GitHub.
- `Tuto #1 <tuto/test.html>`_ : Conduct your first FPGA-based side-channel attack using a pre-built SCAbox image. 
- `Tuto #2 <tuto/installation.html>`_ : Install the SCABox Framework using Vivado and Vitis tools.
- `Tuto #3 <tuto/acquisition.html>`_ : Use the framework to collect power leakage and conduct SCA attacks.
..
   - `Tuto #4 <tuto/create.html>`_ : Learn how to add a custom target IP to the SCABox framework.


..
   - Please follow the demonstration (Tuto#1) to get an overview of the SCAbox capabilities.
   - Please follow the advanced tutorials (Tuto #1, #2 and #3) to build and custom the framework. 

.. toctree::
   :maxdepth: 1
   :caption: Tutorials
   :hidden:

   tuto/home

..
   .. toctree::
   :maxdepth: 1
   :caption: Wiki
   :hidden:

   wiki/home
   
Cite
---------------------------------------------------------------

Anonymous