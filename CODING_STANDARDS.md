# Coding Standards

## Overview
This document defines the coding standards for the FPGA Graphing Calculator project. Adhering to these standards ensures code maintainability, readability, and quality across both hardware (Verilog/SystemVerilog) and software (C/C++) components.

## 1. Language Standards
### 1.1 Hardware Description Languages
- **Primary Language**: SystemVerilog (IEEE 1800-2017)
- **Compatibility**: Code must be compatible with Verilog-2001 for maximum tool compatibility
- **Preferred Constructs**: Use SystemVerilog enhanced features where beneficial:
  - `logic` instead of `wire`/`reg`
  - `always_ff`/`always_comb`/`always_latch`
  - `struct`/`union`/`typedef`
  - `enum` for state machines
  - `assert` properties for protocol checking
  - `package` for shared definitions

### 1.2 Software Languages
- **Primary Language**: C (C99 standard)
- **Secondary Language**: C++ (C++17) where beneficial for abstraction
- **Compiler**: Xilinx Xillinx gcc arm-none-eabi
- **Strict Mode**: Compile with `-Wall -Wextra -Werror -pedantic`

## 2. File Organization

### 2.1 Header Comments
Every file must begin with a standard header comment block:

#### For HDL Files:
```verilog
/**
 * @file   <filename>.v
 * @brief  Brief description of the module's purpose
 * @author Company Name
 * @date   YYYY-MM-DD
 *
 * @details
 * Detailed description of the module functionality, including:
 * - Primary function
 * - Key features
 * - Important limitations or assumptions
 * - Interface description
 *
 * Parameters:
 *   PARAM_NAME: Description of parameter
 *
 * Ports:
 *   PORT_NAME: Description of port (direction, width)
 *
 * Dependencies:
 *   - list of dependent files or modules
 *
 * References:
 *   - [1] Specification or standard reference
 *   - [2] Relevant application note or paper
 *
 * Revision History:
 *   Rev X.Y  YYYY-MM-DD  Author  Description of changes
 */
```

#### For C/C++ Header Files:
```c
/**
 * @file   <filename>.h
 * @brief  Brief description of the module's purpose
 * @author Company Name
 * @date   YYYY-MM-DD
 *
 * @details
 * Detailed description of the module functionality, including:
 * - Primary function
 * - Key features
 * - Important limitations or assumptions
 * - Thread safety information
 *
 * Dependencies:
 *   - list of header files
 *
 * Notes:
 *   - Any important usage notes
 *
 * Example:
 * @code
 *   // Example usage code
 * @endcode
 */
```

#### For C/C++ Source Files:
```c
/**
 * @file   <filename>.c
 * @brief  Brief description of the file's purpose
 * @author Company Name
 * @date   YYYY-MM-DD
 *
 * @details
 * Detailed description of the file contents
 */
```

### 2.2 File Naming
- **HDL Files**: Use lowercase with underscore separation: `floating_point_adder.v`
- **C Files**: Use lowercase with underscore separation: `expression_parser.c`
- **Header Files**: Use lowercase with underscore separation: `expression_parser.h`
- **Constants Files**: Use `_constants` suffix: `math_constants.h`
- **Configuration Files**: Use `_config` suffix: `system_config.h`
- **Test Files**: Use `_test` or `_tb` suffix: `floating_point_adder_tb.v`

### 2.3 Directory Organization
Follow the structure defined in STRUCTURE.md and DIRECTORY_EXPLANATIONS.md.

## 3. Naming Conventions

### 3.1 HDL Naming
- **Modules**: `module_name` (lowercase_with_underscores)
- **Parameters**: `PARAMETER_NAME` (UPPERCASE_WITH_UNDERSCORES)
- **Local Parameters**: `LOCALPARAM_NAME` (UPPERCASE_WITH_UNDERSCORES)
- **Types**: `type_name_t` (lowercase_with_underscores_suffix_t)
- **Enums**: `enum_name_t` (lowercase_with_underscores_suffix_t)
- **Enum Values**: `ENUM_VALUE` (UPPERCASE_WITH_UNDERSCORES)
- **Signals/Wires**: `signal_name` (lowercase_with_underscores)
- **Registers**: `reg_name` (lowercase_with_underscores) - prefer `logic`
- **Constants**: `CONSTANT_NAME` (UPPERCASE_WITH_UNDERSCORES)
- **Functions/Tasks**: `function_name` (lowercase_with_underscores)
- **Generate Blocks**: `genblk_label` (descriptive_prefix)

### 3.2 Software Naming
- **Functions**: `function_name` (lowercase_with_underscores)
- **Variables**: `variable_name` (lowercase_with_underscores)
- **Pointers**: `ptr_variable_name` (pointer_prefix_optional)
- **Constants**: `CONSTANT_NAME` (UPPERCASE_WITH_UNDERSCORES)
- **Macros**: `MACRO_NAME` (UPPERCASE_WITH_UNDERSCORES)
- **Enumeration Types**: `enum_name_t` (lowercase_with_underscores_suffix_t)
- **Enumeration Values**: `ENUM_VALUE` (UPPERCASE_WITH_UNDERSCORES)
- **Struct/Union Types**: `struct_name_t` (lowercase_with_underscores_suffix_t)
- **Structure Members**: `member_name` (lowercase_with_underscores)
- **Global Variables**: `g_variable_name` (g_ prefix optional but recommended)
- **Static Variables**: `s_variable_name` (s_ prefix for file-static)
- **Function Parameters**: `parameter_name` (lowercase_with_underscores)
- **Loop Variables**: `i`, `j`, `k` for indices; descriptive names for others
- **Macros**: Use sparingly; prefer inline functions or const variables when possible

### 3.3 File and Variable Scope Indicators
- **File Scope (Static)**: `s_` prefix for variables/functions
- **Global Variables**: `g_` prefix (avoid when possible)
- **Private Functions**: `_private_function` (leading underscore)
- **Macros that Evaluate to Values**: ALL_CAPS
- **Macros that Execute Statements**: Named like functions but with documentation

## 4. Formatting and Layout

### 4.1 Indentation and Whitespace
- **Indentation Width**: 2 spaces for HDL, 4 spaces for C/C++
- **No Tabs**: Configure editors to insert spaces instead of tabs
- **Line Length**: Maximum 120 characters for HDL, 100 characters for C/C++
- **Trailing Whitespace**: Not allowed
- **End of File**: Must end with a newline character

### 4.2 HDL Specific Formatting
#### Module Declaration
```verilog
module floating_point_adder #
(
    parameter int EXP_WIDTH = 8,
    parameter int FRACTION_WIDTH = 23
)
(
    input  logic                    clk,
    input  logic                    rst_n,
    input  logic [EXP_WIDTH+FRACTION_WIDTH-1:0] operand_a,
    input  logic [EXP_WIDTH+FRACTION_WIDTH-1:0] operand_b,
    output logic [EXP_WIDTH+FRACTION_WIDTH-1:0] result,
    output logic [4:0]                  flags  // [invalid, overflow, underflow, div0, inexact]
);
```

#### Procedural Blocks
```verilog
// Sequential logic
always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        // asynchronous reset
        state <= IDLE;
    end else begin
        // synchronous logic
        state <= next_state;
    end
end

// Combinational logic
always_comb begin
    // Default assignments to prevent latches
    next_state = state;
    output_valid = 1'b0;
    
    case (state)
        IDLE: begin
            if (input_valid) begin
                next_state = PROCESS;
            end
        end
        // ... other states
    endcase
end
```

### 4.3 C/C++ Specific Formatting
#### Indentation and Braces
- **K&R Style**: Braces on same line as control statement
```c
if (condition) {
    // statements
} else {
    // statements
}

for (initialization; condition; increment) {
    // statements
}

while (condition) {
    // statements
}

do {
    // statements
} while (condition);

switch (value) {
    case CASE_A:
        // statements
        break;
    case CASE_B:
        // statements
        break;
    default:
        // statements
        break;
}
```

#### Function Definitions
```c
return_type function_name(
    param_type param1,
    param_type param2
) {
    // function body
}
```

#### Pointer and Reference Declarations
- Place `*` with the variable name, not the type:
```c
int *ptr;          // Correct
int* ptr;          // Incorrect
int * ptr;         // Avoid this style
```

### 4.4 Commenting Style
#### File Headers
As specified in Section 2.1

#### Section Comments
Use to separate logical sections within a file:
```c
/*==============================================================================
 *  SECTION: Initialization Functions
 *============================================================================*/
```

#### TODO and FIXME Comments
- Use `TODO:` for features to be implemented
- Use `FIXME:` for known issues that need correction
- Include ticket/reference if applicable: `TODO: JIRA-123 Implement hyperbolic functions`
- Review regularly during development

## 5. Language-Specific Guidelines

### 5.1 HDL (SystemVerilog/Verilog) Guidelines

#### 5.1.1 Module Design
- **Encapsulation**: Modules should have a single, well-defined purpose
- **Interface Clarity**: Clearly separate data, control, and clock/reset signals
- **Parameterization**: Make width and depth parameters where applicable
- **Reset Strategy**: Use asynchronous active-low reset where appropriate
- **Clock Domains**: Clearly mark clock domains; use proper CDC techniques for cross-domain signals

#### 5.1.2 Procedural Blocks
- **Flip-Flops**: Always use `always_ff` with explicit sensitivity list
- **Combinational Logic**: Always use `always_comb`
- **Latches**: Avoid latches; if necessary, use `always_latch` with explicit comment
- **Blocking vs Non-blocking**:
  - Use `<=` for sequential logic (`always_ff`)
  - Use `=` for combinational logic (`always_comb`)
- **Default Values**: Always provide default values in combinational blocks to prevent latches

#### 5.1.3 Signals and Variables
- **Net Types**: Use `logic` for all signals (replaces `wire`/`reg`)
- **Constants**: Use `localparam` for constants, `parameter` only if needs to be overridden
- **Data Types**: Use appropriate width types; avoid unsized literals
- **Enumerated Types**: Use `enum` for state machines and related constants
- **Structs/Packs**: Use `struct packed` for data that needs to be treated as vectors
- **Arrays**: Prefer fixed-size arrays when size is known

#### 5.1.4 Procedural Coding
- **Case Statements**: Include `default` case; use `unique` or `priority` if mutually exclusive
- **If-Else**: Use `else if` chaining for multiple conditions
- **Loop Limits**: Ensure loops have determinable bounds for synthesis
- **Generate Blocks**: Use for parameterized replication; label clearly

#### 5.1.5 Clocking and Reset
- **Clock Buffers**: Use clock buffering primitives when necessary
- **Reset Synchronization**: Synchronize asynchronous resets if used for synchronous logic
- **Reset Release**: Consider reset release timing to avoid metastability
- **Gated Clocks**: Avoid gated clocks; use clock enables instead

#### 5.1.6 Memory and Registers
- **Memory Inference**: Use consistent patterns for RAM/ROM inference
- **Initial Values**: Be aware that initial values may not synthesize; use reset for known state
- **Shift Registers**: Use explicit shift register coding style for inference

#### 5.1.7 Naming and Hierarchy
- **Hierarchical Names**: Use hierarchical naming with dots (`module_instance.signal`)
- **Instance Names**: Use descriptive instance names: `fpu_adder_inst`
- **Generate Blocks**: Label for clarity: `genvar i; generate for (i=0; i<N; i++) begin : gen_name`

#### 5.1.8 Assertions and Coverage
- **Assertions**: Use SVA (SystemVerilog Assertions) for protocol checking
- **Functional Coverage**: Add cover groups for complex state machines
- **Disable Conditions**: Understand when to disable assertions during reset

### 5.2 Software (C/C++) Guidelines

#### 5.2.1 Language Usage
- **Standard Compliance**: Write standard C99/C++17; avoid compiler extensions unless necessary and documented
- **Portability**: Avoid hardware-specific code in portable layers; use HAL for hardware access
- **Standard Library**: Use standard library functions where appropriate and safe
- **Dynamic Memory**: Minimize use in embedded systems; prefer static allocation or memory pools
- **Recursion**: Avoid deep recursion; use iteration when possible
- **Volatile**: Use correctly for memory-mapped registers and ISR-shared variables
- **Restrict**: Use `restrict` qualifier for pointers when appropriate to enable optimization

#### 5.2.2 Preprocessor and Macros
- **Include Guards**: Use in all header files:
```c
#ifndef MODULE_NAME_H
#define MODULE_NAME_H
// contents
#endif // MODULE_NAME_H
```
- **Macro Safety**: Use do-while(0) for multi-statement macros:
```c
#define MACRO_NAME(arg) do { \
    do_something((arg)); \
    do_another_thing(); \
} while (0)
```
- **Parentheses**: Always macro parameters in parentheses
- **Side Effects**: Avoid macros with side effects in arguments
- **Debugging**: Use `#ifdef DEBUG` for debug code; consider using logging framework instead

#### 5.2.3 Data Types
- **Integer Types**: Use stdint.h types for explicit width:
  - `int8_t`, `int16_t`, `int32_t`, `int64_t`
  - `uint8_t`, `uint16_t`, `uint32_t`, `uint64_t`
- **Boolean**: Use `stdbool.h` and `bool` type
- **Floating Point**: Use `float` and `double` as needed; note precision constraints
- **Size and Pointerdiff**: Use `size_t` and `ptrdiff_t` for sizes and pointer differences
- **Fixed Width**: Whenever size matters, use explicit-width types
- **Promotion Rules**: Understand integer promotion rules to avoid surprises

#### 5.2.4 Functions
- **Size**: Keep functions small and focused (< 50 lines preferred)
- **Parameters**: Limit parameters; consider structs for related parameters
- **Return Values**: Use return values for function results; use pointers for outputs when necessary
- **Error Checking**: Check return values from functions; handle errors appropriately
- **Side Effects**: Minimize and document side effects
- **Pure Functions**: Mark functions that don't modify state as conceptually pure
- **Recursion**: Avoid in embedded systems unless depth is bounded and small

#### 5.2.5 Memory Management
- **Allocation**: Check return value of `malloc`/`calloc`/`realloc`
- **Deallocation**: Always free allocated memory; set pointer to NULL after free
- **Ownership**: Clearly document ownership semantics for passed pointers
- **Buffers**: Always specify buffer lengths; use length-limited functions (`strncpy` vs `strcpy`)
- **Overflow**: Prevent buffer overflows through proper bounds checking
- **Initialization**: Initialize all variables before use
- **Stack vs Heap**: Prefer static allocation for predictable usage; monitor stack usage

#### 5.2.6 Error Handling
- **Return Codes**: Use error return types where appropriate
- **Assertions**: Use `assert()` for catching programming errors during development
- **Graceful Degradation**: Implement fallback behavior when possible
- **Error Reporting**: Use consistent error reporting mechanism (logging, callbacks, etc.)
- **Resource Leaks**: Check for and prevent resource leaks (memory, file handles, etc.)

#### 5.2.7 Concurrency (If Applicable)
- **Mutexes**: Use mutexes for shared resource protection
- **Semaphores**: Use semaphores for signaling and resource counting
- **Priority Inversion**: Be aware of and prevent priority inversion
- **Deadlock Avoidance**: Follow consistent locking order to prevent deadlocks
- **Interrupt Safety**: Use proper techniques for ISR-safe data sharing
- **Atomic Operations**: Use atomic types for simple shared variables when possible

#### 5.2.8 Specific C Constructs
- **Structs**: Always declare struct tag and typedef separately for clarity:
```c
typedef struct {
    int member1;
    float member2;
} my_struct_t;
```
- **Unions**: Use with extreme caution; ensure proper active member tracking
- **Bit Fields**: Avoid or use with caution due to implementation-defined behavior
- **Flexible Array Members**: Use C99 flexible array members when appropriate
- **Inline Functions**: Use `static inline` for small, frequently called functions
- **Restrict Qualifier**: Use `restrict` for pointers when they don't alias to enable optimization

## 6. Documentation Requirements

### 6.1 Commenting Practices
- **Self-Documenting Code**: Strive for code that explains itself through good names and structure
- **Comment Why, Not What**: Comments should explain intent, not repeat what the code does
- **Out-of-Date Comments**: Avoid comments that quickly become outdated; prefer assertions or clear code
- **TODO Comments**: Use as specified in Section 4.4
- **Reference Comments**: Include references to specifications, standards, or algorithms when implementing complex logic
- **Legal Notices**: Include appropriate copyright and license headers as required

### 6.2 Header File Contents
Header files should contain:
- Include guards
- Necessary #includes
- Macro definitions
- Type definitions (structs, enums, typedefs)
- Function prototypes
- External variable declarations (`extern`)
- Inline functions
- Documentation comments

Header files should NOT contain:
- Function definitions (except inline)
- Variable definitions (except const)
- Executable code

### 6.3 Source File Contents
Source files should contain:
- Necessary #includes (typically the corresponding header first)
- Function definitions
- Static variable definitions
- Static function definitions
- Implementation details

## 7. Naming Conventions Summary

### 7.1 HDL Summary
| Item | Convention | Example |
|------|------------|---------|
| Module | lowercase_with_underscores | `floating_point_adder` |
| Parameters | UPPERCASE_WITH_UNDERSCORES | `DATA_WIDTH` |
| Localparams | UPPERCASE_WITH_UNDERSCORES | `LOCALPARAM_NAME` |
| Types | lowercase_with_underscores_t | `state_t` |
| Enums | lowercase_with_underscores_t | `state_t` |
| Enum Values | UPPERCASE_WITH_UNDERSCORES | `STATE_IDLE` |
| Signals/Wires | lowercase_with_underscores | `data_valid` |
| Registers | lowercase_with_underscores | `state_reg` |
| Constants | UPPERCASE_WITH_UNDERSCORES | `MAX_COUNT` |
| Functions/Tasks | lowercase_with_underscores | `calculate_sum` |

### 7.2 Software Summary
| Item | Convention | Example |
|------|------------|---------|
| Functions | lowercase_with_underscores | `calculate_sum` |
| Variables | lowercase_with_underscores | `sum_result` |
| Pointers | lowercase_with_underscores | `ptr_result` |
| Constants | UPPERCASE_WITH_UNDERSCORES | `MAX_BUFFER_SIZE` |
| Macros | UPPERCASE_WITH_UNDERSCORES | `CONVERT_TO_DEGREES` |
| Enums | lowercase_with_underscores_t | `error_t` |
| Enum Values | UPPERCASE_WITH_UNDERSCORES | `ERROR_NONE` |
| Structs | lowercase_with_underscores_t | `point_t` |
| Struct Members | lowercase_with_underscores | `x_coord` |
| Globals | g_ prefix (optional) | `g_system_state` |
| Statics | s_ prefix (optional) | `s_counter` |

## 8. Code Organization

### 8.1 File Organization
#### Header Files (.h)
1. File header comment
2. Copyright/license notice
3. Include guards
4. #includes (standard first, then project-specific)
5. Macros and #defines
6. Type definitions (enum, struct, typedef)
7. Global variable declarations (extern)
8. Function prototypes
9. Inline function definitions
10. End of file comment (optional)

#### Source Files (.c)
1. File header comment
2. Copyright/license notice
3. #include corresponding header first
4. Other #includes (standard first, then project-specific)
5. Static macro definitions
6. Static type definitions (if used only in this file)
7. Static variable definitions
8. Static function definitions
9. Global function definitions
10. End of file comment (optional)

### 8.2 Function Organization
Within each function:
1. Parameter variable declarations (at function start)
2. Local variable declarations (at function start, grouped by type)
3. Input validation and error checking
4. Main algorithm implementation
5. Cleanup and return

### 8.3 Header File Includes
Order of includes:
1. Corresponding header (to ensure it's self-contained)
2. Standard library headers (`#include <stdio.h>`)
3. POSIX/OS-specific headers (`#include <unistd.h>`)
4. Project-specific headers (`#include "project/types.h"`)
5. Other libraries (`#include <math.h>`)

## 9. Safety and Security Considerations

### 9.1 Safety-Critical Practices
- **Defensive Programming**: Assume inputs may be invalid; validate all inputs
- **Fail-Safe Defaults**: Default to safe state on error conditions
- **Resource Management**: Always acquire resources in consistent order; always release
- **State Consistency**: Ensure object/state consistency even in error cases
- **Async Signal Safety**: Use only async-signal-safe functions in signal handlers
- **Interrupt Safety**: Minimize work in ISRs; use flags to defer processing

### 9.2 Security Practices
- **Input Validation**: Validate all external inputs for length, range, and content
- **Buffer Overflow Prevention**: Use length-limited functions; validate indices
- **Format String Safety**: Never pass user input as format string to printf family
- **Command Injection**: Avoid constructing commands from user input; if necessary, use proper escaping
- **Information Leakage**: Avoid emitting sensitive information in error messages
- **Use After Free**: Nullify pointers after free; use static analysis tools
- **Race Conditions**: Use proper synchronization for shared state

### 9.3 Reliability Practices
- **Error Detection**: Use appropriate error detection (checksums, parity, ECC)
- **Error Recovery**: Implement recovery strategies for transient errors
- **Watchdogs**: Use watchdog timers where appropriate; feed regularly
- **Stack Monitoring**: Monitor stack usage; implement stack overflow detection
- **Memory Protection**: Use MPU/MMU where available to protect memory regions
- **Clock Monitoring**: Monitor clock stability where applicable
- **Voltage Monitoring**: Monitor supply voltages where sensing available

## 10. Tools and Verification

### 10.1 Formatting Tools
- **HDL**: Verilator lint, jalint, or similar linters
- **C/C++**: clang-format with project-specific configuration
- **Automatic Formatters**: Configure IDEs to format on save

### 10.2 Static Analysis
- **HDL**: Linting tools (Ultrascent, Spyglass) for potential issues
- **C/C++**: 
  - clang-tidy for bug detection and style
  - cppcheck for static analysis
  - Coverity Scan for defect detection
  - PVS-Studio for deep analysis
- **Complexity Metrics**: Monitor cyclomatic complexity; refactor high-complexity functions

### 10.3 Testing
- **Unit Tests**: Write tests for each function/module
- **Code Coverage**: Aim for >80% line coverage, >70% branch coverage
- **Static Analysis**: Run as part of CI pipeline
- **Dynamic Analysis**: Use valgrind, AddressSanitizer, ThreadSanitizer where applicable
- **Fuzzing**: Consider for input-parsing components

### 10.4 Metrics and Monitoring
- **Complexity**: Track cyclomatic complexity per function
- **Dependencies**: Monitor header inclusion and coupling
- **Duplication**: Check for code duplication; refactor common code
- **Dependencies**: Track external library versions and licenses

## 11. Exceptions and Waivers
Any deviation from these standards must:
1. Be documented in the code with justification
2. Be reviewed and approved during code review
3. Be rare and well-justified
4. Include a plan for refactoring to compliance when feasible

## 12. References and Standards
- **MISRA C:2012** - Guidelines for safety-critical C code
- **CERT C Coding Standard** - Secure coding guidelines
- **SystemVerilog Assertions** - IEEE 1800-2017
- **Verification Methodology Manual for SystemVerilog** - Ovral et al.
- **The Practice of Programming** - Kernighan and Pike
- **Clean Code** - Robert Martin
- **Effective C++** - Scott Meyers
- **Linux Kernel Coding Style** - Documentation/process/coding-style.rst

---
*These standards are subject to periodic review and update. Project leads may establish project-specific variations with appropriate justification and documentation.*