# Contributing to FPGA Graphing Calculator

Thank you for considering contributing to our project! We welcome contributions from the community to help improve this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation Standards](#documentation-standards)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

## How Can I Contribute?

### Reporting Bugs
Before submitting a bug report, please check if it has already been reported by searching the [Issues](https://github.com/yourusername/fpga-graphing-calculator/issues). When you are creating a bug report, please include as many details as possible including:
- Steps to reproduce the issue
- Expected behavior vs. actual behavior
- FPGA bitstream version and software version
- Screenshots or logs if applicable
- Your development environment details

### Suggesting Features
Feature requests are welcome! Please open an issue describing:
- The problem your feature would solve
- How the feature would work
- Any potential drawbacks or considerations
- Why this feature aligns with project goals

### Contributing Code
1. Fork the repository
2. Create a new branch from `main`: `git checkout -b feature/amazing-feature`
3. Make your changes following our coding standards
4. Add tests for your changes
5. Ensure all tests pass
6. Commit your changes using conventional commit messages
7. Push to your branch: `git push origin feature/amazing-feature`
8. Open a Pull Request against the `main` branch

## Development Setup

### Prerequisites
- Xilinx Vivado 2023.2+
- Xilinx Vitis 2023.2+
- Git
- Make
- Python 3.8+ (for scripts)
- Verilator (optional, for simulation)

### Setup Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fpga-graphing-calculator.git
   cd fpga-graphing-calculator
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Source the Vivado and Vitis settings (adjust paths as needed):
   ```bash
   source /opt/Xilinx/Vivado/2023.2/settings64.sh
   source /opt/Xilinx/Vitis/2023.2/settings64.sh
   ```

4. Verify your setup:
   ```bash
   ./scripts/util/check_setup.sh
   ```

## Pull Request Process

1. Ensure your code passes all tests and follows coding standards
2. Update documentation as needed
3. The PR will be reviewed by at least one maintainer
4. Address any review comments
5. Once approved, maintainers will merge your PR
6. Your branch will be deleted after merging

### What Makes a Good PR?
- Addresses a single concern/feature
- Includes comprehensive tests
- Follows coding standards
- Includes updated documentation
- Has clear, descriptive commit messages

## Coding Standards

### Verilog/SystemVerilog
- Follow [SystemVerilog IEEE 1800-2017] standards
- Use non-blocking assignments (`<=`) for sequential logic
- Use blocking assignments (`=`) for combinational logic
- Use `always_ff` for clocked blocks and `always_comb` for combinational blocks
- Parameterize modules using `localparam` for constants
- Use `typedef` for complex data types
- Follow naming conventions:
  - Modules: `module_name`
  - Signals: `signal_name`
  - Parameters: `PARAMETER_NAME`
  - States in FSMs: `STATE_NAME`
- Include proper header documentation for each module
- Limit line length to 120 characters
- Use 2-space indentation

### Embedded C/C++
- Follow MISRA C:2012 guidelines where applicable
- Use ANSI C (C99) or C++17 standards
- Use descriptive names for variables and functions
- Functions should be short and focused (under 50 lines when possible)
- Header files should include proper include guards
- Error handling should be explicit and consistent
- Use `const` correctness extensively
- Avoid magic numbers; use named constants
- Limit line length to 100 characters
- Use 4-space indentation

### Documentation
- All public functions and modules must have Doxygen-style comments
- Header files should describe interface contracts
- Complex algorithms should include references or explanations
- State machines should include state diagrams in documentation
- Register maps should be documented with bitfield descriptions

## Testing Guidelines

### Unit Tests
- Unit tests should be written for all new functionality
- Test both normal operation and edge cases
- Mock hardware dependencies when testing software
- For FPGA modules, create directed and random testbenches
- Aim for >80% code coverage
- Test files should be named `*_test.cpp` or `*_tb.v`

### Integration Tests
- Test hardware-software interfaces thoroughly
- Test end-to-end functionality of major features
- Include performance benchmarks where applicable
- Test on actual hardware when possible

### Running Tests
- Software unit tests: `./scripts/test/run_unit_tests.sh sw`
- FPGA unit tests: `./scripts/test/run_unit_tests.sh fpga`
- All tests: `./scripts/test/run_all_tests.sh`

## Documentation Standards

### Architecture Decision Records (ADRs)
- Significant architectural decisions should be documented as ADRs
- ADRs should be stored in `docs/architecture/adr/`
- Follow the template in `docs/architecture/adr/TEMPLATE.md`

### API Documentation
- Generate Doxygen documentation for software components
- Generate documentation for FPGA IP cores
- Keep documentation up-to-date with code changes

### Diagrams
- Use draw.io (.dio) for diagrams
- Store source diagrams in `docs/diagrams/source/`
- Export to PDF/PNG/SVG for inclusion in documentation
- Label all signals, buses, and components clearly

## Reporting Bugs

When reporting a bug, please include:
1. **Clear title**: Descriptive and concise
2. **Steps to reproduce**: Numbered list of actions
3. **Expected behavior**: What should happen
4. **Actual behavior**: What actually happens
5. **Environment**:
   - FPGA bitstream version (if applicable)
   - Software version
   - Vivado/Vitis version
   - Board revision
   - Any relevant peripheral connections
6. **Additional context**: Logs, screenshots, waveforms

## Suggesting Features

When suggesting a feature, please include:
1. **Problem statement**: What problem does this solve?
2. **Proposed solution**: How would the feature work?
3. **Alternatives considered**: Other approaches you thought about
4. **Impact**: How will this affect users and the codebase?
5. **Implementation suggestions**: If you have ideas on how to implement it

## Community

- Join our discussions in the [Discussions](https://github.com/username/fpga-graphing-calculator/discussions) tab
- Follow us on Twitter [@FPGACalc](https://twitter.com/FPGACalc) for updates
- Check out our [projects](https://github.com/username/fpga-graphing-calculator/projects) for roadmap and current work

## Getting Help

If you need help with your contribution:
1. Check the [documentation](docs/)
2. Look through existing [issues](https://github.com/username/fpga-graphing-calculator/issues)
3. Ask in the [Discussions](https://github.com/username/fpga-graphing-calculator/discussions)
4. Contact a maintainer directly

Thank you again for contributing to our project!

---
*Based on the Contributor Covenant v2.1*