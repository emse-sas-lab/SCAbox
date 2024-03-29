#1 - Run the Pre-Built Demo
===============================================================

**Duration:** 20-30 min

Goals
***************************************************************

In this tutorial you will conduct your first FPGA-based side-channel attack in three steps:

1. Download the Application Image
2. Launch the Demo
3. Collect the AES Leakage

**Summary:** This tutorial do not require any software tool installation or programming. It uses a pre-built boot image available on github that can be loaded into a micro SD card to launch the demo. The image contains an FPGA bitstream that embeds time-to-digital converter sensors (TDC) and a hardware AES. It also contains a software program that we will serve as an interface to communicate with your computer through serial port. At the end of this tutorial you will conduct a correlation power analysis attack using the AES leakage collected using TDCs.

Requirements
***************************************************************

- A Zynq board
- A micro SD card
- A micro USB cable 
- Any terminal emulator such as PuTTY, TeraTerm or picocom
- Python version :math:`\geq` 3.8
- `Tuto #0 <download.html>`_: Download the SCAbox Framework.

.. note::
	Because it uses pre-built images, this tutorial is board dependent. 
	Currently, two boards are supported: Digilent Zybo z7-10 and Digilent Zybo z7.

.. image:: media/img/zybo_setup.jpg
   :width: 400px
   :alt: Zybo setup
   :align: center

Emulator setup
***************************************************************

The terminal emulator allows to communicate via UART with the SoC.
It must be configured properly in order to work and allow command typing.
Bellow is given the emulator configuration used :

- port is        : /dev/ttyUSBx
- flowcontrol    : none
- baudrate is    : 921600
- parity is      : none
- databits are   : 8
- stopbits are   : 1
- local echo is  : yes

.. note::
	- If your terminal provide it, you can also use the local line edit.
	- Port name can vary according to your OS, eg. on windows its COMx 

Tutorial 
***************************************************************

The tutorial starts here

1. Load the boot image inside the SD card
---------------------------------------------------------------

1. **Insert** the SD card into your computer
2. **Format** the SD card. 
3. **Copy** the BOOT.bin image that matches your board reference
4. **Eject** the SD card

.. note::
   The folder containing the images is located in **your_path/SCAbox/SCAbox-demo/image**

2. Launch the Demo
---------------------------------------------------------------

1. Insert the SD card into the Zybo board card slot.
2. Place the jumper 5 in **SD** boot position
3. Connect the Zybo to your computer using the **micro USB cable**
4. Power on the Zybo and wait for the green led "**DONE**" to illuminate.

.. note::
	If the "DONE" led is off, press the "PS-SRST" button. If it remains off the image is probably not compatible with your board, or the SD card is not supported. Please check the requirement section at the beginning of this tutorial.

.. image:: media/img/zybo_programmed.jpg
   :width: 400
   :alt: Zybo programmed
   :align: center

5. Start the serial communication with the parameters given in the **Emulator setup** section at the beginning of this tutorial

6. Press the "PS-SRST" button, the following welcome message should appear

.. image:: media/img/SCA_Putty1.png
   :width: 400
   :alt: FIFO output simple
   :align: center

You can now use the available serial commands to perform AES encryptions, side-channel acquisitions, etc. If you want to learn more about available commands please follow the `Tuto #3 <acquisition.html>`_.

3. Collect the AES Leakage
---------------------------------------------------------------

To facilitate the data acquisition and visualisation SCAbox comes with a simple notebook. This jupyter notebook connects directly to the Zynq board through a serial communication and can exchange data and commands with the device.

.. note::
	You can install jupyter notebook using `pip install jupyterlab`

1. Open a terminal at the notebook path: **your_path/SCAbox/SCAbox-notebook/src**

2. Then launch jupyter-lab and click on scabox.ipynb

.. code-block:: shell

	$ jupyter-lab

The following view should appear:

.. image:: media/img/notebook_welcome.png
   :width: 800
   :alt: SCAbox jupyter demo
   :align: center

3. Import scabox SCA library by launching the following cell

.. code-block:: shell

	from scabox import *

4. Connect to your Zybo using the following cell
	
.. code-block:: shell

	zb = ZyboSerial(port=None,baudrate=921600, timeout=1)
	
5. Launch a demo cpa

- **n_trace**: 2500
- **chunk_size**: 250
- **n_sample**: 400
- **i_byte**: 0

.. code-block:: shell

	Demo.hw_aes_cpa_demo(zb,i_byte=0,n_trace=2500,n_sample=400,chunk_size=250)

This will launch 2500 AES acquisitions and compute CPA on the last round. 

.. image:: media/img/notebook_cpa_results.png
   :width: 800
   :alt: SCAbox jupyter demo cpa
   :align: center

Results are updated dynamically every 250 traces. The temporal correlation indicates the current key guess. 
On the right, the concord view shows the key guess progression over the number of traces used. Here it took less 
than 250 traces to extract the secret key byte. 

Conclusion
***************************************************************

You did it ! It was your first FPGA-based side-channel attack experience on SCAbox. Now you may be interested in creating your own designs. That's the topic addressed in the following tutorials.

Click **Next** to start the `Tuto#2 <installation.html>`_: Install the Framework.

