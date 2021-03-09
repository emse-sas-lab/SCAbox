SCABox Evaluation Framework
***************************************************************

.. image:: https://img.shields.io/github/license/emse-sas/sca_framework
    :target: https://choosealicense.com/licenses/mit/
    :alt: license


.. image:: https://img.shields.io/github/deployments/emse-sas/sca_framework/github-pages
    :target: https://emse-sas.github.io/sca_framework/
    :alt: pages

`Website <https://emse-sas.github.io/sca_framework/>`_

SCABox is a framework that provide *tools* and *materials* to perform side-channel analysis.
It provides software, embedded and hardware features gathered in a *hybrid* test-bench that performs *acquisitions* and *attacks*.

*Only a Zynq-like board is needed. All the SCA acquisition is performed inside the SoC.*

Overview
---------------------------------------------------------------

Purposes
===============================================================

SCABox aims at popularizing the SCA analysis by allowing easy experiment and development.
Furthermore it allows to replace oscilloscope based SCA test-bench with only an FPGA SoC.

- **Learn** SCA analysis and co-design development
- **Reproduce** the attacks achieved by state of the art
- **Characterize** the hardware security of your devices and software

*The project is thought to be progressive and adapted to the needs of both developers and scientists.*

If you are not familiar with SCA we provided a various materials in the wiki to smoothly introduce you to the topic.

If you are already familiar with SCA we encourage you to take a look at our tutorials.

If you want to get deep into the setup you can go to the technical documentations of the parts you are interested in. 

How ?
===============================================================

Our test-bench is based on sensors that leverage FPGA digital logic blocks available in the FPGA slices to capture the SoC voltage fluctuations.
These sensors are employed to eavesdrop the power leakage of a crypto-algorithm running in the FPGA or in the CPU.

*To know more about how the bench and the SCA attacks works take a look at the wiki.*

Features
===============================================================

The SCABox test-bench is meant to perform attack simulations on an SoC.
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

SCABox is an open-source project, all the sources are hosted on GitHub and organized around various repositories

- `IP repository <https://github.com/emse-sas/sca-ip/>`_
- `Acquisition demo <https://github.com/emse-sas/sca-demo-tdc-aes/>`_
- `Attack demo <https://github.com/emse-sas/sca-automation/>`_
- `SCABox website  <https://github.com/emse-sas/sca_framework/>`_

Each repository is provided with a technical documentation.
This website provide general documentation around the SCA topic and the test-bench

- Tutorials to install the bench, customize it and launch attacks
- Wiki to get introduced to the remote SCA and the bench architecture

*This way you can choose to get started with the part you are the most confortable with.*

Authors
===============================================================

Anonymous

More
===============================================================

SCABox is a project on the topic of side-channel analysis.
The goal of SCABox is to provide a cheap and efficient test-bench for side-channel analysis.

To know more about SCABox please visit our `website <https://emse-sas.github.io/sca_framework/>`_.
It provides a tutorials and a wiki about side-channel analysis.

SCABox is an open-source project, all the sources are hosted on GitHub

- `IP repository <https://github.com/emse-sas/sca-ip/>`_
- `Acquisition demo <https://github.com/emse-sas/sca-demo-tdc-aes/>`_
- `Attack demo <https://github.com/emse-sas/sca-automation/>`_
- `SCABox website  <https://github.com/emse-sas/sca_framework/>`_

Contributing
---------------------------------------------------------------

Please feel free to take part into SCABox project, all kind of contributions are welcomed.

The project aims at gathering a significant number of IP cores, crypto-algorithms and attack models 
in order to provide an exhaustive view of today's remote SCA threat.

Software and embedded improvements are also greatly welcomed. Since the project is quite vast and invovles
a very heterogeneous technical stack, it is difficult to maintain the quality with a reduced size team.  

License
---------------------------------------------------------------

All the contents of the SCABox project are licensed under the `MIT license <https://choosealicense.com/licenses/mit/>`_ provided in each GitHub repository.

Copyright (c) 2020 Anonymous
