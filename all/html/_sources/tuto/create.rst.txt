#4 - Build your Own Designs
===============================================================
   
Goals
***************************************************************

In this tutorial you will learn how to add a custom target IP to the SCABox framework. Based on an example, you will learn how to build an AXI wrapper on top of your design to integrate it on SCABox. 

1. Download the target
2. Create the AXI IP core
3. Build the AXI IP core
4. Package the AXI IP core
5. Build the Vivado Project
6. Integrate the IP to the C program
7. Capture target side-channel leakage

Requirements
***************************************************************

You must have a complete the installation tutorial before starting this tutorial.
It is recommended to have an understanding of our hardware setup before starting the tutorial.

- Any terminal emulator such as PuTTY, TeraTerm or picocom
- Have a completed the installation tutorial
- Have an understanding of our hardware setup

Download the target
---------------------------------------------------------------

For this tutorial uses a publicly available FPGA implementation of the CRYPTON block cipher. The CRYPTON lightweight block cipher encrypts individual blocks of 64 bit length with a 64, 96, or 128 bit key.
1. Clone the CRYPTON algorithm from this address: https://github.com/huljar/mcrypton-vhdl.

Create the AXI IP core
---------------------------------------------------------------

1. Launch Vivado 
2. Open the SCABox project created in the previous tutorial
3. Click on **Tools > Create and Package New IP**
4. Hit **next** and select **Create AXI4 Peripheral** 
5. The peripheral must be configured with the following details then hit **next**:
	- Name: CRYPTON
	- Version: 1.0
	- Display name: CRYPTON_1.0
	- Description: CRYPTON Block cipher
	- IP location: your_path/SCAbox/sca-ip/ip_repo
6. In the next window, increase the register number to **16**, you can also modify AXI name to **S_AXI**, then hit **next**.
7. Finally, select **add IP to the repository** and hit **Finish**

The AXI IP Core has been created and you should be able to see it in the IP catalog. If not please add the **your_path/SCAbox/sca-ip/ip_repo** path to your IP repository path.

Build the AXI IP core
---------------------------------------------------------------

1. Enter the IP catalog 
2. **Right click** on the newly created CRYPTON_1.0 IP and select **Edit in IP Packager**. Hit **OK**. A new project window should open

In the new project you should see two VHDL source appear. The top one is will be the interface with the outside world. It also contains the AXI component that will handle the communication with the zynq processor. Now, we need to add the CRYPTON sources to the project.

3. Click on **File > Add Sources**
4. Select "Add or create design sources" then hit **next**
5. On the next window hit **+** and add all the CRYPTON sources except "axi_stream_wrapper.vhd" from the CRYPTON project **hdl** folder downloaded on github.
6. Hit **Finish**, the mycrypton_top module should appear on the Vivado Sources window.

Now we have to interface the CRYPTON module with AXI peripheral. First, we need **clock**, **done** and **start** signals for SCAbox to operate properly.

7. Modify the Crypton_v1_0 vhdl source file by adding **keysize** parameter and **clock**, **done** and **start** signals 

.. literalinclude:: media/code/crypton_v1_0.vhd
   :language: vhdl
   :lines: 5-21
   :emphasize-lines: 12-14

8. On the same file, Add the parameters to the AXI component and port map.

.. literalinclude:: media/code/crypton_v1_0.vhd
   :language: vhdl
   :lines: 50-61
   :emphasize-lines: 7-9
   
.. literalinclude:: media/code/crypton_v1_0.vhd
   :language: vhdl
   :lines: 88-99
   :emphasize-lines: 6-8
   
9. Now, on the CRYPTON_v1_0_S00_AXI vhdl source file, we need to modify the entity according to the new IOs.

.. literalinclude:: media/code/crypton_v1_0_S_AXI.vhd
   :language: vhdl
   :lines: 5-23
   :emphasize-lines: 14-16
   
10. Then we add the crypton module to our AXI peripheral

.. literalinclude:: media/code/crypton_v1_0_S_AXI.vhd
   :language: vhdl
   :lines: 91-100
   :emphasize-lines: 1-9

**Plaintext, ciphertext, key, done, start and reset** signals are read or written by the processor. We need to interface them using AXI registers 

11. First we need to create the signals that will serve as interface.

.. literalinclude:: media/code/crypton_v1_0_S_AXI.vhd
   :language: vhdl
   :lines: 121-131
   :emphasize-lines: 2-10

12. The signals flowing from the FPGA to the CPU are **done** and **ciphertext**. We connect them to any AXI register that is not use for reads.

.. literalinclude:: media/code/crypton_v1_0_S_AXI.vhd
   :language: vhdl
   :lines: 504-546
   :emphasize-lines: 19,21,33-34

12. The signals flowing from the CPU to the FPGA are **key**, **plaintext** and **start**. We connect them to any AXI register that is not use for writes.

.. literalinclude:: media/code/crypton_v1_0_S_AXI.vhd
   :language: vhdl
   :lines: 605-609
   :emphasize-lines: 1-4
   
13. To detect the end of the encryption we use a process that generates the done signal when the number of encryption clock cycle is reached

.. literalinclude:: media/code/crypton_v1_0_S_AXI.vhd
   :language: vhdl
   :lines: 567-603
   :emphasize-lines: 1-36

14. Finally, we add the port map of the CRYPTON module to establish the final connection

.. literalinclude:: media/code/crypton_v1_0_S_AXI.vhd
   :language: vhdl
   :lines: 611-620
   :emphasize-lines: 1-8
   
The IP is ready to be synthetized and packaged. 

Package the AXI IP core
---------------------------------------------------------------

1. Click **run synthesis** to verify that the IP has been properly created.
2. If no error or critical warning appear click **Package IP** else correct the errors. 
3. In the package IP identification window enter your ID 
4. In the file group window enter software drivers. 

You should see 6 files appear: Makefile, CRYPTON_selftest.c, CRYPTON.h, CRYPTON.c, CRYPTON.tcl, CRYPTON.mdd
These files will be used as software driver to control the CRYPTON IP from the processor. We need to modify them accordingly to the methodology adopted for the other SCAbox IPs.

6. In the yourpath/SCAbox/sca-ip/ip_repo/crypton_1.0/drivers/crypton_v1_0 folder, delete the data and hdl folders and replace then by the data and hdl folders used in yourpath/SCAbox/sca-ip/ip_repo/aes_1.0/drivers/aes_1.0

we are importing the base AES drivers in order to modify them and fit with the CRYPTON implementation

7. Replace "aes" with "crypton" in each file names and import them as software drivers: Right click on software driver > Add Files (use view all files)

You should have  Makefile, xcrypton.c, xcrypton.h, xcrypton_hw.h, crypton.tcl, crypton.mdd

8. Now, open each file and replace AES and aes occurence with CRYPTON and crypton occurences. (you can use ctrl+r on vivado to replace words, use match case for caps lock)

.. literalinclude:: media/code/xcrypton_hw.h
   :language: C
   
9. Package the IP and click on close project.

Build the vivado project
---------------------------------------------------------------

1. In the SCABox Vivado project open the **block design** 

2. Then, click on the IP catalog and right click on **AXI Peripheral** to hit **refresh all repositories**

   The CRYPTON block cipher should appear. 

3. Double click on CRYPTON IP and select **Add IP to Block Design**

4. Remove the previously used AES IP and replace its connections by those of the CRYPTON IP

5. Now the design is ready, you can click on generate bitstream 

6. On success, select **File > Export > Export** Hardware, (check **include Bitstream**)

7. Launch the SDK by selecting **File > Launch SDK**


Integrate the IP to the C program
---------------------------------------------------------------

1. On Xilinx SDK or Vitis, open the hw_platform project arborescence and open the drivers folder arborescence.

You should see the crypton software driver appear. 

2. Now right click on the BSP project and select **Re-generate BSP Sources**

You should see **crypton_v1_0** folder appear in **yourBSP/ps7_cortexa9_0/libsrc**

3. Now you can rebuild the C/C++ index **Project > C/C++index > Rebuild** and build all the projects **Project > Build All**

The project is now ready and will be modified to add CRYPTON ip core support.

4. Open the main.c file contained in SCABox/src/main.c and create the CRYPTON definition

.. code-block:: C

   #define SCABOX_TDC
   //#define SCABOX_RO
   //#define SCABOX_AES
   //#define SCABOX_PRESENT
   //#define SCABOX_KLEIN
   #define SCABOX_CRYPTON

5. Then you will have to add the crypton commands in main.c and main.h files. 

The procedure takes some time 

6. Once done, build the project and conenct through JTAG to the Zybo board.

Capture target side-channel leakage
---------------------------------------------------------------

1. Open a serial tool, connect to the Zybo at 921600 baudrate.

2. Test the crypton module with the following command: ``> crypton -m hw -k ffff -d ffff``

The result should be

