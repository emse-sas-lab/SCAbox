Acquisition
===============================================================

Introduction
***************************************************************

The side-channel acquisition consists on transferring the data between the remote sensors and the attacker CPU.
The acquisition is perform on the remote SoC, but the attack can be anywhere the leakage can be communication :

- Via any bus or serial connection
- Via network
- Directly inside CPU

Ideally, the remote sensors are sampled at the similar instants during each victim's encryption run.
To perform an attack the data of the sensors must be acquired during different victim's encryption run.
We call this process *iterating* acquisition. Each run is an *iteration* providing a *trace* representing the power leakage. 

Triggering
***************************************************************

The triggering consist on launching the sensor acquisition at the right instants to capture crypto-algorithm runs.
The triggering must be done at the same instants during each iteration in order to latter perform consistent correlation between iterations.

Data transfer
***************************************************************

The data transfer consist on sending the sampled from the sensors from the fabric to the attacker CPU.
The attacker CPU is not necessarily located on the SoC of the fabric.
Indeed, performing the CPA is a computationally expensive task regarding the count traces required,
whereas CPU ressources on the SoC are often limited.

Thus, the data transfert must be performed from the fabric to a more powerful CPU passing thought the CPU available on the SoC.

Sensor location
***************************************************************

It is observed that the sensors capture better traces when located near the target device.

Sensor sizing
***************************************************************

It is observed that the sensors capture better traces when they are more present. 

Noise to signal
***************************************************************

The side-channel acquisition is not subject to usual signal constraints that characterize a correct acquisition

- No need for the sampling frequency to be twice the Shannon frequency
- No need for constant sampling frequency

However the noise to signal ratio can be high when the sensor sizing or location cannot be optimal.
Futhermore, due to the presence of the CPU, the PDN gets noised by non-targeted activity even in an optimal configuration.
Thus, signal filtering is key in the attack process. It must ideally be adapted to the physical state and structure of the SoC.

Regarding this matter, two approaches have been considered :

- Spectrum analysis from experiments
- Noise deconvolution

Our Setup
***************************************************************