Targets
===============================================================

Introduction
***************************************************************

The side-channel analysis provides very powerful attack mean that will adapt to very different kind of targets.
The targets are classified according to in which part of the SoC they live and which algorithm they perform.
As stated in the [Attack] part, the target we are interested in are CPU and FPGA accelerators.

In all cases the same correlation processing is performed on the leakage,
allowing the attacker to easily attempt to attack a wide variety of targets.

The project to attack commonly used software and hardware algorithms in order to evaluation their leakage.

Hardware
***************************************************************

In the case where the crypto-algorithm runs on the CPU located on the SoC we say that we perform a *hardware attack*.
In the demo application, the crypto-algorithm used a custom-made hardware AES128, it is a straightforward implementation
that is not protected against side-channel.

The hardware attack is the one that has been performed for long, the leakage is significant providing a high noise to signal ratio.
This attack is also very fast as the hardware crypto-algorithms runs generally very fast compared to a CPU.

Software
***************************************************************

In the case where the crypto-algorithm runs on the CPU located on the SoC we say that we perform a *software attack*.
In the demo application, the crypto-algorithm running is the well known tiny-AES, it is a straightforward implementation
that is very popular and does not feature side-channel counter-measure.

The software attack is significantly more difficult than the hardware one. This is caused by two factors :

- The decreased noise to signal ratio
- The increase in time required to perform computation

The first factor comes from the fact that the CPU is not only running instructions of pure AES computation 
and thus will add additional power consumption to the data.

The second factor comes from the fact that software implementations are generally slower than hardware implementations,
requiring more data to be processed and thus significantly increasing the attack time.


Our Setup
***************************************************************

As stated above, our setup provides a demo that attacks hardware and software implementation of the AES.
For the sake of evaluation we provided an AXI4 IP for the AES128, this IP can be connected to any AXI4 master interface
in order to provide software control of the accelerator.

We also integrated the tiny-AES in the demo as git sub-module the sources are directly compiled with the demo code.
For the sake of evaluation the tiny-AES can be controlled via the demo.