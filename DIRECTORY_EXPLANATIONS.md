# Directory Explanations

## .github/
Contains GitHub-specific configuration for issue templates, pull request templates, and CI/CD workflows.
- `ISSUE_TEMPLATE/`: Standardized issue templates for bug reports, feature requests, and documentation requests to ensure consistent reporting.
- `PULL_REQUEST_TEMPLATE/`: Templates for different PR types (bug fix, feature, documentation) to guide contributors in providing necessary information.
- `workflows/`: GitHub Actions workflow files for continuous integration (ci.yml), nightly builds (nightly.yml), and release automation (release.yml).

## docs/
Central repository for all project documentation.
- `architecture/`: Architectural documentation including Architecture Decision Records (ADR), block diagrams, sequence diagrams, and state machine diagrams.
- `datasheets/`: Component datasheets for reference (Zynq-7000, HDMI transmitter, audio codec, etc.).
- `diagrams/`: Source diagram files (drawio) and exported formats (PDF, PNG, SVG).
- `meeting_notes/`: Minutes from design reviews, sprint planning, and technical discussions.
- `standards/`: Project-wide standards documents covering coding conventions, commit messages, and documentation practices.

## embedsw/
Embedded software component targeting the ARM Cortex-A9 Processing System.
- `bsp/`: Board Support Package containing low-level hardware initialization and pinmux configuration specific to Zybo Z7.
- `drivers/`: Device drivers for peripherals (AXI DMA, GPIO, I2C, timer, HDMI transmitter, I2S audio, VDMA).
- `hal/`: Hardware Abstraction Layer providing a consistent API for accessing hardware peripherals, divided into include (headers) and src (implementation).
- `libraries/`: Reusable software libraries:
  - `math/`: Fixed-point and floating-point math libraries, polynomial evaluation routines.
  - `parser/`: Expression parsing and function evaluation libraries.
  - `graph/`: Graphing engine and rasterization libraries.
  - `ui/`: User interface components including themes and widget library.
- `apps/`: Application-specific code:
  - `calculator/`: Main calculator application with source files for main loop, menu system, graphing functionality, and utilities.
- `boot/`: Boot code including assembly startup script, linker script, and build scripts for creating bootable binaries.

## fpga/
FPGA design targeting the Programmable Logic of the Zynq-7000.
- `src/`: Source code for FPGA design.
  - `hdl/`: Hardware Description Language source.
    - `rtl/`: Register Transfer Level code organized by functionality:
      - `arithmetic/`: Floating-point adder/multiplier, fixed-point arithmetic, CORDIC for trigonometric functions.
      - `display/`: HDMI encoder, VGA timing generator, framebuffer management.
      - `memory/`: DDR3 memory controller and memory arbiter.
      - `axi/`: AXI interface components (AXI-Lite for register access, AXI-Stream for video data, AXI-MM for memory-mapped access).
      - `utils/`: Synchronizers, clock dividers, and other utility modules.
    - `sim/`: Simulation environment:
      - `testbenches/`: Verilog testbenches for each module.
      - `scripts/`: Simulation scripts for running tests.
    - `tb/`: Testbench support files including test data vectors and golden reference outputs.
  - `ip/`: Custom IP cores packaged for Vivado IP integrator:
    - `custom_math_accelerator/`: Hardware accelerator for mathematical operations.
    - `display_pipeline/`: Hardware pipeline for display processing.
  - `bd/`: Block Design files:
    - `system.bd`: Top-level block design integrating PS and PL.
    - `ip_repo/`: Repository for custom IP used in block design.
- `vivo/`: Vivado project files and scripts.
  - `projects/`: Vivado project directory for Zybo Z7.
    - `src/`: Constraint files and other project sources.
    - `constrs/`: Xilinx Design Constraints (.xdc) files for pin timing and I/O standards.
    - `runs/`: Synthesis and implementation run directories.
    - `impl/`: Implementation subdirectories.
    - `scripts/`: Tcl scripts for automating Vivado flows (block design creation, bitstream generation, simulation).
  - `doc/`: FPGA-specific documentation:
    - `specs/`: FPGA design specification and AXI interface specification.
    - `reports/`: Synthesis and implementation reports organized by run type.
- `utils/`: Utility scripts for parsing utilization reports and checking timing closure.

## sim/
Simulation-related files and scripts.
- `scripts/`: Shell scripts for running different simulation environments (UVM, Verilator).
- `waveforms/`: Directory for storing waveform dumps:
  - `golden/`: Reference golden waveforms for regression testing.
  - `captured/`: Captured waveforms from simulation runs.

## scripts/
Utility scripts for build, test, and development processes.
- `build/`: Build automation scripts:
  - `build_fpga.sh`: Script to build FPGA bitstream.
  - `build_sw.sh`: Script to build embedded software.
  - `package_release.sh`: Script to package release artifacts.
- `util/`: Utility helper scripts:
  - `format_hdl.sh`: Script to format HDL files (using verible or similar).
  - `format_sw.sh`: Script to format software files (using clang-format).
  - `generate_docs.sh`: Script to generate documentation from source comments.
- `test/`: Test execution scripts:
  - `run_unit_tests.sh`: Script to run unit tests for both FPGA and software.
  - `run_integration_tests.sh`: Script to run integration tests.

## tests/
Test suite organized by test level.
- `unit/`: Unit tests:
  - `fpga/`: Unit tests for FPGA modules (arithmetic, display).
  - `sw/`: Unit tests for software components (HAL, libraries).
- `integration/`: Integration tests:
  - `hw_sw_interface/`: Tests for hardware-software communication via AXI.
  - `system/`: System-level integration tests.
- `system/`: System and acceptance tests:
  - `acceptance/`: Acceptance test procedures and scripts.

## assets/
Static assets used by the software.
- `images/`: Logos, screenshots, and other graphical assets.
- `fonts/`: Bitmap fonts for text rendering.
- `audio/`: Audio samples for any audio features.

## release/
Release artifacts organized by version.
- `v1.0.0/`: Example release directory containing bitstream, software binaries, and documentation.
- `latest/`: Symbolic link or copy of the most recent release.

## README.md
Top-level project overview and instructions.

This structure separates concerns clearly:
- Hardware design (fpga/) is isolated from software (embedsw/)
- Documentation (docs/) is centralized and standards-driven
- Tests (tests/) follow industry-standard unit/integration/system hierarchy
- Build and CI scripts (scripts/, .github/workflows/) automate the development lifecycle
- IP cores and block designs are organized for reuse
- Release management is versioned and traceable

Each directory serves a specific purpose in the professional engineering lifecycle, enabling scalability, maintainability, and clear handoff between hardware and software teams.