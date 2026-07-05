# Documentation Standards

## Overview
This document defines the documentation standards for the FPGA Graphing Calculator project. Consistent, high-quality documentation is essential for maintainability, knowledge transfer, and long-term project success.

## Documentation Types

### 1. Architecture Decision Records (ADRs)
ADRs capture significant architectural decisions along with their context and consequences.

#### Location
`docs/architecture/adr/`

#### Template
```markdown
# ADR-XXX: Title of the Decision

## Status
Proposed | Accepted | Superseded | Deprecated | Superseded

## Context
What is the issue that we're seeing that is motivating this decision or change?

## Decision
What is the change that we're proposing and/or doing?

## Consequences
What becomes easier or more difficult to do because of this change?
- List of concrete consequences

### Positive
- ...

### Negative
- ...
```

#### Examples
- ADR-001: Use AXI4-Stream for video data transfer between FPGAmodules
- ADR-002: Adopt IEEE 754-2008 compliant floating-point format
- ADR-003: Use FreeRTOS as the operating system kernel

### 2. Module Documentation
Each hardware module and software component must have documentation.

#### Hardware Modules (Verilog/SystemVerilog)
Each file must include a header block:

```verilog
/**
 * @file   fp_fp_
 * @author>Company Name
 * @date   2025-07-05
 * @brief  IEEE 754-2008 compliant single-precision floating-point adder
 *
 * @details
 * This module implements a single-precision floating-point adder
 * compliant with IEEE 754-2008 standard. It supports normal numbers,
 * subnormals, zero, infinity, and NaN values according to the standard.
 *
 * Pipeline Stages: 3
 * Latency: 3 clock cycles
 * Throughput: 1 operation per clock cycle
 *
 * Parameters:
 *   - EXP_WIDTH: Exponent width (default: 8 for single precision)
 *   - FRACTION_WIDTH: Fraction/mantissa width (default: 23 for single precision)
 *
 * Ports:
 *   - clk: Clock input
 *   - rst_n: Active-low asynchronous reset
 *   - operand_a: First operand (EXP_WIDTH+FRACTION_WIDTH bits)
 *   - operand_b: Second operand (EXP_WIDTH+FRACTION_WIDTH bits)
 *   - result: Sum of operand_a and operand_b
 *   - flags: Status flags [invalid_operation, overflow, underflow, division_by_zero, inexact]
 *
 * Dependencies:
 *   - normalizer.v
 *   - exception_detector.v
 *
 * References:
 *   - IEEE Standard 754-2008 for Floating-Point Arithmetic
 *   - "Computer Arithmetic: Algorithms and Hardware Designs" by Behrooz Parhami
 */
```

#### Software Components (C/C++)
Each header file must include documentation:

```c
/**
 * @file   expression_parser.h
 * @brief  Mathematical expression parser
 * @author Company Name
 * @date   2025-07-05
 *
 * This module provides functions for parsing mathematical expressions
 * in infix notation and converting them to an abstract syntax tree (AST)
 * for evaluation.
 *
 * Supported Operations:
 *   - Arithmetic: +, -, *, /, ^
 *   - Trigonometric: sin, cos, tan, asin, acos, atan
 *   - Hyperbolic: sinh, cosh, tanh
 *   - Logarithmic: log, log10, ln
 *   - Exponential: exp, pow
 *   - Constants: pi, e
 *
 * Dependencies:
 *   - ast.h
 *   - token.h
 *
 * Usage Example:
 * @code
 *   expr_t* expression = expr_parse("sin(x)^2 + cos(y)");
 *   double result = expr_eval(expression, vars);
 *   expr_free(expression);
 * @endcode
 */
```

### 3. API Documentation
Public APIs must be documented using Doxygen-compatible comments.

#### Doxygen Guidelines
- Use `/** ... */` for documentation blocks
- Use `\brief` for brief description (optional if first sentence serves as brief)
- Use `\details` for detailed description
- Use `\param [in,out,inout] name description` for parameters
- Use `\return` or `\retval` for return values
- Use `\note` for important notes
- Use `\warning` for important warnings
- Use `\see` for references to related functions/files
- Use `\code ... \endcode` for code examples
- Use `\deprecated` for deprecated interfaces

### 4. Hardware Documentation
#### Block Diagrams
- Created using draw.io (.dio format)
- Stored in `docs/diagrams/source/`
- Exported to PDF/PNG/SVG for inclusion in documents
- Must include:
  - Clear module labels
  - Signal names and widths
  - Clock domains
  - Reset signals
  - Interface types (AXI, etc.)

#### Timing Diagrams
- Created using WaveDrom or similar tools
- Show signal timing relationships
- Include clock cycles, setup/hold times
- Label all significant transitions

#### State Machine Diagrams
- Use standard state diagram notation
- Show states, transitions, conditions, and actions
- Include initial and final states where applicable
- Document reset behavior

### 5. Software Documentation
#### User Guides
- Task-oriented documentation
- Step-by-step procedures
- Screenshots where applicable
- Troubleshooting section
- FAQ

#### API References
- Generated from source code comments
- Organized by module
- Include parameter descriptions, return values, examples
- Note thread-safety and reentrancy

#### Developer Guides
- Build instructions
- Development environment setup
- Coding standards
- Testing procedures
- Debugging guidelines

### 6. File Naming Conventions
#### Documentation Files
- Use lowercase with hyphens as separators: `user-guide.pdf`
- Use descriptive names: `fpga-architecture-overview.docx`
- Version in filename when appropriate: `api-reference-v2.1.pdf`

#### Diagram Files
- Source: `description.dio`
- Exported: `description.pdf` or `description.png`
- Versions: `description_v2.dio`

### 7. Documentation Process
#### As Part of Definition of Done
- All code changes must include corresponding documentation updates
- New modules require documentation before being considered complete
- API changes require updated API documentation
- Architectural decisions require ADRs

#### Review Process
- Documentation reviewed alongside code in pull requests
- Technical writers review for clarity and completeness
- SMEs review for technical accuracy
- Documentation must pass spell-check and grammar-check tools

#### Versioning
- Documentation versioned with software releases
- Major documentation updates noted in release notes
- Archive previous versions in `docs/archive/`

### 8. Tools and Formats
#### Preferred Tools
- Diagrams: draw.io (diagrams.net)
- Documentation: Markdown (.md) for lightweight, PDF for formal documents
- API Documentation: Doxygen
- Spell Checking: aspell or similar
- Validation: markdownlint, proselint

#### Formats
- Source: Markdown for wikis and README, .dio for diagrams
- Internal sharing: PDF
- Archival: PDF/A for long-term preservation
- Web: HTML generated from Markdown

### 9. Language and Style
#### Language
- English (American spelling)
- Clear, concise, unambiguous
- Active voice preferred
- Present tense for describing current behavior

#### Style Guidelines
- Use consistent terminology throughout
- Define acronyms on first use
- Use SI units with appropriate prefixes
- Number figures and tables sequentially
- Provide descriptive captions for all figures and tables
- Use warnings and notes sparingly but effectively
- Follow company branding guidelines for templates

### 10. Accessibility
- Ensure sufficient color contrast in diagrams
- Provide alternative text for important images
- Use semantic markup in HTML documents
- Ensure documents are navigable via keyboard
- Provide transcripts for any audio content

### 11. Review and Approval
#### Review Checklist
- [ ] Technically accurate
- [ ] Complete and covers all relevant aspects
- [ ] Clear and understandable to target audience
- [ ] Consistent with terminology used elsewhere
- [ ] Properly formatted and styled
- [ ] Free of spelling and grammatical errors
- [ ] Includes necessary diagrams and examples
- [ ] Follows document templates
- [ ] Version and date information present

#### Approval
- All documentation must be reviewed by at least one peer
- Architectural documents require review by lead architect
- User-facing documents require review by technical writer and SME
- Final approval by documentation owner or project lead

### 12. Templates and Examples
Template files are available in:
- `docs/templates/ADR_TEMPLATE.md`
- `docs/templates/MODULE_HEADER_TEMPLATE.v`
- `docs/templates/API_HEADER_TEMPLATE.h`
- `docs/templates/USER_GUIDE_TEMPLATE.md`

## Compliance
Compliance with these standards will be verified through:
- Automated checks in CI pipeline
- Documentation reviews in pull requests
- Periodic documentation audits
- Feedback from documentation consumers

Exceptions to these standards must be requested and approved through the architecture review board.