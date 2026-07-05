# System Architecture

## Overview
The FPGA Graphing Calculator implements a heterogeneous system architecture leveraging both the Programmable Logic (PL) and Processing System (PS) of the Xilinx Zynq-7000 SoC. This architecture optimizes performance by assigning computationally intensive tasks to hardware accelerators in the FPGA while using the ARM Cortex-A9 processors for control flow, user interface, and system coordination.

## Hardware/Software Partitioning Rationale

### FPGA (Programmable Logic) Responsibilities
The FPGA is responsible for computationally intensive, data-parallel, and real-time critical operations:

1. **Floating-Point Arithmetic Acceleration**
   - IEEE 754-2008 compliant single-precision floating-point adder and multiplier
   - Pipelined implementation achieving >200 MHz Fmax
   - Hardware support for subnormal numbers, infinity, NaN detection and propagation
   - Status flag generation (invalid operation, overflow, underflow, division by zero, inexact)

2. **Fixed-Point Arithmetic**
   - Configurable precision fixed-point units for known-range operations
   - Lower latency and resource utilization compared to floating-point for specific use cases
   - Parameterizable word length and fractional bits

3. **Coordinate Transformations**
   - Hardware-accelerated rotation, scaling, and translation for real-time pan/zoom operations
   - CORDIC-based implementations for trigonometric and hyperbolic functions
   - Matrix multiplication for affine transformations

4. **Signal Processing & Waveform Generation**
   - Numerically controlled oscillators (NCOs) for function evaluation
   - Filtering and interpolation units for smooth curve rendering
   - Delta-sigma modulators for audio output generation

5. **Graph Rasterization Acceleration**
   - Edge evaluation and fill rule hardware for polygon rendering
   - Anti-aliasing subpixel precision units
   - Z-buffer or painter's algorithm hardware for 3D extensions (future)

6. **Custom Math Coprocessors**
   - Special function units (exp, log, trig) using polynomial approximation or CORDIC
   - Lookup table-based units with interpolation for transcendental functions
   - Polynomial evaluation units using Horner's method

### ARM Processing System (PS) Responsibilities
The ARM Cortex-A9 processors handle control-intensive, sequential, and user-facing operations:

1. **Operating Logic & System Control**
   - Boot sequence and system initialization
   - Power management and clock configuration
   - Error handling and fault detection/recovery
   - Debug and diagnostic services

2. **Menu System & User Interface**
   - Touchscreen and button input processing
   - GUI rendering and widget management
   - Menu navigation and dialog handling
   - Theme and layout management

3. **Graph Management & Data Handling**
   - Expression storage and variable management
   - Function catalog and user-defined function handling
   - Graph parameter management (range, resolution, style)
   - History and recall capabilities

4. **Memory Allocation & Resource Management**
   - Heap management for dynamic data structures
   - Memory pool allocation for fixed-size objects
   - Buffer management for DMA transfers
   - Memory protection and isolation

5. **File Handling & Storage**
   - Filesystem interface for saving/loading workspaces
   - Serial communication protocols (USB, UART)
   - SD card access for persistent storage
   - Data serialization and deserialization

6. **Rendering Coordination & Display Management**
   - Framebuffer management and page flipping
   - Synchronization with display timing controllers
   - Layer composition and alpha blending
   - Power-saving display modes

7. **Communication with FPGA (PS-PL Interface)**
   - Configuration and control register access via AXI-Lite
   - Command queuing and status monitoring
   - Interrupt handling for FPGA-generated events
   - Debug and trace data transfer

8. **System Services**
   - Timekeeping and scheduling services
   - Memory protection unit (MPU) configuration
   - Interrupt controller management
   - Cache maintenance and coherence operations

## Expected Performance Improvements

### FPGA Acceleration Benefits
- **Floating-Point Operations**: 10-100x speedup compared to software implementation
  - Software FP addition: ~200-500 cycles on Cortex-A9
  - Hardware FP addition: 3-5 cycles with pipelining
- **Fixed-Point Operations**: 5-50x speedup for known-range calculations
- **Coordinate Transformations**: 20-100x speedup for real-time manipulation
- **Expression Evaluation**: Overall 5-20x speedup for complex mathematical expressions
- **Deterministic Latency**: Hardware execution provides predictable timing critical for real-time interaction

### Software Maintainability Benefits
- **Isolation of Concerns**: Clear separation between compute-intensive hardware and control-intensive software
- **Reduced Software Complexity**: Offloading complex algorithms to hardware simplifies software implementation
- **Independent Optimization**: Hardware and software teams can optimize their respective domains separately
- **Easier Testing**: Hardware accelerators can be unit-tested in isolation with testbenches
- **Clear Interfaces**: Well-defined AXI boundaries simplify integration and debugging

### Scalability Considerations
- **Parameterizable Designs**: Most FPGA modules are parameterizable for different precision/performance points
- **Resource Headroom**: Current utilization leaves room for additional features or increased precision
- **Performance Headroom**: Timing closure achieved with margin allows for frequency scaling or feature addition
- **Architectural Extensibility**: AXI-based design allows easy addition of new peripherals or accelerators

## Communication Mechanisms

### AXI Lite (AXI-Lite)
Used for low-bandwidth, register-based control and status interfaces:

- **FPGA Configuration Registers**
  - Mode selection and configuration of arithmetic units
  - Precision and format controls
  - Enable/disable controls for power management
  - Status registers for busy/ready flags and error indicators

- **Software Access Pattern**
  - Non-blocking reads/writes for status polling
  - Interrupt-driven updates for event notification
  - Minimal latency overhead (~10-20 cycles for read/write)
  - Suitable for infrequent control operations

### AXI Memory Mapped (AXI-MM)
Used for high-bandwidth data transfers between PS and PL:

- **Framebuffer Data Transfer**
  - Transfer of rendered graphics data from software framebuffer to display hardware
  - Transfer of vertex data or function points for hardware rasterization
  - Utilizes burst transfers for efficient bandwidth usage
  - Typically unidirectional (software→hardware for display)

- **Shared Memory Buffers**
  - Double/triple buffered framebuffers for tear-free display
  - Command queues for software-to-hardware instruction passing
  - Result queues for hardware-to-software feedback (e.g., hit detection)
  - Utilizes cache coherence mechanisms when applicable

- **Burst Characteristics**
  - Supports INCR, WRAP, and FIXED burst types
  - Burst lengths up to 16 beats for efficient DDR3 utilization
  - Address alignment considerations for optimal performance

### AXI Stream (AXI-Stream)
Used for real-time, streaming data interfaces:

- **Video Data Transport**
  - Unidirectional stream from video timing generator to HDMI transmitter
  - Carries pixel data, synchronization signals, and data enable
  - Supports backpressure through ready/valid handshake
  - Optimized for continuous, isochronous data flow

- **Audio Data Transport**
  - I2S audio stream from FPGA to audio codec
  - Carries serialized audio samples with word select and clock
  - Supports flexible sample rates and bit depths
  - Utilizes FIFO buffering for jitter reduction

- **Debug and Trace Streams**
  - Instrumentation data output for performance monitoring
  - Event tracing for real-time system analysis
  - Configurable bandwidth and sample rates

### Interrupts
Used for event notification and asynchronous signaling:

- **FPGA to PS Interrupts**
  - Computation completion signals (e.g., "graph ready")
  - Error conditions (e.g., arithmetic overflow, memory errors)
  - Input events (e.g., touchscreen pen down, button press)
  - Timer expirations for periodic tasks

- **PS to FPGA Interrupts** (less common, but possible)
  - Configuration change notifications
  - Command availability signals
  - Synchronization signals for coordinated operations

- **Interrupt Management**
  - Prioritized interrupt controller in PS
  - Vectored interrupt handling for low latency
  - Ability to mask/enable interrupts based on system state
  - Interrupt service routines (ISRs) kept short with deferral to task level

### Direct Memory Access (DMA)
Used for efficient bulk data transfer without CPU intervention:

- **AXI DMA Engine**
  - Configured by PS to transfer data between DDR3 and FPGA peripherals
  - Supports memory-to-memory, memory-to-peripheral, and peripheral-to-memory transfers
  - Scatter-gather capability for non-contiguous buffer transfers
  - Interrupt on completion or error conditions

- **Use Cases**
  - Transfer of large function evaluation tables from DDR3 to FPGA lookup tables
  - Transfer of captured waveform data from ADC to DDR3 for storage
  - Transfer of pre-rendered graphics layers for composition
  - Transfer of audio samples from DDR3 to I2S transmitter

- **Advantages**
  - Zero-copy transfers reducing CPU overhead
  - Continuous throughput utilization of memory bandwidth
  - Allows CPU to perform other tasks during transfer
  - Precise timing control for isochronous data (audio/video)

## Memory Map and Addressing

### AXI-Lite Register Map (Example)
```
0x4000_0000 - 0x4000_FFFF: Custom Math Accelerator
  0x4000_0000: Control Register (start, reset, mode)
  0x4000_0004: Status Register (busy, error flags)
  0x4000_0008: Operand A Input
  0x4000_000C: Operand B Input
  0x4000_0010: Result Output
  0x4000_0014: Precision/Format Configuration

0x4001_0000 - 0x4001_FFFF: Display Pipeline
  0x4001_0000: Video Timing Configuration
  0x4001_0004: Framebuffer Address Register
  0x4001_0008: Display Control (enable, test pattern)
  0x4001_000C: Status Register (vsync, hsync active)
  0x4001_0010: Interrupt Enable/Status
  0x4001_0014: Color/Gamma Correction Registers

0x4002_0000 - 0x4002_FFFF: Memory Arbiter & Controller
  0x4002_0000: Memory Controller Configuration
  0x4002_0004: Arbiter Priority Settings
  0x4002_0008: Memory Status (refresh, errors)
  0x4002_0010: Performance Counters (read/write bandwidth)
```

### Shared Memory Regions
- **Framebuffer Region**: DDR3 address range allocated for display buffers
- **Command Queue Region**: Circular buffer in DDR3 for software→FPGA commands
- **Response Queue Region**: Circular buffer in DDR3 for FPGA→software responses
- **Lookup Table Region**: DDR3-resident tables copied to FPGA BRAM/URAM as needed
- **Heap Region**: Standard heap for dynamic allocation in embedded software

## Clocking and Reset Strategy

### Clock Domains
- **CPU_6x6x_PL_CLK**: 150 MHz - Main system clock for FPGA logic
- **FPGA0_CLK**: 100 MHz - Optional secondary clock for specific peripherals
- **REF_CLK**: 200 MHz - Reference clock for clock generators and serial transceivers
- **DDR3_CLK**: 400 MHz - DDR3 memory interface clock (200 MHz DDR rate)
- **VIDEO_CLK**: 148.5 MHz - HDMI pixel clock for 1080p60
- **AUDIO_CLK**: Variable - Based on audio sample rate (e.g., 12.288 MHz for 48kHz audio)

### Reset Strategy
- **PS_POR_B**: Power-on reset from PS (active low)
- **PL_RESET_AND_RESET_N**: Combined reset from PS to PL (active low reset, active high reset_n)
- **Local Resets**: Module-specific resets derived from PL reset with synchronization
- **Reset Synchronization**: Two-stage synchronizers for asynchronous reset deassertion
- **Reset Sequencing**: Proper ordering to ensure stable power clocks before reset release

## Power Management Considerations

### FPGA Power Domains
- **VCCINT**: 1.0V - FPGA core power (dynamic based on utilization)
- **VCCBRAM**: 1.0V - Block RAM power
- **VCCAUX**: 1.8V - Auxiliary circuits (I/O buffers, clock management)
- **VCCO**: Variable - I/O bank powers based on interface standards

### Power Optimization
- **HP Banks**: 1.8V for DDR3 interfacing
- **HR Banks**: 3.3V for HDMI, GPIO, and other peripherals
- **MGTAVTT/ MGTAVFF**: 1.2V/0.9V for GTP transceivers (HDMI)

### Power Reduction Techniques
- **Clock Gating**: Disable clocks to idle modules
- **Block RAM Shutdown**: Power down unused BRAM columns
- **Dynamic Voltage and Frequency Scaling (DVFS)**: Adjust based on performance requirements
- **Selective Module Power Down**: Power off entire subsystems when not in use (future expansion)
- **I/O Optimization**: Minimize transitions on unused I/O pins

## Thermal and Reliability Considerations

### Thermal Management
- **Power Dissipation Estimation**: <1.5W typical for FPGA fabric under load
- **Junction Temperature Monitoring**: Utilize on-die temperature sensors
- **Thermal Throttling**: Reduce performance if temperature exceeds safe limits
- **Heat Sink Requirements**: Ensure adequate cooling for sustained operation
- **Thermal Cycling**: Design for expected operational temperature ranges

### Reliability Features
- **Error Detection Codes (EDC)**: Parity or ECC on critical memory buffers
- **Watchdog Timers**: Monitor for system lockups
- **Built-In Self Test (BIST)**: Power-on self test for critical hardware
- **Redundancy**: Triple modular redundancy (TMR) for critical control logic (future consideration)
- **Radiation Hardening**: Not required for terrestrial consumer device, but design practices considered

## Design Constraints and Assumptions

### Performance Targets
- **FPGA Fmax**: ≥150 MHz with timing slack >0.1ns
- **Expression Evaluation Latency**: <10ms for 95% of test cases
- **Graph Refresh Rate**: ≥30 FPS for moderately complex functions
- **Boot Time**: <2 seconds from power-on to interactive state
- **Audio Latency**: <10ms for interactive audio feedback

### Resource Constraints
- **LUT Utilization**: <70% to allow for future feature expansion
- **FF Utilization**: <65%
- **DSP Utilization**: <60% (preserving resources for additional math units)
- **BRAM Utilization**: <60% (leaving room for lookup tables and buffers)
- **Power Consumption**: <2.5W total system power

### I/O and Interface Constraints
- **HDMI Output**: TMDS differential pairs at 1.485 Gbps per channel
- **DDR3 Interface**: Following MIPS specification for Zybo Z7
- **GPIO**: 3.3V logic with configurable drive strength and slew rate
- **USB OTG**: High-speed (480 Mbps) device/host capability
- **Ethernet**: 10/100/1000 Mbps via PS-GEM

### Environmental Assumptions
- **Operating Temperature**: 0°C to 40°C (consumer device range)
- **Storage Temperature**: -20°C to +60°C
- **Humidity**: 5% to 95% non-condensing
- **Altitude**: Up to 2000 meters
- **Shock and Vibration**: Consumer handling levels

## Future Expansion Considerations

### Hardware Expansion Points
- **AXI-Lite Slave Interfaces**: Additional address ranges available for new peripherals
- **AXI-Stream Interfaces**: FIFO-based interfaces for streaming data
- **AXI-MM Master/Slave**: Additional memory-mapped access points
- **Interrupt Expanders**: Additional interrupt lines available
- **Unused I/O Pins**: Several GPIO pins available for future peripherals
- **MGT Sites**: Additional transceiver sites for high-speed serial interfaces

### Software Expansion Points
- **HAL Extension Points**: Well-defined interfaces for adding new device drivers
- **Filesystem Abstraction**: Easy addition of new storage media
- **UI Framework**: Widget-based design allows easy addition of new controls
- **Plugin Architecture**: Future extension for user-defined functions or features
- **Network Stack**: Addition of TCP/IP capabilities for connected features

### Performance Scaling Options
- **Increased Parallelism**: Additional FPGA instances of arithmetic units
- **Higher Precision**: Migration to double-precision floating-point
- **Increased Throughput**: Wider data paths or higher clock frequencies
- **Advanced Algorithms**: More sophisticated approximation or iterative methods
- **Hardware/Software Tradeoff Adjustment**: Rebalancing based on profiling data

This architecture provides a solid foundation for a high-performance graphing calculator while maintaining flexibility for future enhancements and demonstrating professional heterogeneous system design practices.