# Repository Structure

.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── documentation_request.md
│   ├── PULL_REQUEST_TEMPLATE/
│   │   ├── bug_fix.md
│   │   ├── feature.md
│   │   └── documentation.md
│   └── workflows/
│       ├── ci.yml
│       ├── nightly.yml
│       └── release.yml
├── docs/
│   ├── architecture/
│   │   ├── adr/
│   │   ├── block_diagrams/
│   │   ├── sequence_diagrams/
│   │   └── state_machines/
│   ├── datasheets/
│   ├── diagrams/
│   │   ├── drawio/
│   │   └── exported/
│   ├── meeting_notes/
│   └── standards/
│       ├── coding_standards.md
│       ├── commit_conventions.md
│       └── documentation_standards.md
├── embedsw/
│   ├── bsp/
│   │   └── zybo_z7/
│   ├── drivers/
│   │   ├── axi_dma/
│   │   ├── axi_gpio/
│   │   ├── axi_iic/
│   │   ├── axi_timer/
│   │   ├── hdmi_tx/
│   │   ├── i2s_audio/
│   │   └── vdma/
│   ├── hal/
│   │   ├── include/
│   │   └── src/
│   ├── libraries/
│   │   ├── math/
│   │   │   ├── fixed_point/
│   │   │   ├── floating_point/
│   │   │   └── polynomial/
│   │   ├── parser/
│   │   │   ├── expression/
│   │   │   └── function/
│   │   ├── graph/
│   │   │   ├── engine/
│   │   │   └── rasterizer/
│   │   └── ui/
│   │       ├── themes/
│   │       └── widgets/
│   ├── apps/
│   │   └── calculator/
│   │       ├── src/
│   │   │   ├── main.c
│   │   │   ├── menu.c
│   │   │   ├── graph.c
│   │   │   └── utils.c
│   │   └── Makefile
│   └── boot/
│       ├── boot.s
│       ├── linker.ld
│       └── Makefile
├── fpga/
│   ├── src/
│   │   ├── hdl/
│   │   │   ├── rtl/
│   │   │   │   ├── arithmetic/
│   │   │   │   │   ├── fp_adder.v
│   │   │   │   │   ├── fp_multiplier.v
│   │   │   │   │   ├── fixed_point_virtex.v
│   │   │   │   │   └── cordic.v
│   │   │   │   ├── display/
│   │   │   │   │   ├── hdmi_encoder.v
│   │   │   │   │   ├── vga_timing.v
│   │   │   │   │   └── framebuffer.v
│   │   │   │   ├── memory/
│   │   │   │   │   ├── ddr3_controller.v
│   │   │   │   │   └── arbiter.v
│   │   │   │   ├── axi/
│   │   │   │   │   ├── axi_lite_interface.v
│   │   │   │   │   ├── axi_stream_vdma.v
│   │   │   │   │   └── axi_mm_bridge.v
│   │   │   │   └── utils/
│   │   │   │       ├── synchronizer.v
│   │   │   │       └── clock_divider.v
│   │   │   ├── sim/
│   │   │   │   ├── testbenches/
│   │   │   │   │   ├── tb_fp_adder.v
│   │   │   │   │   └── tb_framebuffer.v
│   │   │   │   └── scripts/
│   │   │   └── tb/
│   │   │       ├── data/
│   │   │       └── golden/
│   │   ├── ip/
│   │   │   ├── custom_math_accelerator/
│   │   │   │   ├── src/
│   │   │   │   └── sim/
│   │   │   └── display_pipeline/
│   │   │       ├── src/
│   │   │       └── sim/
│   │   └── bd/
│   │       ├── system.bd
│   │       └── ip_repo/
│   ├── vivo/
│   │   ├── projects/
│   │   │   ├── zybo_z7/
│   │   │   │   ├── src/
│   │   │   │   ├── constrs/
│   │   │   │   │   ├── system.xdc
│   │   │   │   │   └── platform.xdc
│   │   │   │   ├── runs/
│   │   │   │   └── impl/
│   │   │   └── scripts/
│   │   │       ├── create_bd.tcl
│   │   │       ├── generate_bitstream.tcl
│   │   │       └── run_simulation.tcl
│   │   └── doc/
│   │       ├── specs/
│   │       │   ├── fpga_spec.md
│   │       │   └── axi_interface_spec.md
│   │       └── reports/
│   │           ├── synthesis/
│   │           │   ├── utilization.rpt
│   │   │   │   └── timing.rpt
│   │   │   └── implementation/
│   │   │       ├── power.rpt
│   │   │   │   └── timing_summary.rpt
│   │   └── utils/
│   │       ├── parse_utilization.tcl
│   │       └── check_timing.tcl
├── sim/
│   ├── scripts/
│   │   ├── run_uvm.sh
│   │   └── run_verilator.sh
│   └── waveforms/
│       ├── golden/
│       └── captured/
├── scripts/
│   ├── build/
│   │   ├── build_fpga.sh
│   │   ├── build_sw.sh
│   │   └── package_release.sh
│   ├── util/
│   │   ├── format_hdl.sh
│   │   ├── format_sw.sh
│   │   └── generate_docs.sh
│   └── test/
│       ├── run_unit_tests.sh
│       └── run_integration_tests.sh
├── tests/
│   ├── unit/
│   │   ├── fpga/
│   │   │   ├── arithmetic/
│   │   │   └── display/
│   │   └── sw/
│   │       ├── hal/
│   │       └── libraries/
│   ├── integration/
│   │   ├── hw_sw_interface/
│   │   └── system/
│   └── system/
│       └── acceptance/
├── assets/
│   ├── images/
│   │   ├── logo/
│   │   └── screenshots/
│   ├── fonts/
│   │   └── bitmap/
│   └── audio/
│       └── samples/
├── release/
│   ├── v1.0.0/
│   │   ├── bitstream/
│   │   ├── software/
│   │   └── documentation/
│   └── latest/
└── README.md