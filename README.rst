SCAbox Evaluation Framework
***************************************************************

.. raw:: html

    <p align="center">
    <img src="https://github.com/emse-sas-lab/SCAbox/blob/master/docs/sources/media/img/SCAbox_logo.png" height="250px">
    </p>
    
.. image:: https://img.shields.io/github/license/emse-sas/sca_framework
    :target: https://choosealicense.com/licenses/mit/
    :alt: license

`Official project website <https://emse-sas-lab.github.io/SCAbox/>`_ :fire:

SCAbox is a framework that provide *tools* and *materials* to perform FGPA-based side-channel analysis.
It provides software and hardware features gathered in a *heterogeneous* device that performs *acquisitions* and *attacks*.

*Only a Zynq-based development board is needed. All the side-channel analysis (SCA) acquisition is performed inside the SoC.*




Overview
---------------------------------------------------------------

Purposes
===============================================================

SCAbox aims at popularizing the FPGA-based SCA analysis by allowing simple experiment and development.
By using the SCAbox framework youwill be able to:

- **Familiarize** with SCA and co-design development.
- **Reproduce** attacks conducted in recent academic papers.
- **Build** your own FPGA-based side-channel sensors.
- **Characterize** the SCA leakage of your hardware and software algorithm implementations.

*The project is thought to be modular and adapted to the needs of both developers and researchers.*

If you are not familiar with Power SCA we provided various materials in the `wiki <https://emse-sas-lab.github.io/SCAbox/wiki/home.html>`_ to smoothly introduce you to the topic.
If you are already familiar with SCA we encourage you to take a look at our `tutorials <https://emse-sas-lab.github.io/SCAbox/tuto/home.html#tutorials>`_.

How ?
===============================================================

Our test-bench is based on sensors that use FPGA digital logic blocks available in the FPGA slices to capture the SoC voltage fluctuations.
These sensors are employed to eavesdrop the power leakage of a crypto-algorithm running in the FPGA or in the CPU.

*To learn more about how the bench and the SCA attacks works take a look at the wiki.*

Features
===============================================================

The SCAbox test-bench is meant to perform attack simulations on an SoC.
It allows to perform various SCA analysis related tasks.

- **Compute** crypto-algorithm runs using software and hardware
- **Capture** electrical power leakage with FPGA sensors
- **Transfer** leakage data via serial port
- **Export** leakage data to CSV
- **Attack** from serial port to key guess
- **Visualize** correlation and acquisition
- **Automate** attack and export using the GUI
- **Customize** the bench by integrating your own code

*Take a look at the repositories linked below to get an overview of the contents.*

Documentation
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

SCAbox is an open-source project, all the sources are hosted on GitHub and organized around various repositories

- `IP repository <https://github.com/emse-sas-lab/SCAbox-ip/>`_
- `Acquisition demo <https://github.com/emse-sas-lab/SCAbox-demo/>`_
- `Attack demo <https://github.com/emse-sas-lab/SCAbox-automation/>`_
- `SCAbox website  <https://github.com/emse-sas-lab/SCAbox/>`_

Each repository is provided with a technical documentation.
This website provide general documentation around the SCA topic and the test-bench

- Tutorials to install the bench, customize it and launch attacks
- Wiki to get introduced to the remote SCA and the bench architecture

*This way you can choose to get started with the part you are the most confortable with.*

Authors
===============================================================

Anonymous

Contributing
---------------------------------------------------------------

Please feel free to take part into SCAbox project, all kind of contributions are welcomed.

The project aims at gathering a significant number of IP cores, crypto-algorithms and attack models 
in order to provide an exhaustive view of today's remote SCA threat.

Software and embedded improvements are also greatly welcomed. Since the project is quite vast and invovles
a very heterogeneous technical stack, it is difficult to maintain the quality with a reduced size team.  

License
---------------------------------------------------------------

All the contents of the SCAbox project are licensed under the `MIT license <https://choosealicense.com/licenses/mit/>`_ provided in each GitHub repository.

Copyright (c) 2020 Anonymous
