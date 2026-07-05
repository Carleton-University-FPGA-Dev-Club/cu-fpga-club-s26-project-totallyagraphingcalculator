# FPGA Graphing Calculator

A high-performance graphing calculator implemented on the Xilinx Zynq-7000 SoC (Zybo Z7 development board) featuring hardware-accelerated mathematical operations, HDMI/VGA output, and an intuitive graphical user interface.

## Features

- Hardware-accelerated floating-point arithmetic (addition, multiplication, trigonometric functions)
- Fixed-point math co-processor for efficient fixed-point calculations
- Expression parser with support for variables, functions, and complex expressions
- Real-time 2D graphing with pan/zoom capabilities
- Multiple graphing modes: Cartesian, parametric, polar
- HDMI 1080p60 and VGA 640x480 display outputs
- Stereo audio output for function sonification
- Intuitive touchscreen and button-driven user interface
- Expandable architecture for adding new mathematical functions

## Repository Structure

See [STRUCTURE.md](STRUCTURE.md) for detailed directory organization and [DIRECTORY_EXPLANATIONS.md](DIRECTORY_EXPLANATIONS.md) for explanations of each directory's purpose.

## Getting Started

### Prerequisites

- Xilinx Vivado 2023.2 or later
- Xilinx Vitis 2023.2 or later
- Zybo Z7 development board
- USB-JTAG programming cable
- HDMI or VGA display
- Optional: USB keyboard/mouse, audio output

### Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fpga-graphing-calculator.git
   cd fpga-graphing-calculator
   ```

2. Build the FPGA bitstream:
   ```bash
   ./scripts/build/build_fpga.sh
   ```

3. Build the software application:
   ```bash
   ./scripts/build/build_sw.sh
   ```

4. Generate boot image and program the board:
   ```bash
   ./scripts/build/package_release.sh
   ```

5. Connect the board to power and JTAG, then program the flash:
   ```bash
   vivado -mode batch -source scripts/vivo/scripts/flash_bitstream.tcl
   ```

## Documentation

- [Architecture Documentation](docs/architecture/)
- [FPGA Design Specifications](docs/fpga/doc/specs/)
- [Software API Reference Manual](docs/embedsw/)
- [Usage Guide](docs/user_guide.md) (coming soon)

## Development

### Building Individual Components

- **FPGA only**: `./scripts/build/build_fpga.sh --bitstream-only`
- **Software only**: `./scripts/build/build_sw.sh --sw-only`
- **Unit tests**: `./scripts/test/run_unit_tests.sh`
- **Integration tests**: `./scripts/test/run_integration_tests.sh`

### Code Formatting

- **HDL files**: `./scripts/util/format_hdl.sh`
- **Software files**: `./scripts/util/format_sw.sh`
- **Documentation**: `./scripts/util/generate_docs.sh`

### Continuous Integration

GitHub Actions workflows are configured in `.github/workflows/`:
- Build verification on every push
- Nightly builds with full test suite
- Release packaging on tag pushes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Xilinx University Program for hardware donations
- Open-source math libraries (Cephes, Boost.Math) for reference implementations
- The open-source FPGA community for inspiration and shared IP cores

---
*Developed for educational and demonstration purposes. Not intended for use in safety-critical applications.*