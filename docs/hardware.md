# Hardware & Technical Environment

## Overview

All teams will develop and demonstrate their systems using the **g.tec Unicorn Hybrid Black** EEG headset.  
Each team will be allocated **one Unicorn system** for the duration of the event (Friday 16th and Monday 19th, the weekend will be without the headset.).

This document defines:
- Supported hardware
- Recommended software stack
- Streaming and integration constraints
- What organisers **will** and **will not** support during the hackathon

Teams are expected to **familiarise themselves with the Unicorn ecosystem in advance**.  
This event is not an introductory training workshop.

---

## EEG Hardware

### g.tec Unicorn Hybrid Black

Each Unicorn system includes:
- 8 EEG channels + reference + ground  
- Dry electrodes  
- Wireless transmission  
- Battery-powered operation  

**Important characteristics**
- Consumer-grade research hardware
- Sensitive to electrode contact quality
- Sensitive to movement and environmental noise
- Designed for rapid setup, not clinical-grade stability

Official resources:
- Unicorn Recorder Hybrid Black (GitHub):  
  https://github.com/unicorn-bi/Unicorn-Recorder-Hybrid-Black
- g.tec official setup tutorials (video):  
  https://www.gtec.at/unicorn-hybrid-black-video-tutorials/

Teams should assume **non-ideal signal conditions** and design control strategies accordingly.

---

## Data Streaming & Communication

### Lab Streaming Layer (LSL)

**LSL is the recommended and supported data transport layer for this hackathon.**

All teams should assume:
- Real-time EEG access via LSL streams
- Synchronisation via LSL timestamps
- Interoperability with audio, visual, or control software via LSL

Introductory reference:
- MNE-LSL introduction:  
  https://mne.tools/mne-lsl/stable/generated/tutorials/00_introduction.html
- Python API repo: pylsl 
  https://github.com/chkothe/pylsl/tree/master
- Python Package Installation:
  https://pypi.org/project/pylsl/


LSL is widely used in BCI research and is the most robust option for rapid integration under time constraints.

---

### Unicorn → LSL Streaming

Multiple established approaches exist for streaming Unicorn data into LSL. Teams may use **any method**, provided it is **stable, reproducible, and demonstrable**.

Recommended references:
- Python + pylsl implementation (Rob Oostenveld):  
  https://robertoostenveld.nl/unicorn2lsl/
- FieldTrip real-time Unicorn streaming:  
  https://www.fieldtriptoolbox.org/development/realtime/unicorn/
- Python data collection walkthrough (Medium guide):  
  https://medium.com/the-ultimate-bedroom-bci-guide/collecting-brain-signal-data-using-the-g-tec-unicorn-eeg-headset-in-python-65240c741693

⚠️ **Critical Note**  
Organisers will **not debug custom streaming pipelines on the day**.  
If you choose a non-standard or experimental approach, reliability is your responsibility.

---

## Supported Software Environments

### Operating Systems
- **Windows 10 / Windows 11** (recommended)
- macOS / Linux: possible, but **not guaranteed** to be supported onsite

### Programming Languages
- **Python** (strongly recommended)
- MATLAB (acceptable, particularly with FieldTrip)
- Other languages are allowed but **unsupported**

### Common Libraries & Tools
- pylsl
- NumPy / SciPy
- MNE / MNE-LSL
- Audio / MIDI / OSC libraries of your choice
- DAWs or synthesis environments (optional)

Teams should arrive with **all dependencies pre-installed and tested**.

---

## Audio & Musical Output

Teams are free to choose their musical output modality, including:
- MIDI instruments
- Software synthesizers
- Digital Audio Workstations (DAWs)
- Algorithmic or generative sound systems
- External audio hardware

**Constraints**
- Audio output must be **self-contained**
- Teams must bring:
  - Their own laptops
  - Any required audio interfaces
  - Headphones or speakers (if required)

Venue AV systems support **standard stereo audio only**.

---

## Latency & Performance Expectations

There is **no fixed latency requirement**, but judging will consider:
- Stability of control
- Responsiveness
- Robustness under live conditions

Teams should design systems that tolerate:
- Noisy EEG
- Brief signal dropouts
- Variable electrode contact quality

Pipelines that only work under ideal laboratory conditions are **high-risk**.

---

## On-Site Support

### What Will Be Provided
- g.tec Unicorn Hybrid Black systems
- Basic assistance with:
  - Hardware setup
  - Sensor placement
  - Connectivity issues

### What Will NOT Be Provided
- Custom software debugging
- Signal processing consultation
- Machine learning troubleshooting
- Audio engineering support
- Spare laptops, cables, or peripherals

This is a **development and demonstration event**, not a training course.

---

## Strong Recommendations

Teams are strongly advised to:
- Test their **full pipeline end-to-end** before arrival
- Have a **fallback or degraded mode**
- Be able to:
  - Visualise EEG signals live
  - Confirm LSL connectivity quickly
  - Recover gracefully from brief failures

Backup plans are explicitly evaluated in the judging rubric.

---

## Final Note

If your system:
- Requires perfect EEG signals
- Requires prolonged calibration
- Cannot tolerate brief data loss

…it is unlikely to perform well in a live setting.

Design accordingly.
